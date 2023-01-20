from  rest_framework import routers
from.views import MonUtilisateur
rooter=routers.DefaultRouter()
rooter.register('UtilisateurLog', MonUtilisateur, basename='UtilisateurLog')