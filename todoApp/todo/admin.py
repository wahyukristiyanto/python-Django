from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    # to show readonly filed/autofill field
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)