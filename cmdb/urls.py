from django.conf.urls import  url
import views,envviews
from cmdb.views import HostViewSet

host_list = HostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
host_detail = HostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^host_list/$', views.List_Host, name='List_Host'),
    #url(r'sync',views.sync_asset_to_host,name='sync_asset_to_host'),
    url(r'^env_add/$', envviews.IpSourceView.as_view(),name='env_add'),
    
    url(r'^host_add/$', views.List_Host, name='host_add'),
    url(r'^host_edit/$', views.List_Host, name='host_edit'),
    url(r'^host_view/$', views.List_Host, name='host_view'),
    
    #rest
    url(r'^host/$', host_list, name='host-list'),   
    url(r'^host/(?P<pk>[0-9]+)/$', host_detail, name='host-detail'),
    ]
