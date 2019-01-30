from rest_framework import serializers
#from . import Task

# class Task(object):
#     def __init__(self, **kwargs):
#         for field in ('id', 'name', 'owner', 'status'):
#             setattr(self, field, kwargs.get(field, None)) 


# STATUSES = (
#     'New',
#     'Ongoing',
#     'Done',
# )


# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=256)
#     owner = serializers.CharField(max_length=256)
#     status = serializers.ChoiceField(choices=STATUSES, default='New')

#     def create(self, validated_data):
#         return Task(id=None, **validated_data)

#     def update(self, instance, validated_data):
#         for field, value in validated_data.items():
#             setattr(instance, field, value)
#         return instance

# class LangdetectSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=256)
#     class Meta:
#         fields = ('texto')

# class SentenceSplittingSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=900)

# class TokenizergSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=900)

# class PostaggingSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=900)

# class WsdtaggerSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=900)

# class NerSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=900)

# class DatesDetectSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=900)

# class ParserSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=900)

# class DependenciesSerializer(serializers.Serializer):
#     texto = serializers.CharField(max_length=900)