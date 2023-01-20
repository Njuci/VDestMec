from django.contrib import admin
from .models import Etudiant

# Register your models here.
class tablEtudiant(admin.ModelAdmin):
    list_display=('nom','post_nom','prenom','numMatricule')
admin.site.register(Etudiant,tablEtudiant)  