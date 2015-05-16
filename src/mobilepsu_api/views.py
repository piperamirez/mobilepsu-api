from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mobilepsu_api.models import Field
from mobilepsu_api.serializers import FieldSerializer

@api_view(['GET', 'POST'])
def field_list(request):
    """
    List all fields, or create a new one.
    """
    if request.method == 'GET':
        fields = Field.objects.all()
        serializer = FieldSerializer(fields, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FieldSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def field_detail(request, pk):
    """
    Retrieve, update or delete a field instance
    """
    try:
        field = Field.objects.get(pk=pk)
    except Field.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FieldSerializer(field)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FieldSerializer(field, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        field.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)