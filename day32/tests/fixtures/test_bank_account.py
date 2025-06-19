import unittest
from mypj.fixtures.bank_account import BankAccount


def setUpModule():
    print("calling setup module")


def tearDownModule():
    print("calling teardown module")


class TestBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("calling setup class")

    def setUp(self) -> None:
        self.bank_account = BankAccount(10)
        print("calling setUp")

    def tearDown(self) -> None:
        self.bank_account = None
        print("calling teardown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("calling teardown class")

    def test_deposit_success(self):
        # bank_account = BankAccount(0)
        # bank_account.deposit(10)
        self.bank_account.deposit(10)

        # self.assertEqual(bank_account.balance, 10)
        self.assertEqual(self.bank_account.balance, 20)

    def test_withdraw_success(self):
        # bank_account = BankAccount(10)
        # bank_account.withdraw(10)
        self.bank_account.withdraw(10)

        # self.assertEqual(bank_account.balance, 0)
        self.assertEqual(self.bank_account.balance, 0)
