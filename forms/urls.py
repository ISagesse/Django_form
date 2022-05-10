from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new_contact', views.contact, name='contact'),
    path('new_snippet', views.snippet, name='snippet'),
]