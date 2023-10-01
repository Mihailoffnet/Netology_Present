from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from demo.models import Comment
from demo.serializers import CommentSerializer


# class CommentViewSet(ViewSet):
#     def list(self, request): # list - вывести все объекты
#         return Response({'status': 'ok'})
#     def retrivie(self, request): # retrivie - вывести конкретный объект
#         return Response({'status': 'ok'})
#     def destroy(self, request): # destroy - удалить конкретный объект
#         return Response({'status': 'ok'})
#     def update(self, request): # update - обновить конкретный объект
#         return Response({'status': 'ok'})
#     def create(self, request): # create - обновить конкретный объект
#         return Response({'status': 'ok'})


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user',] # DjangoFilterBackend
    search_fields = ['text',] # SearchFilter ?search= или переназначить в сеттингс 'SEARCH_PARAM': 'q',
    ordering_fields = ['id', 'user', 'text', 'created_at'] # OrderingFilter ?ordering= или переназначить в сеттингс 'ORDERING_PARAM': 'o',
    pagination_class = LimitOffsetPagination #?limit=(сколько показать)&offset=(сколько пропустить)



