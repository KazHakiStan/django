from django.contrib import admin

# Register your models here.
from .models import Post, People, Comments, Profile


#admin.site.register(Post)

class PostInline(admin.StackedInline):
    model = Comments
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    ordering = ('-created_at', '-id')
    readonly_fields = ('created_at',)
    inlines = [PostInline]


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role')
    ordering = ('-id',)


admin.site.register(Comments)


admin.site.register(Profile)
# @admin.register(Comments)
# class CommentsAdmin(admin.ModelAdmin):
#