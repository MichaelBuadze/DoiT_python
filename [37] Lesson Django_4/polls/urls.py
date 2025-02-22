from django.urls import path, include
from . import views


urlpatterns = [
    path('index', views.index, name="index"),
    path('<int:question_id>', views.detail, name="detail"),
  

]

# 127.0.0.1:8000/polls/