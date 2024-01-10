from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostInformation.as_view()),
    path('posts/create/instrument/', views.InstrumentChoice.as_view()),
    path('posts/create/genre/', views.GenreChoice.as_view()),
]
