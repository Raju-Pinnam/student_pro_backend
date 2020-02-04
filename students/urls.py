from django.urls import path

from .views import StudentLCView, StudentUDView

urlpatterns = [
    path('', StudentLCView.as_view()),
    path('<int:pk>/', StudentUDView.as_view())
]
