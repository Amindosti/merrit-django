from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Form.models import CreateForm
from .serializers import HomePageSerializers
from django.contrib.auth.models import User
from rest_framework import viewsets


@api_view(['GET', 'POST'])
def data_entry_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = CreateForm.objects.all()
        serializer = HomePageSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HomePageSerializers(data=request.data)
        if serializer.is_valid():
            CreateForm.objects.create(
                author=request.user,
                formarray=request.data,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def data_entry_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = CreateForm.objects.get(pk=pk)
    except CreateForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HomePageSerializers(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HomePageSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = HomePageSerializers
