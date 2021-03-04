# -*- coding: utf-8 -*-
from rest_framework import serializers
from cmdb.models import Host
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cmdb.models import *
import time
from publisher.models import projectToHost, serviceToHost


rexNum = "^[0-9]*$"


class HostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # 定义临时字段，临时存储显示
    env = serializers.SerializerMethodField()
    re_per = serializers.SerializerMethodField()
    update_time = serializers.SerializerMethodField()

    class Meta:
        model = Host
        fields = '__all__'

    def get_env(self, obj):
        return obj.env.env.fullname

    def get_re_per(self, obj):
        return obj.re_per.first_name if obj.re_per else "0"

    def get_update_time(self, obj):
        return obj.update_time.strftime("%Y-%m-%d %H:%M:%S")

    def __init__(self, *args, **kwargs):
        super(HostSerializer, self).__init__(*args, **kwargs)






