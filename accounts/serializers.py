from rest_framework import serializers
from accounts.models import User
from business.models import Branch

class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source = 'date_joined')
    # no_of_locations = serializers.SerializerMethodField()
    no_of_locations = serializers.IntegerField(source="user_count")

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'created_at',
            'no_of_locations',
        ]

    # def get_no_of_locations(self, obj):
    #     return Branch.objects.filter(branch_owner=obj.id).count()