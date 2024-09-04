from rest_framework import serializers
from test_project.users.models import User
from django.contrib.auth import get_user_model




class UserSerializers(serializers.ModelSerializer):
    class meta:
        model = get_user_model(
        fields = "__all__"
        )


        