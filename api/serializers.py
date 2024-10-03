from rest_framework import serializers
from .models import ImageModel

class ContactFormSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()
class AchivitaContactFormSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    business_type = serializers.CharField()




class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id', 'title', 'image']
