from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]