from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'content', 'cat')

class WomanDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Women
        fields = '__all__'