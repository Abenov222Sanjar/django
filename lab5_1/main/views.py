from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import List, Todo
from main.serializers import ListSerializer, TodoSerializer, TodoDetailedSerializer


class ListViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = List.objects.all()
        serializer = ListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id):
        queryset = List.objects.get(id=id)
        serializer = ListSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        queryset = List.objects.create(
            name=self.request.data.get('name')
        )
        serializer = ListSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, id):
        queryset = List.objects.get(id=id)
        queryset.name = self.request.data.get('name')
        queryset.save()
        serializer = ListSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, id):
        List.objects.get(id=id).delete()
        queryset = List.objects.all()
        serializer = ListSerializer(queryset)
        return Response(serializer.data)


class TodoViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list_unmarked(self, request, id):
        queryset = Todo.objects.filter(list_id=id, mark=False)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def list_marked(self, request, id):
        queryset = Todo.objects.filter(list_id=id, mark=True)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id, id2):
        queryset = Todo.objects.get(id=id2, list_id=id)
        serializer = TodoDetailedSerializer(queryset)
        return Response(serializer.data)

    def create(self, request, id):
        queryset = Todo.objects.create(
            list=List.objects.get(id=id),
            todo=self.request.data.get('todo'),
            created=self.request.data.get('created'),
            due_on=self.request.data.get('due_on'),
            owner=self.request.data.get('owner'),
            mark=False
        )
        serializer = TodoDetailedSerializer(queryset)
        return Response(serializer.data)

    def update(self,request,id, id2):
        queryset = Todo.objects.get(id=id2, list_id=id)
        queryset.list = List.objects.get(id=self.request.data.get('list'))
        queryset.todo = self.request.data.get('todo')
        queryset.created = self.request.data.get('created')
        queryset.due_on = self.request.data.get('due_on')
        queryset.owner = self.request.data.get('owner')
        queryset.mark = self.request.data.get('mark')
        queryset.save()
        serializer = TodoDetailedSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, id, id2):
        queryset = Todo.objects.get(id=id2, list_id=id)
        queryset.delete()
        serializer = TodoDetailedSerializer(queryset)
        return Response(serializer.data)
