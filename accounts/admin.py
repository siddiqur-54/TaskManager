from django.contrib import admin
from accounts.models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['user', 'contact']
    search_fields = ['user', 'contact', 'birth_date', 'gender', 'blood_group']

admin.site.register(Person, PersonAdmin)