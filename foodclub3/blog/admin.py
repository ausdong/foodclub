from django.contrib import admin
from blog.models import Post, Category, Image

# Register your models here.

class PostAdmin(admin.ModelAdmin):
        # fields display on change list
        list_display = ['name', 'dsc']
        # fields to search in change list
        search_fields = ['name', 'dsc', 'time']
        # enable the date drill down on change list
        date_hierarchy = 'time'
        # enable the save buttons on top on change form
        save_on_top = True

		
class CategoryAdmin(admin.ModelAdmin):
        # fields display on change list
        list_display = ['name', 'dsc']
        # fields to search in change list
        search_fields = ['name', 'dsc', 'time']
        # enable the date drill down on change list
        date_hierarchy = 'time'
        # enable the save buttons on top on change form
        save_on_top = True

		
		
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image)