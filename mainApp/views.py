from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from mainApp import serializers, models

# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        self.serializer_class = serializers.CreateAccountSerializer
        return super().create(request, *args, **kwargs)
