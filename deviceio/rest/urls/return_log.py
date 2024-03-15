from django.urls import path
from deviceio.rest.views import return_log

app_name = 'return_log'

urlpatterns = [
    path('return_log/create', return_log.ReturnLogCreateView.as_view(),name='return_log-create'),
    path('return_log/list', return_log.ReturnLogListView.as_view(),name='return_log-list'),
    path('return_log/detail/<uuid:uuid>', return_log.ReturnLogRetrieveUpdateDestroyView.as_view(),name='return_log.detail.update.destroy'),

]