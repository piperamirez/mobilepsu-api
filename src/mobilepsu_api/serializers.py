from rest_framework import serializers
from mobilepsu_api.models import Field

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('id', 'name')