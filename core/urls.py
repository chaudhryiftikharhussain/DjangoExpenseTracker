from django.urls import path
from core import views as core_views

urlpatterns = [
    path('expenses/', core_views.expenses, name='expenses'),
    path('categories', core_views.categories, name='categories'),
]
