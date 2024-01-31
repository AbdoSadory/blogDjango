from rest_framework import serializers
from .models import Writer,Blog

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Writer
        fields = ['name','email','age']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = ['title','content','published_at',"writer_id"]