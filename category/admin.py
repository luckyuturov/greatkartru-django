from unicodedata import category
from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    'Класс для автозаполнения поля slug'
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)#Регистрируем модуль Категории для вывода полей в админке
