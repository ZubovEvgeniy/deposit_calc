from rest_framework.decorators import api_view  # Импортировали декоратор
from rest_framework.response import Response
import status

from .serializers import DepositSerializer


@api_view(['POST'])
def calculate(request):
    serializer = DepositSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
