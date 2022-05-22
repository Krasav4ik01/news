from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Poets)
admin.site.register(Writers)
admin.site.register(Heroes)
admin.site.register(Labours)

class NewsCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(News, NewsCategory)
admin.site.register(Post)

  



