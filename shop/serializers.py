from rest_framework import serializers
from .models import ProductImage, Product, ProductCommentImage, ProductComment


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = "__all__"
        


















