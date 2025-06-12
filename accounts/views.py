from drf_yasg.openapi import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts import serializers
from accounts.models import Account


class AccountCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = serializers.AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDeleteAPIView(APIView):
    def delete(self, request, account_id):
        account = Account.objects.get(id=account_id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


