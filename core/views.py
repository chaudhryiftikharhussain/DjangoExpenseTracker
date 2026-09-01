from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Expense, Category
from core.forms import AddCategoryForm, AddExpenseForm


# Create your views here.

@login_required
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context=context)

@login_required
def expenses(request):
    if request.user.is_superuser:
        expenses = Expense.objects.all()
    else:
        expenses = Expense.objects.filter(user=request.user)
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

@login_required
def add_category(request):
    print(request.POST)
    print("add category me a gya ")
    form = AddCategoryForm()
    print(form)
    if request.method == "POST":
        print("post call me aya")
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            print("form is saved")
            return redirect('/categories')
        else:
            print("form is not valid")


    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context=context)

@login_required
def add_expense(request):
    print(request.POST)
    print("add expense me a gya ")
    form = AddExpenseForm(user=request.user)
    print(form)
    if request.method == "POST":
        print("post call me aya")
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            print("form is valid")

            print("POST user:", request.POST.get("user"))
            print("CLEANED user:", form.cleaned_data.get("user"))
            print(
                "CLEANED user ID:",
                form.cleaned_data.get("user").id
                if form.cleaned_data.get("user")
                else None
            )

            expense = form.save()

            print("SAVED user:", expense.user)
            print("SAVED user ID:", expense.user_id)

            return redirect("/expenses")
    else:
        print("form is not valid")


    context = {
        'form': form,
    }
    return render(request, 'add_expense.html', context=context)

@login_required
def edit_expense(request, expense_id):
    print(request.POST)
    print("edit expense me a gya ", expense_id)
    expense_object = Expense.objects.get(id=expense_id)
    form = AddExpenseForm(instance=expense_object)
    print(form)
    if request.method == "POST":
        print("post call me aya")
        form = AddExpenseForm(request.POST, instance=expense_object)
        if form.is_valid():
            print("form is valid")
            form_object = form.save(commit=False)
            print(form_object.user)
            # yahan pe krna
            form_object.user = request.user
            print("user is attached")
            print(form_object.user)
            form_object.save()
            print(form_object.user)
            print("form is saved")
            return redirect('/expenses')
        else:
            print("form is not valid")


    context = {
        'form': form,
    }
    return render(request, 'add_expense.html', context=context)

@login_required
def delete_expense(request, expense_uuid):

    print("delete expense me a gya ", expense_uuid)
    expense_object = Expense.objects.get(uuid=expense_uuid)
    expense_object.delete()
    return redirect('/expenses')
