from rest_framework import serializers
from .models import FileUploader, Order

class FileUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploader
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"