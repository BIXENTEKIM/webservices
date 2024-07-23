from . import views
from django.urls import path

urlpatterns = [
    path('',views.StudentsList.as_view()),
    path('students/<int:pk>',views.StudentByID.as_view()),
]