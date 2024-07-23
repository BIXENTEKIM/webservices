from rest_framework import serializers
from .models import Receipting

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model =Receipting
        fields ='__all__'