from rest_framework import serializers
from .models import Students

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model =Students
        fields ='__all__'