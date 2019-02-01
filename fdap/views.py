from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets, status
from . import serializers
from .freeling.postagger import Postagger

class langdetect(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.textoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class sentenceSplitting(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.textoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class tokenizer(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.textoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class postagging(APIView):
    serializer_class = serializers.textoSerializer

    def post(self, request, *args, **kwargs):
        analize = Postagger(request.data)
        k = analize.principal()
        serializer = serializers.textoSerializer(data=k)
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
