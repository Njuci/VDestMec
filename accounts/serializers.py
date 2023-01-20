from rest_framework import serializers
from .models import Etudiant

class utilisateurLogue(serializers.ModelSerializer):
    class Meta:
        model=Etudiant
        fields=(
        "id",
        "nom",
        "post_nom",
        "prenom",
        "sexe",
        "numMatricule",
        "actif",
        "admin",
             )
        