from django.contrib import admin
from .models import Book

@admin.register(Book) 
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'price', 'isbn']
    search_fields = ['title', 'author', 'isbn']
    list_filter = ['author'] 

