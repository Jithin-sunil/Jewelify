from django.urls import path
from Basics import views

urlpatterns = [
    path('Add/',views.add,name="add"),
    path('Calculator/',views.Calculator,name="Calculator"),
    path('Largest/',views.Largest,name="Largest"),
    path('OddorEven/',views.OddorEven,name="OddorEven"),
    
]