from rest_framework import serializers
from business.models import Branch, Business

class BusinessSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    Created_at = serializers.DateTimeField(source="created_at")
    Name = serializers.CharField(source="name")
    Category = serializers.CharField(source="category.name")
    no_of_locations = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = [
            'id',
            'Name',
            'Created_at',
            'Category',
            'no_of_locations'
        ]

    def get_no_of_locations(self, obj):
        return Branch.objects.filter(business__id=obj.id).count()