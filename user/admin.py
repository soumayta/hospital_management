from django.contrib import admin
from django.db.models import fields
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = '__all__'

