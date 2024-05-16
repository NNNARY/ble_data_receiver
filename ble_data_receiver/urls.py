"""ble_data_receiver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from data_handler.views import data_receiver, root_view, graph_data_view, graph_distance_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_view, name='root'),
    path('data-receiver/', data_receiver, name='data-receiver'),
    path('chart-data/', graph_data_view, name='chart-data'),
    path('graph-data/', graph_distance_view, name='graph-data'),# 새로운 URL 패턴 추가
    # 다른 URL 패턴들을 필요에 따라 추가할 수 있습니다.
]