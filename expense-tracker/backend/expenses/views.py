from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer
from django.db.models import Sum
from datetime import datetime, timedelta

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        """Get expense summary statistics"""
        expenses = Expense.objects.all()
        total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        count = expenses.count()
        
        # Get summary by category
        by_category = {}
        for expense in expenses:
            if expense.category not in by_category:
                by_category[expense.category] = 0
            by_category[expense.category] += float(expense.amount)
        
        return Response({
            'total_expenses': float(total),
            'total_count': count,
            'by_category': by_category
        })
    
    @action(detail=False, methods=['get'])
    def today(self, request):
        """Get expenses for today"""
        today = datetime.now().date()
        expenses = Expense.objects.filter(date=today)
        serializer = self.get_serializer(expenses, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def this_month(self, request):
        """Get expenses for this month"""
        today = datetime.now().date()
        first_day = today.replace(day=1)
        expenses = Expense.objects.filter(date__gte=first_day)
        serializer = self.get_serializer(expenses, many=True)
        return Response(serializer.data)
