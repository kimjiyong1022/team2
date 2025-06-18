from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Account, Transaction
from decimal import Decimal

User = get_user_model()

class AccountModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.account = Account.objects.create(
            user=self.user,
            account_number='1234567890123456',
            balance=Decimal('100000.00'),
            bank_code='KAKAO',
            type='CHECKING'
        )

    def test_account_creation(self):
        self.assertEqual(self.account.user, self.user)
        self.assertEqual(self.account.account_number, '1234567890123456')
        self.assertEqual(self.account.balance, Decimal('100000.00'))
        self.assertEqual(self.account.bank_code, 'KAKAO')
        self.assertEqual(self.account.type, 'CHECKING')

    def test_account_str(self):
        expected_str = f"{self.account.account_number} - {self.user.name if hasattr(self.user, 'name') else self.user.username}"
        self.assertEqual(str(self.account), expected_str)


class TransactionModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.account = Account.objects.create(
            user=self.user,
            account_number='9876543210987654',
            balance=Decimal('50000.00'),
            bank_code='NH',
            type='MINUS'
        )
        self.transaction = Transaction.objects.create(
            account=self.account,
            transaction_type='deposit',
            transaction_method='cash_deposit',
            amount=Decimal('10000.00'),
            balance=Decimal('60000.00'),
            description='현금 입금 테스트'
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.account, self.account)
        self.assertEqual(self.transaction.transaction_type, 'deposit')
        self.assertEqual(self.transaction.transaction_method, 'cash_deposit')
        self.assertEqual(self.transaction.amount, Decimal('10000.00'))
        self.assertEqual(self.transaction.balance, Decimal('60000.00'))
        self.assertEqual(self.transaction.description, '현금 입금 테스트')

    def test_transaction_str(self):
        expected_str = f"{self.account.account_number} - deposit - 10000.00"
        self.assertEqual(str(self.transaction), expected_str)
