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
    business = serializers.CharField(source = 'business.name')
    branch_name = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    created_on = serializers.DateTimeField(source = 'business.created_at')
    team_members = serializers.SerializerMethodField()

    class Meta:
        model = Branch
        fields = [
            'id',
            'business',
            'branch_name',
            'created_by',
            'created_on',
            'team_members',
        ]

    def get_branch_name(self, obj):
        if obj.name:
            return obj.name
        else:
            return obj.alias

    def get_team_members(self, obj):
        members = []
        for user in obj.branch_owner.all():
            members.append(
                {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'joined_date': user.date_joined,
                    'no_of_locations': Branch.objects.filter(branch_owner=user.id).count()
                }
            )
        return members
    
        # return list(obj.branch_owner.all().values_list('first_name', flat=True))
    
    def get_created_by(self,obj):
        # return f'{obj.added_by.first_name} {obj.added_by.last_name}' 
        if obj.added_by.last_name:
            return f'{obj.added_by.first_name} {obj.added_by.last_name}'
        return obj.added_by.first_name