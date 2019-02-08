from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets, status
from .freeling.postagger import Postagger
from .freeling.langdetect import LangDetect
from .freeling.tokenizer import Tokenizer
from .freeling.sentencespliting import SentenceSpliting
from . import serializers
import json

## ----------------------------------------------
## ------    Clase que detecta el Idioma   ------
## ----------------------------------------------
class langdetect(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        analize = LangDetect(request.data['texto'])
        k = analize.inicio()
        ts= [("texto", k)]
        landet = dict(ts)
        serializer = serializers.textoSerializer(data=landet)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## ----------------------------------------------
## ---   Clase que desarrolla el tokenizado   ---
## ----------------------------------------------
class tokenizer(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        analize = Tokenizer(request.data['texto'])
        k = analize.inicio()
        ts= [("texto", k)]
        token = dict(ts)
        serializer = serializers.textoSerializer(data=token)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## ----------------------------------------------
## - Clase que desarrolla el Split de oraciones -
## ----------------------------------------------
class sentenceSplitting(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        analize = SentenceSpliting(request.data['texto'])
        k = analize.inicio()
        ts= [("texto", k)]
        senspl = dict(ts)

        serializer = serializers.textoSerializer(data=senspl)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## ----------------------------------------------
## ----  Clase que desarrolla el Postagging  ----
## ----------------------------------------------
class postagging(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        h = request.data['texto']
        dataform = str(h).strip("'<>() ").replace('\'', '\"')
        j = json.loads(dataform)
        analize = Postagger(j)
        k = analize.inicio()
        ts= [("texto", k)]
        postag = dict(ts)
        
        serializer = serializers.textoSerializer(data=postag)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class wsdtagger(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.textoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ner(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.textoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class datesDetect(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.textoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class parser(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.textoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class dependencies(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.textoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    context = { }

    return render(request, 'index.html', context)
