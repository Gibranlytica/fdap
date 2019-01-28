from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from .serializers import LangdetectSerializer, SentenceSplittingSerializer, TokenizergSerializer, PostaggingSerializer, WsdtaggerSerializer, NerSerializer, DatesDetectSerializer, ParserSerializer, DependenciesSerializer, PostSerializer
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json


class LangdetectViewSet(views.APIView):

    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = LangdetectSerializer(yourdata, many=True).data
        return Response(results)

class SentenceSplittingViewSet(serializers.Serializer):

    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = SentenceSplittingSerializer(yourdata, many=True).data
        return Response(results)

class TokenizerViewSet(serializers.Serializer):

    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = TokenizergSerializer(yourdata, many=True).data
        return Response(results)

class PostaggingViewSet(serializers.Serializer):

    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = PostaggingSerializer(yourdata, many=True).data
        return Response(results)

class WsdtaggerViewSet(serializers.Serializer):
    
    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = WsdtaggerSerializer(yourdata, many=True).data
        return Response(results)

class NerViewSet(viewsets.ModelViewSet):

    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = NerSerializer(yourdata, many=True).data
        return Response(results)

class DatesDetectViewSet(viewsets.ModelViewSet):
    
    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = DatesDetectSerializer(yourdata, many=True).data
        return Response(results)

class ParserViewSet(viewsets.ModelViewSet):
    
    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = ParserSerializer(yourdata, many=True).data
        return Response(results)

class DependenciesViewSet(viewsets.ModelViewSet):
    
    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = DependenciesSerializer(yourdata, many=True).data
        return Response(results)

def index(request):
    nombre = "Israel"
    blog = "https://www.uno-de-piera.com"
    tupla = (1,2,3,4,5,6,7,8,9,10)
    context = {
        'saludo': 'hola que ase', 
        'tupla':tupla,
        'nombre': nombre,
        'blog': blog
    }
    
    # devolvemos los datos a la vista saludo.html para printarlos
    return render(request, 'index.html', context)