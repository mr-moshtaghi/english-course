from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'is_viewed')

    def get_is_viewed(self, obj):
        return obj.is_viewed(self.context.get('request').user)

