from django.urls import path

from .views import StateView

urlpatterns = [
    path('states/', StateView.as_view())
]
