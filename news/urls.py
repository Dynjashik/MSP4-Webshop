from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_news, name='news'),
    path('add/', views.add_news_item, name='add_news'),
    path('edit/<int:news_id>/', views.edit_news_item, name='edit_news_item'),
    path('delete/<int:news_id>/', views.delete_news_item, name='delete_news_item')
]
