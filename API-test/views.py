from django.shortcuts import render

# Create your views here.
from .permissions import  IsSuperUserOrStaffReadOnly
from .serializers import UserSerializers
from test_project.users.models import User
from rest_framework.viewsets import ModelViewSet





class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly)