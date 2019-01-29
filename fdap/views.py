# from django.shortcuts import render
# from django.http import Http404
# from rest_framework import viewsets
# from .serializers import LangdetectSerializer, SentenceSplittingSerializer, TokenizergSerializer, PostaggingSerializer, WsdtaggerSerializer, NerSerializer, DatesDetectSerializer, ParserSerializer, DependenciesSerializer, PostSerializer
# from django.http import JsonResponse
# from django.core import serializers
# from django.conf import settings
# import json

from rest_framework.response import Response
from rest_framework import viewsets, status

from . import serializers
#from . import Task

class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner', 'status'):
            setattr(self, field, kwargs.get(field, None)) 

# Global variable used for the sake of simplicity.
# In real life, you'll be using your own interface to a data store
# of some sort, being caching, NoSQL, LDAP, external API or anything else
tasks = {
    1: Task(id=1, name='Demo', owner='xordoquy', status='Done'),
    2: Task(id=2, name='Model less demo', owner='xordoquy', status='Ongoing'),
    3: Task(id=3, name='Sleep more', owner='xordoquy', status='New'),
}

def get_next_task_id():
    return max(tasks) + 1


class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.TaskSerializer

    def list(self, request):
        serializer = serializers.TaskSerializer(
            instance=tasks.values(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.id = get_next_task_id()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(instance=task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(
            data=request.data, instance=task)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(
            data=request.data,
            instance=task,
            partial=True)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        del tasks[task.id]
        return Response(status=status.HTTP_204_NO_CONTENT)

# class LangdetectViewSet(views.APIView):

#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = LangdetectSerializer(yourdata, many=True).data
#         return Response(results)

# class SentenceSplittingViewSet(serializers.Serializer):

#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = SentenceSplittingSerializer(yourdata, many=True).data
#         return Response(results)

# class TokenizerViewSet(serializers.Serializer):

#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = TokenizergSerializer(yourdata, many=True).data
#         return Response(results)

# class PostaggingViewSet(serializers.Serializer):

#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = PostaggingSerializer(yourdata, many=True).data
#         return Response(results)

# class WsdtaggerViewSet(serializers.Serializer):
    
#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = WsdtaggerSerializer(yourdata, many=True).data
#         return Response(results)

# class NerViewSet(viewsets.ModelViewSet):

#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = NerSerializer(yourdata, many=True).data
#         return Response(results)

# class DatesDetectViewSet(viewsets.ModelViewSet):
    
#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = DatesDetectSerializer(yourdata, many=True).data
#         return Response(results)

# class ParserViewSet(viewsets.ModelViewSet):
    
#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = ParserSerializer(yourdata, many=True).data
#         return Response(results)

# class DependenciesViewSet(viewsets.ModelViewSet):
    
#     def get(self, request):
#         yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
#         results = DependenciesSerializer(yourdata, many=True).data
#         return Response(results)

# def index(request):
#     nombre = "Israel"
#     blog = "https://www.uno-de-piera.com"
#     tupla = (1,2,3,4,5,6,7,8,9,10)
#     context = {
#         'saludo': 'hola que ase', 
#         'tupla':tupla,
#         'nombre': nombre,
#         'blog': blog
#     }
    
#     # devolvemos los datos a la vista saludo.html para printarlos
#     return render(request, 'index.html', context)