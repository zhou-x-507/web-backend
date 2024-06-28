import uuid

from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework.viewsets import GenericViewSet
from django.db import transaction
from django.db.models import Q

from ..models import User
from .serializers import UserSerializer


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset()

    @action(detail=False, methods=['POST']) 
    def add_user(self, request, pk=None):
        name = request.data.get("name")
        _uid = str(uuid.uuid4())
        with transaction.atomic():
            user = User.objects.create(uuid=_uid, name=name)

        return Response(data={"uuid": user.uuid if user else None})

    @action(detail=False, methods=['GET']) 
    def get_user_list(self, request, pk=None):
        queryset = self.get_queryset()
        print(":::::", queryset)
        serializer_data = UserSerializer(queryset, many=True).data
        
        return Response(data=serializer_data)

