from django.urls import path
from core import views as core_views

urlpatterns = [
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('expenses/', core_views.expenses, name='expenses'),
    path('categories', core_views.categories, name='categories'),
]
