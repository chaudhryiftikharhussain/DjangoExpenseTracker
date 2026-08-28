from django.urls import path
from django.views.generic.base import RedirectView
from core import views as core_views


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='dashboard')),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('expenses/', core_views.expenses, name='expenses'),
    path('categories', core_views.categories, name='categories'),

    path('add-category/', core_views.add_category, name='add_category'),

    # Expenses CRUD
    path('add-expense/', core_views.add_expense, name='add_expense'),
    path('edit-expense/<int:expense_id>', core_views.edit_expense, name='edit_expense'),
    path('delete-expense/<uuid:expense_uuid>', core_views.delete_expense, name='delete_expense'),

]
