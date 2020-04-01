from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('app/', views.application, name="application"),
    path('add/', views.add, name="add"),
    path('delete/<int:id>', views.delete,name="delete"),
    path('update/<int:id>', views.update, name="update"),
]