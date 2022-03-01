from django.contrib import admin
from django.forms import models
from . import models
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display=('title',)

admin.site.register(models.notes,NotesAdmin)
