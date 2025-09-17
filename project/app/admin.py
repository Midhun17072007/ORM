from django.contrib import admin 
from .models import Movies
admin.site.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display=('M_ID', 'M_name', 'Release_date', 'Director','Actors') 