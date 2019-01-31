from rest_framework import serializers

class textoSerializer(serializers.Serializer):
    texto = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        self.parse_text(validated_data)
        return super().create(validated_data)
   
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance