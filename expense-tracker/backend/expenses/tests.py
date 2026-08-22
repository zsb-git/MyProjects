from django.test import TestCase
from .models import Expense
from datetime import date

class ExpenseModelTest(TestCase):
    def setUp(self):
        Expense.objects.create(
            description="Test Expense",
            amount=50.00,
            category="food",
            date=date.today()
        )
    
    def test_expense_creation(self):
        expense = Expense.objects.get(description="Test Expense")
        self.assertEqual(expense.amount, 50.00)
        self.assertEqual(expense.category, "food")
