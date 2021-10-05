from typing_extensions import Required
import graphene
from graphene_django import DjangoObjectType
from .models import links

class all_url(DjangoObjectType):

    class Meta:
        model = links
        fields = ['url','info']

class Query (graphene.ObjectType):
    all_links = graphene.List(all_url)
    def resolve_all_links(root,info):
        return links.objects.all()

class UrlMutation (graphene.Mutation):
    class Arguments:
        url = graphene.String(required=True)
    link = graphene.Field(all_url)

class Mutation (graphene.ObjectType):
    add_urls = UrlMutation.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)