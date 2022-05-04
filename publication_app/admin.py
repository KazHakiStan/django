from django.contrib import admin

# Register your models here.
from .models import Post, People


#admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    ordering = ('-created_at', '-id')
    readonly_fields = ('created_at',)


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role')
    ordering = ('-id',)