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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from requests.auth import HTTPBasicAuth
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    # page_size_query_param = 'page_size'
    # max_page_size = 50


class OctopusViewSet(APIView):

    pagination_class = LargeResultsSetPagination

    def get(self, request):

        url_nba = 'https://balldontlie.io/api/v1/games/'
        response_nba = requests.get(url_nba)
        data_nba = response_nba.json()


        token = '470e0dd9a6c049aebe3e5dfcea45a989'
        url_premier = 'https://api.football-data.org/v2/competitions/2001/matches'
      
        response = requests.get(url_premier, headers={'X-Auth-Token': '{}'.format(token)})
        
        data_premier = response.json()


        mix_data_set = []
    

        for i in data_nba['data']:
            mix_data_set.append(i)

        mix_data_set.append(data_premier)

        page = request.GET.get('page')



        return Response(mix_data_set)

