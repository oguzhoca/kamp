from django.contrib import admin
from . models import Client, Category

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',  'piece')
    list_filter = ('name',)
    search_fields = ('name', )

@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
