from rest_framework import serializers
#from . import Task

class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner', 'status'):
            setattr(self, field, kwargs.get(field, None)) 


STATUSES = (
    'New',
    'Ongoing',
    'Done',
)


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)
    status = serializers.ChoiceField(choices=STATUSES, default='New')

    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
# class LangdetectSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()

# class SentenceSplittingSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()

# class TokenizergSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()

# class PostaggingSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()

# class WsdtaggerSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()

# class NerSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()

# class DatesDetectSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()

# class ParserSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()

# class DependenciesSerializer(serializers.Serializer):
#     comments = serializers.IntegerField()
#     likes = serializers.IntegerField()