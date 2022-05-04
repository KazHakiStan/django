from django.contrib import admin

# Register your models here.
from .models import Post


#admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    ordering = ('-created_at', '-id')
    readonly_fields = ('created_at',)