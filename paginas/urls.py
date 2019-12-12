from django.urls import path
from .views import LoginPageView, HomePageView

urlpatterns = [
    path('', LoginPageView.as_view(), name ='login'),
    path('home/', HomePageView.as_view(), name ='home'),
]