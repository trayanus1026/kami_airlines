# airlines/views.py

from pstats import Stats
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Testplane
from .serializers import TestplaneSerializer

class AirplaneListCreateView(generics.ListCreateAPIView):
    queryset = Testplane.objects.all()
    serializer_class = TestplaneSerializer
    
    def post(self, request, *args, **kwargs):
        # Check if there are fewer than 10 airplanes
        if Testplane.objects.count() >= 10:
            return Response({"error": "Cannot add more than 10 airplanes."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)