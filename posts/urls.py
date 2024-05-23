from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostInformation.as_view()),
    path('posts/create/instrument/', views.Instruments.as_view()),
    path('posts/create/genre/', views.Genres.as_view()),
]
