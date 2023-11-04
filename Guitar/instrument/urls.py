
from django.urls import path,include 
from .views import GuitarListView

urlpatterns = [
    path('guitarlist/', GuitarListView.as_view()),
    
]
