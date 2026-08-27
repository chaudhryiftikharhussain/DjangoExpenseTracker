from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Expense, Category


# Create your views here.

@login_required
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context=context)

@login_required
def expenses(request):
    expenses = Expense.objects.all()
    context = {
        'expenses': expenses,
    }
    return render(request, 'expenses.html', context=context)


@login_required
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context=context)