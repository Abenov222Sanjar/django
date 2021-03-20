from django.urls import path
from rest_framework.routers import SimpleRouter

from main import views

urlpatterns = [
    path('', views.ListViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:id>/', views.ListViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'})),
    path('<int:id>/todos/completed/', views.TodoViewSet.as_view({'get': 'list_marked'})),
    path('<int:id>/todos/', views.TodoViewSet.as_view({'get': 'list_unmarked', 'post': 'create'})),
    path('<int:id>/todos/<int:id2>/', views.TodoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}))
]