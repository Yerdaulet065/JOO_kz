from django.urls import path
from main import views


urlpatterns = [
    path('', views.MainPage, name='main'),

    path('create', views.CreatePage, name='create'),
    path('update/<int:pk>', views.UpdatePage, name='update'),
    path('delete/<int:pk>', views.DeletePage, name='delete'),
]