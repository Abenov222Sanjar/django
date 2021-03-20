from rest_framework import serializers
from main.models import List, Todo


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('todo', )


class TodoDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
