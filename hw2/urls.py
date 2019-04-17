from django.urls import path
from . import views

urlpatterns = [
    path('historical/', views.record_list),
    path('historical/<int:dt>/', views.record_detail),
    #url(r'^historical/(?P<dt>[0-9]{8})/$', views.record_detail),
    #url(r'^historical/', views.record_list),
    ]

