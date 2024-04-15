from django.contrib import admin
from .models import Library, UserAccount, Book


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'state_facility')
    search_fields = ('name', 'address')


@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'image')
    search_fields = ('username', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publishing_house', 'library', 'remain_count')
    search_fields = ('title', 'author', 'publishing_house')
    filter_horizontal = ('users',)
