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
urlpatterns = []