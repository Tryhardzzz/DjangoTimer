from django.urls import path
from . import views

urlpatterns = [
	path('', views.times_list, name='times_list'),
	path('time/<int:pk>/', views.time_detail, name='time_detail'),
]
