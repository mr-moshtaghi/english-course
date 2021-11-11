from rest_framework import serializers
from .models import Course, Video, CourseUser


class CourseSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'is_viewed')

    def get_is_viewed(self, obj):
        return obj.is_viewed(self.context.get('request').user)


class CourseUserSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CourseUser
        exclude = ('created_at', 'updated_at', 'user')

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)



class CourseVideoSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ('id', 'title', 'url', 'is_viewed')

    def get_is_viewed(self, obj):
        return obj.is_viewed(self.context.get('request').user)

