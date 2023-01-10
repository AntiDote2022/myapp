from django.contrib import admin
from .models import *

admin.site.register(Texts)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('numbers', 'kom_name', 'kom_text')


admin.site.register(Comments, CommentAdmin)




