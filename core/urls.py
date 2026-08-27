from django.urls import path
from django.views.generic.base import RedirectView
from core import views as core_views


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='dashboard')),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('expenses/', core_views.expenses, name='expenses'),
    path('categories', core_views.categories, name='categories'),
]
