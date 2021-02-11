# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cmdb.models import *
from publisher.models import projectToHost,serviceToHost

rexNum = "^[0-9]*$"


class HostSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #定义临时字段，临时存储显示
    temp = serializers.SerializerMethodField()
    prj_name = serializers.SerializerMethodField()
    sv_name = serializers.SerializerMethodField()
    fzr = serializers.SerializerMethodField()
    class Meta:
        model = Host
        fields = '__all__'
    
    def get_temp(self,obj):
        return obj.env.env.id
    
    def get_prj_name(self,obj):
        pn = projectToHost.objects.filter(host=obj.id)
        return pn[0].Project.name if pn.count() > 0 else "0"
    
    def get_sv_name(self,obj):
        pn = serviceToHost.objects.filter(host=obj.id)
        return pn[0].service.name if pn.count() > 0 else "0"
    
    def get_fzr(self,obj):
        return obj.re_per.username if obj.re_per else "0"
    
    def __init__(self,*args,**kwargs):
        super(HostSerializer,self).__init__(*args,**kwargs)
        

class hostQueryFormSerializer(serializers.Serializer): 
    #bootstrap-table全家桶    
    page = serializers.CharField(max_length=100)
    offset = serializers.CharField(max_length=100)
    order = serializers.CharField(max_length=100)
    #自定义查询条件字段
    vlan_type = serializers.CharField(max_length=100)
    project_type = serializers.CharField(max_length=100)
    #group_type = serializers.CharField(max_length=100)
    status_type = serializers.CharField(max_length=100)
    asset_search = serializers.CharField(max_length=100)
    start_time = serializers.CharField(max_length=100)
    end_time = serializers.CharField(max_length=100)
     
    def __init__(self,*args,**kwargs):
        super(hostQueryFormSerializer,self).__init__(*args,**kwargs)


     
     

        
    