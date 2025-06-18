from drf_yasg.openapi import Response
from rest_framework import serializers, status, generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountSerializer





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


class AccountListAPIView(generics.ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

# 단일 계좌 상세조회
class AccountDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        account_id = self.kwargs.get('account_id')
        return get_object_or_404(Account, id=account_id, user=self.request.user)

