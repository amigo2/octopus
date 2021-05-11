import json
import requests

from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from requests.auth import HTTPBasicAuth

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OctopusViewSet(APIView):

    def get(self, request):
        #try:
        url_nba = 'https://balldontlie.io/api/v1/games/'
        response_nba = requests.get(url_nba)
        data_nba = response_nba.json()


        token = '470e0dd9a6c049aebe3e5dfcea45a989'
        url_premier = 'https://api.football-data.org/v2/competitions/2001/matches'
      
        response = requests.get(url_premier, headers={'X-Auth-Token': '{}'.format(token)})
        
        data_premier = response.json()
 

        
        #return Response(data_nba)
        return Response(data_premier)

        # except:
        #     res = {"code": 404, "message": "Data not Found!"}
        #     return Response(data=json.dumps(res), status=status.HTTP_404_NOT_FOUND)

