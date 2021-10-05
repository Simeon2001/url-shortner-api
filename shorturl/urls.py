from graphene_django.views import GraphQLView
from django.urls import path
from shorturl.schema import schema
from . import views

urlpatterns = [
    path('graphql',GraphQLView.as_view(graphiql=True,schema=schema)), 
    path('<str:hash>', views.rework, name = 'linkers/' ),
#    path('hash', views.rework, name = 'linkers/' ),
]