from rest_framework import serializers
from . models import Plan

class PlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plan
        # data shown as JSON
        fields = ['id', 'name', 'price', 'validity', 'daily_internet',]