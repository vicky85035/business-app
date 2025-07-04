from rest_framework import serializers
from business.models import Branch

class BusinessSerializer(serializers.ModelSerializer):
    business = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    address = serializers.StringRelatedField()

    class Meta:
        model = Branch
        fields = ['id','business','created_at','category','address']