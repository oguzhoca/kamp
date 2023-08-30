from django.urls import path
from . import views


urlpatterns = [
    path('', views.client_view, name="client"),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('clients/date/<str:date>/', views.ClientDateView.as_view(), name='client-date'),
    path('blog/date/<str:date>/', views.BlogDateView.as_view(), name='blog-date'),



]