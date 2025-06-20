from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UserSignupAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

