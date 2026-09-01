from django import forms
from django.contrib.auth.models import User
from django.template.context_processors import request

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

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        print("constructor called ")
        print("FORM USER:", user)
        print("IS SUPERUSER:", user.is_superuser if user else "NO USER")

        if user and user.is_superuser:

            print("super user received")
            self.fields["user"] = forms.ModelChoiceField(
                queryset=User.objects.all(),
                required=True,
                label="User",
                widget=forms.Select(attrs={
                    "class": "form-select",
                })
            )

    def save(self, commit=True):
        expense = super().save(commit=False)

        print("save called")

        if self.current_user and self.current_user.is_superuser:
            print("super user received from form")
            expense.user = self.cleaned_data["user"]
        else:
            print("user set from the login")
            expense.user = self.current_user

        if commit:
            expense.save()

        return expense