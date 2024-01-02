from django.db import models
from django.contrib.auth.models import User
from tasks.utils import title_slugification
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from django.urls import reverse

# Create your models here.
class TaskQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(description__icontains=query)
        return self.filter(lookups) 

class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(max_length=5, choices=PRIORITY_CHOICES, default='L')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pending = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    objects = TaskManager()

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("tasks:task_detail_view", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')


def task_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        title_slugification(instance, save=False)
pre_save.connect(task_pre_save, sender=Task)

def task_post_save(sender, instance, created, *args, **kwargs):
    if created:
        title_slugification(instance, save=True)
post_save.connect(task_post_save, sender=Task)