from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='items'),
  path('items-list/', views.ItemsList.as_view(), name='items-list'),
]