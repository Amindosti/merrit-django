from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DataEntry
from .serializers import DataEntrySerializers
from django.contrib.auth.models import User
from rest_framework import viewsets


@api_view(['GET', 'POST'])
def data_entry_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = DataEntry.objects.all()
        serializer = DataEntrySerializers(snippets, many=True)
        return Response(serializer.data)


def data_entry_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = DataEntry.objects.get(pk=pk)
    except DataEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DataEntrySerializers(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DataEntrySerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = DataEntrySerializers
