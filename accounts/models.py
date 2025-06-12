from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# ✅ Account 모델
class Account(models.Model):
    BANK_CODE = [
        ("KAKAO", "카카오뱅크"),
        ("NH", "농협은행"),
        ("IBK", "IBK 기업은행"),
        ("KB", "<국민은행>"),
    ]
    ACCOUNT_TYPE = [
        ("CHECKING", "입출금통장"),
        ("MINUS", "마이너스 통장"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    bank_code = models.CharField(choices=BANK_CODE, max_length=10)
    type = models.CharField(choices=ACCOUNT_TYPE, max_length=10)

    def __str__(self):
        return f"{self.account_number} - {self.user.name}"


# ✅ Transaction 모델
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    TRANSACTION_TYPE = [
        ('deposit', '입금'),
        ('withdrawal', '출금'),
    ]
    TRANSACTION_METHOD = [
        ('card', "카드 결제"),
        ('automatic_transfer', "자동이체"),
        ("cash_deposit", "현금 입금"),
        ("cash_withdrawal", "현금 출금"),
        ("account_deposit", "계좌 입금"),
        ("account_withdrawal", "계좌 출금"),
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    transaction_method = models.CharField(max_length=20, choices=TRANSACTION_METHOD)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account.account_number} - {self.transaction_type} - {self.amount}"
