from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from library.models import Author, Book
from library.serializers import AuthorSerializer


class AuthorModelView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name"]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ["first_name"]



