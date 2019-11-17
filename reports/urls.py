"""military_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [

    # path('', views.report_home_view, name='index'),
    path('', views.serviceman_list_view, name='users'),
    path('serviceman_list', views.serviceman_list_view, name='users'),
    path('edit_chain/<int:serviceman_id>', views.edit_service_members_chain_view, name='edit_service_members_chain'),
    path('reports_list/<int:serviceman_id>/', views.reports_list_view, name='reports_list'),
    path('report_filling/<int:report_id>/', views.report_filling_view, name='report_filling'),

    # path('generate_report', views.generate_report_view, name='generate_report'),

    # path('form', views.dyn_form_view, name='form'),
    # path('test_form', views.test_form_view, name='test_form'),

]

