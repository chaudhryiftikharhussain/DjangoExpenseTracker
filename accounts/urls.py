from django.urls import path
from django.views.generic.base import RedirectView
from accounts import views as accounts_views

urlpatterns = [
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),
]
