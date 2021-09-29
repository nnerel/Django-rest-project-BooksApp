from rest_framework import generics, permissions
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response

from books.models import Book
from .serializers import BookSerializer


class BookPermission(permissions.BasePermission):

    message = "you do not have permissions"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.added_by == request.user


class BookList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.books.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView, BookPermission):
    permission_classes = [BookPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
