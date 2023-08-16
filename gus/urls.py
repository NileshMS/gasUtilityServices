from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ServicesListView.as_view(), name='service-home'),
    path('service-detail/', views.ServiceDetailView.as_view(), name='service-detail'),
]
