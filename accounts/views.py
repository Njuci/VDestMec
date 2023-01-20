from .models import Etudiant
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import utilisateurLogue
from rest_framework.permissions import IsAuthenticated

class MonUtilisateur(viewsets.ViewSet):
    
    permission_classes=(IsAuthenticated,)
    
    
    def list(self,request):
        utilisloge=Etudiant.objects.get(numMatricule=request.user)
        user_data=utilisateurLogue(utilisloge).data
        return Response(user_data)
        
        