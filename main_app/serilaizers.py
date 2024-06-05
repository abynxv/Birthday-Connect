from .models import FriendsModel
from rest_framework import serializers

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsModel
        fields = '__all__'
