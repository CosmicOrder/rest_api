from rest_framework import serializers

from new_api.models import SomeObject


class SomeObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeObject
        fields = '__all__'


class SomeObjectRetrieveSerializer(serializers.ModelSerializer):
    child = SomeObjectListSerializer(many=True)

    class Meta:
        model = SomeObject
        fields = ['id', 'name', 'object_type', 'child']
