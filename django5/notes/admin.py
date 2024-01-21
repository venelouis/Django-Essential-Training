from django.contrib import admin

# Register your models here.
from . import models
class NotesAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title',)

admin.site.register(models.Notes, NotesAdmin)