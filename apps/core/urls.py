from django.urls import path, include
from .views import home

from rest_framework import routers
from apps.core import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) # rota para acessar os usuarios
router.register(r'groups', views.GroupViewSet) # rota para acesar os grupo

urlpatterns = [
    path('', home, name='home'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]



