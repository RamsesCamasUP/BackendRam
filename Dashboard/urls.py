from .views import ListDashboard, DetailDashboard
from django.urls import path,re_path

urlpatterns = [
    re_path(r'^dashboard/$',ListDashboard.as_view(),name='lista-dash'),
    re_path(r'^dashboard/(?P<pk>[0-9]+)$',DetailDashboard.as_view(),name='detail-dash'),
]
