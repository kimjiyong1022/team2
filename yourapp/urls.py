from django.urls import path
from .views import login_view
from . import views


urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]