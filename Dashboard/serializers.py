from rest_framework import serializers
from .models import Post
from Form.models import CreateForm


class DashboardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = []


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateForm
        fields = ('author', 'form_array', 'id')
