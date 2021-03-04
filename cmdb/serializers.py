# -*- coding: utf-8 -*-
from rest_framework import serializers
from cmdb.models import Host
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cmdb.models import *
from publisher.models import projectToHost, serviceToHost


rexNum = "^[0-9]*$"


class HostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # 定义临时字段，临时存储显示


    class Meta:
        model = Host
        fields = '__all__'







