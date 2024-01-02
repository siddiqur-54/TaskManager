import random
from django.utils.text import slugify


def title_slugification(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug=new_slug
    else:
        slug=slugify(instance.title)
    Klass=instance.__class__
    query_set=Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if query_set.exists():
        rand_int=random.randint(100_000,500_000)
        slug=f"{slug}-{rand_int}"
        return title_slugification(instance, save=save, new_slug=slug)
    instance.slug=slug
    if save:
        instance.save()
    return instance