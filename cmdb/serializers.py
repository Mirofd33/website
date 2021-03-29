# -*- coding: utf-8 -*-
from rest_framework import serializers
from cmdb.models import Host, ASSET_STATUS, ASSET_TYPE
from publisher.models import projectToHost, serviceToHost


rexNum = "^[0-9]*$"


class HostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # 定义临时字段，临时存储显示
    env = serializers.SerializerMethodField()
    re_per = serializers.SerializerMethodField()
    update_time = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    asset_type = serializers.SerializerMethodField()
    prjname = serializers.SerializerMethodField()
    srvname = serializers.SerializerMethodField()


    class Meta:
        model = Host
        fields = '__all__'

    def get_env(self, obj):
        return obj.env.env.fullname

    def get_re_per(self, obj):
        return obj.re_per.first_name if obj.re_per else "0"

    def get_update_time(self, obj):
        return obj.update_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_status(self, obj):
        return dict(ASSET_STATUS)[str(obj.status)] if obj.status else "0"

    def get_asset_type(self, obj):
        return dict(ASSET_TYPE)[str(obj.asset_type)] if obj.status else "0"

    def get_prjname(self, obj):
        pn = projectToHost.objects.filter(host=obj.id)
        return pn[0].Project.name if pn.count() > 0 else "0"

    def get_srvname(self, obj):
        pn = serviceToHost.objects.filter(host=obj.id)
        return pn[0].service.name if pn.count() > 0 else "0"

    def __init__(self, *args, **kwargs):
        super(HostSerializer, self).__init__(*args, **kwargs)






