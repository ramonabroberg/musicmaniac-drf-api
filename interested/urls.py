from django.urls import path
from interested import views

urlpatterns = [
    path('interested/', views.InterestedList.as_view()),
    path('interested/<int:pk>/', views.InterestedInformation.as_view()),
]
