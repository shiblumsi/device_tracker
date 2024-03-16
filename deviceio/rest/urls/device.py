from django.urls import path
from deviceio.rest.views import device

app_name = 'device'

urlpatterns = [
    path('device/create', device.DeviceCreateView.as_view(),name='device-create'),
    path('device/list', device.DeviceListView.as_view(),name='device-list'),
    path('device/detail/<uuid:uuid>', device.DeviceRetrieveUpdateDestroyView.as_view(),name='device.detail.update.destroy'),
    path('device/search/<uuid:uuid>', device.DeviceDetailView.as_view(),name='device-detail')
]