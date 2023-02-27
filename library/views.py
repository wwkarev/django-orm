from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins, filters
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from library.models import Author, Category
from library.serializers import AuthorSerializer, CategorySerializer


# @api_view(['POST'])
# def create_author(request):
#     print(request.data)
#     serializer = AuthorSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)


# @api_view(['PUT'])
# def update_author(request, author_id):
#     print(request.data)
#     author = Author.objects.get(pk=author_id)
#     serializer = AuthorSerializer(author, data=request.data, partial=False)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)


# @api_view(['PATCH'])
# def partial_update_author(request, author_id):
#     print(request.data)
#     author = Author.objects.get(pk=author_id)
#     serializer = AuthorSerializer(author, data=request.data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)


class CustomModelView(APIView):
    def post(self, request):
        serializer = self._serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        return self._update(request, pk, False)

    def patch(self, request, pk):
        return self._update(request, pk, True)

    def _update(self, request, pk, partial):
        obj = self._model_cls.objects.get(pk=pk)
        serializer = self._serializer(obj, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        obj = self._model_cls.objects.get(pk=pk)
        obj.delete()
        return Response(status=204)

    def get(self, request, pk=None):
        data = self._model_cls.objects.all()
        many = True
        if pk:
            data = data.get(pk=pk)
            many = False

        return Response(self._serializer(data, many=many).data)



class AuthorApiView(CustomModelView):
    _model_cls = Author
    _serializer = AuthorSerializer

class CategoryApiView(CustomModelView):
    _serializer = CategorySerializer
    _model_cls = Category


class AuthorModelView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name"]