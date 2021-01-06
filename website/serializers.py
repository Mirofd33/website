# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User

rexNum = "^[0-9]*$"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = User
        fields = ('password','username','is_superuser','email')
    