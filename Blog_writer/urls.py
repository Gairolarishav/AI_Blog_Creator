from django.urls import path,include
from Blog_writer import views

urlpatterns = [
    path('', views.home ,name='home'),
]