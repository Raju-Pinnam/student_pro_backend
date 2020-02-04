from rest_framework import generics

from .models import State
from .serializers import StateSerializer


class StateView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
