from rest_framework import serializers

class LangdetectSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()

class SentenceSplittingSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()

class TokenizergSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()

class PostaggingSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()

class WsdtaggerSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()

class NerSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()

class DatesDetectSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()

class ParserSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()

class DependenciesSerializer(serializers.Serializer):
    comments = serializers.IntegerField()
    likes = serializers.IntegerField()