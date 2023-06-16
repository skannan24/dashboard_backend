from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dashboards_app import views

router = routers.DefaultRouter()
router.register('dashboards', views.DashboardsAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
    path('api/', include(router.urls))
]
