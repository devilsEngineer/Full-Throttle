from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import User,ActivityPeriod

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ActivityPeriodSerializer(DocumentSerializer):
    class Meta:
        model = ActivityPeriod
        fields = '__all__'