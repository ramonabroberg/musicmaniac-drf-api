from django.urls import path
from messaging import views

urlpatterns = [
    path('messages/', views.MessageList.as_view()),
    path('messages/<int:user_id>/', views.MessageConversation.as_view()),
    path('messages/create', views.MessageCreate.as_view()),
]