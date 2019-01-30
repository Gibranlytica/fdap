from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

class langdetect(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

class sentenceSplitting(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

class tokenizer(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

class postagging(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

class wsdtagger(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

class ner(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

class datesDetect(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

class parser(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

class dependencies(APIView):

    def get(self, request, format=None):
        return Response({"success": True, "content": "Hello World!"})

def index(request):
    context = { }

    return render(request, 'index.html', context)