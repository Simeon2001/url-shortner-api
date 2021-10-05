from graphene_django.views import GraphQLView
from django.urls import path
from shorturl.schema import schema

urlpatterns = [
    path('graphql',GraphQLView.as_view(graphiql=True,schema=schema)), 
]