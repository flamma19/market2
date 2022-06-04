from .views import AlertList, AlertDetail, CreateAlert, AdminAlertDetail, EditAlert, DeleteAlert
from django.urls import path

app_name = 'alert'

urlpatterns = [
    path('', AlertList.as_view(), name='listalert'),
    path('alert/<str:pk>/', AlertDetail.as_view(), name='detailalert'),
    path('admin/create', CreateAlert.as_view(), name='createAlert'),
    path('admin/edit/alertdetail/<int:pk>/', AdminAlertDetail.as_view(), name='admindetailalert'),
    path('admin/edit/<int:pk>/', EditAlert.as_view(), name='editAlert'),
    path('admin/delete/<int:pk>/', DeleteAlert.as_view(), name='deleteAlert'),
]
