from django.urls import path
from messages import views

urlpatterns = [
    path('messages/', views.MessageList.as_view()),
    path('messages/<int:user_id>/', views.MessageConversation.as_view()),
]