from django.shortcuts import render

from rest_framework import viewsets

from .serializers import *


class DashboardsAPI(viewsets.ModelViewSet):
    serializer_class = DashboardsSerializer
    queryset = Dashboards.objects.all()
