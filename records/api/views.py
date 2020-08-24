from rest_framework import generics, status, viewsets, filters

from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from records.api.permissions import IsAuthorOrReadOnly, IsAuthorOrReject
from records.api.serializers import (TaskSerializer,
                                    ChoiceSerializer,
                                    IncomeSerializer,
                                    ExpenditureSerializer,
                                    CategorySerializer)
from records.models import Task, Choice, Income, Expenditure, Category

from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    # max_page_size = 100


class ChoiceViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Choice."""
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReject]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Choice.objects.filter(author=user)


class TaskViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Task."""
    lookup_field = "slug"
    serializer_class = TaskSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated, IsAuthorOrReject]
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('created_at', )
    search_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user).order_by("-created_at")



class IncomeViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Income."""
    lookup_field = "slug"
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReject]
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('created_at', )
    search_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)    

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(author=user).order_by("-created_at")


class ExpenditureViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Expenditure."""
    lookup_field = "slug"
    serializer_class = ExpenditureSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReject]
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('created_at', )
    search_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

    def get_queryset(self):
        user = self.request.user
        return Expenditure.objects.filter(author=user).order_by("-created_at")


class CategoryViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Income."""
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReject]
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('title', )
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)    

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(author=user).order_by("title")