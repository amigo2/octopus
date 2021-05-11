import json
import requests
import graphene
from graphene_django import DjangoObjectType
from rest_framework.response import Response
from graphene import ObjectType, String, Schema


from .views import OctopusViewSet


class Query(graphene.ObjectType):
    nba = graphene.String()
    premier = graphene.String()
    
    def resolve_nba(self, info):
        url_nba = 'https://balldontlie.io/api/v1/games/'
    
        response_nba = requests.get(url_nba)
        data_nba = response_nba.json()
        json_data_nba = json.dumps(data_nba)
        return {
            'statusCode': 200,
            'nba':  json.loads(json_data_nba)
        }

    def resolve_premier(self, info):
        
        token = '470e0dd9a6c049aebe3e5dfcea45a989'
        url_premier = 'https://api.football-data.org/v2/competitions/2001/matches'

        response = requests.get(url_premier, headers={'X-Auth-Token': '{}'.format(token)})
        data_premier = response.json()
        json_data_premier = json.dumps(data_premier)
        return {
            'statusCode': 200,
            'premier':  json.loads(json_data_premier)
        }




schema = graphene.Schema(query=Query)

