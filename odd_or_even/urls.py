from django.urls import path
from .views import odd_even

urlpatterns = [
    path("<int:num>", odd_even)
]
