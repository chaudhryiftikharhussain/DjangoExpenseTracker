from django import forms
from core.models import Category, Expense


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category name',
            }),
        }

class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["category", "amount", "description", "date"]

        widgets = {
            "category": forms.Select(attrs={
                "class": "form-select",
                "placeholder": "Select category",
            }),

            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter amount",
                "step": "0.01",
                "min": "0",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter expense description",
                "rows": 3,
            }),

            "date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "Select date",
            }),
        }