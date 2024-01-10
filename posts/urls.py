from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostInformation.as_view()),
    path('posts/instruments', views.InstrumentChoices.as_view()),
    path('posts/genres', views.GenreChoices.as_view()),
]
