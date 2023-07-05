from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from REST_AP

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()



urlpatterns =[
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('Auth/', include('rest_framework.urls')),
    path('prediction/', Framework_View.as_view(), name ='Prediction'),
]
