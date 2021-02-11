# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from cmdb.models import *
from utils import env_dispatch
from cmdb.serializers import HostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from publisher.models import projectToHost,serviceType


# Create your views here.


def constructQueryDic(data):
    conditions = {}
    
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    if start_time or end_time:
        if len(start_time)>0 and len(end_time)>0:
            conditions['create_time__range'] = (start_time,end_time)
        if len(start_time)>0 and len(end_time) == 0:
            conditions['create_time__gte'] = start_time
        if len(start_time) == 0 and len(end_time) > 0:    
            conditions['create_time__lte'] = end_time
    
    vlan_type = data.get('vlan_type')
    if vlan_type:
        if len(vlan_type)>0 and vlan_type != '0':
            conditions['env_id__in'] = IpSource.objects.filter(env__in = vlan_type)
        
    project_type = data.get('project_type')
    if project_type:
        if len(project_type)>0 and project_type != '0':
            conditions['id'] = projectToHost.objects.get(Project_id=project_type).host
        
    status_type = data.get('status_type')
    if status_type:
        if len(status_type)>0 and status_type != '0':
            conditions['status'] = status_type
        
    asset_search = data.get('asset_search')
    if asset_search:
        if len(asset_search)>0 and asset_search != '0':
            conditions['asset_type'] = asset_search
        
    return conditions

def searchQueryDic(data):
    conditions = {
        "hostname__contains": data,
        "ip__contains": data,
        "mac__contains":data,
        "ilo_ip__contains":data,
        "asset_no__contains":data,
        "escode__contains":data,
        "sn__contains":data
    }
    return conditions

class HostViewSet(viewsets.ModelViewSet):    
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    
    def list(self, request, *args, **kwargs):   
        if request.method == "GET":
            #bootstrap-table全家桶
            search = request.GET.get('search')
            sort = request.GET.get('sort')  
            limit = request.GET.get('page') if request.GET.get('page') else 10
            offset = request.GET.get('offset') if request.GET.get('offset') else 0
            order = request.GET.get('order')
            #固定搜索条件对象处理集合
            conditions = constructQueryDic(request.GET)
            q = Q()
            for j in conditions:
                q.add(Q(**{j: conditions[j]}),Q.AND)
            #动态搜索条件对象处理集合
            if search:
                search_conditions = searchQueryDic(search)
                for i in search_conditions:
                    q.add(Q(**{i: search_conditions[i]}), Q.OR)
            all_records = Host.objects.filter(q)
            # 排序
            if sort:  
                if sort in ['hostname','ip','cpu_num','re_per']:  
                    if order == 'desc':  
                        sort = '-%s' % (sort)
                    all_records = all_records.order_by(sort)
            else:
                all_records = all_records.order_by("-id")
            #分页
            pageinator = Paginator(all_records, limit)
            page = int(int(offset) / int(limit) + 1)
            sl = self.get_serializer(pageinator.page(page), many=True)
            response_data = {'total': all_records.count(), 'rows': sl.data}
            
            
            return Response(response_data)

        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['env'] = IpSource.objects.get(id=env_dispatch(serializer.validated_data['ip']))
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['env'] = IpSource.objects.get(id=env_dispatch(serializer.validated_data['ip']))
        #serializer.validated_data['idc'] = IpSource.objects.get(id=env_dispatch(serializer.validated_data['ip']))
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
        
        
    
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          #IsOwnerOrReadOnly,)




