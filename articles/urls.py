from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/comments/comment_create/', views.comment_create, name='comment_create'),
    path('<int:id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]