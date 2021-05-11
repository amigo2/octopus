from rest_framework import routers
from core import views
from django.urls import path, include
#from core.views import GraphQLOctoView
from django.views.decorators.csrf import csrf_exempt

#from graphene_django.views import Query

from core.schema import schema


# Routers 
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('octopus/', views.OctopusViewSet.as_view(), name='octopus'),
    #path('graphql/', views.GraphQLOctoView.as_view(graphiql=True)),
    #path("graphql/", csrf_exempt(Query.as_view(graphiql=True, schema=schema))),
]