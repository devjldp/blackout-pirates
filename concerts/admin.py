from django.contrib import admin

from .models import Concert

# Register your models here.

class ConcertAdmin(admin.ModelAdmin):
  list_display = ('city', 'date')
  ordering = ['date'] # Ordereing Ascendent
  # ordering = ['-date'] # Ordering descendent

# Register your models here.
admin.site.register(Concert, ConcertAdmin)