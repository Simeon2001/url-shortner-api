import graphene
from graphene_django import DjangoObjectType
from .models import links
import hashlib
import time
from datetime import datetime

class all_url(DjangoObjectType):

    class Meta:
        model = links
        fields = ['url','detail']

class Query (graphene.ObjectType):
    all_links = graphene.List(all_url)
    def resolve_all_links(root,info):
        return links.objects.all()

class UrlMutation (graphene.Mutation):
    class Arguments:
        url = graphene.String(required=True)
        detail = graphene.String(required=False)
    link = graphene.Field(all_url)
    @classmethod
    def mutate(cls,root,info,url,detail):
        sec = str(time.time())
        d = str(datetime.now())
        dd = (d + sec) 
        c = (dd.encode('UTF-8'))
        m = hashlib.sha256(c).hexdigest()
        v = m[0:5]
        link = links(url=url,detail=detail,extension=v)
        link.save()
        return UrlMutation(link=link)

class Mutation (graphene.ObjectType):
    add_urls = UrlMutation.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)