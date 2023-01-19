from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from mainApp import serializers, models, controller, exceptions

# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        self.serializer_class = serializers.CreateAccountSerializer
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        return Response("Method Not Allowed", status=405)

    def retrieve(self, request, pk=None):
        return Response("Method Not Allowed", status=405)

    def update(self, request, pk=None):
        return Response("Method Not Allowed", status=405)

    def partial_update(self, request, pk=None):
        return Response("Method Not Allowed", status=405)

    @action(detail=False, methods=['get'])
    def me(self, request):
        try:
            account = models.Account.objects.get(user__id=request.user.id)
        except:
            return Response(status=404)
        return Response(data=serializers.AccountSerializer(account).data, status=200)

    @action(detail=False, methods=['post'])
    def save_password(self, request):
        try:
            account = models.Account.objects.get(user__id=request.user.id)
        except:
            return Response(data="you need a token for this endpoint", status=401)
        try:
            password_obj = controller.save_password(account, request)
        except exceptions.MaxSizeException as e:
            return Response({'message': e.message}, status=400)
        except exceptions.NoPasswordException as e:
            return Response({'message': e.message}, status=400)
        except exceptions.NoSiteException as e:
            return Response({'message': e.message}, status=400)
        return Response(serializers.PasswordSerializer(password_obj).data, status=200)

    @action(detail=False, methods=['get'])
    def passwords(self, request):
        try:
            account = models.Account.objects.get(user__id=request.user.id)
        except:
            return Response(data="you need a token for this endpoint", status=401)
        return Response(serializers.PasswordSerializer(controller.get_all_passwords(account), many=True).data, status=200)
