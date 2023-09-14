from django.contrib import admin
from .models import Projet
from .forms import ProjetForm

class ProjetAdmin(admin.ModelAdmin):
    form = ProjetForm

admin.site.register(Projet, ProjetAdmin)
