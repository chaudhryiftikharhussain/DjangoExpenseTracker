from django.shortcuts import render

from core.models import Expense, Category


# Create your views here.

def expenses(request):
    expenses = Expense.objects.all()
    context = {
        'expenses': expenses,
    }
    return render(request, 'expenses.html', context=context)


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context=context)