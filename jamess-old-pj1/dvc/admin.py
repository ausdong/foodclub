from django.contrib import admin
from dvc.models import Fighter, Warcategory, Prompt, Battle, Face

# Register your models here.

admin.site.register(Fighter)
admin.site.register(Warcategory)
admin.site.register(Prompt)
admin.site.register(Battle)
admin.site.register(Face)