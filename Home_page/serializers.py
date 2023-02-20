from rest_framework import serializers
from Form.models import CreateForm


class HomePageSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateForm
        fields = ('formarray', 'id')
