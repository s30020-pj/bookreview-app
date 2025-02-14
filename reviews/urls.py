from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

app_name = 'reviews'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add_book/', views.add_book_form, name='add_book_form'),
    path('add_book_submit/', views.add_book_submit, name='add_book_submit'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/review/', views.add_review, name='add_review'),
]