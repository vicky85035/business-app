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
    
class BranchSerializer(serializers.ModelSerializer):
    Business = serializers.StringRelatedField(source = 'business')
    Branch_name = serializers.SerializerMethodField()
    created_by = serializers.EmailField(source='added_by')
    created_on = serializers.DateTimeField(source = 'business.created_at')
    Team_members = serializers.StringRelatedField(source = 'business.team')

    class Meta:
        model = Branch
        fields = [
            'id',
            'Business',
            'Branch_name',
            'created_by',
            'created_on',
            'Team_members',
        ]

    def get_Branch_name(self, obj):
        if obj.name:
            return obj.name
        else:
            return obj.alias