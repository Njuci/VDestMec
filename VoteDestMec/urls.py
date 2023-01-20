
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from accounts.urls import rooter as accounts_rooter

root=routers.DefaultRouter()
root.registry.extend(accounts_rooter.registry)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(root.urls))
]
