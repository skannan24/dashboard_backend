from rest_framework import serializers
from .models import *


class DashboardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboards
        fields = "__all__"
