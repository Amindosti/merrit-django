from rest_framework import serializers
from .models import CreateForm


class FormSerializer(serializers.ModelSerializer):
    formarray = serializers.BaseSerializer

    class Meta:
        model = CreateForm
        fields = ('formarray',)
