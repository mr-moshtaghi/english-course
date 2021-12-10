from rest_framework import serializers
from .models import Course, Video, CourseUser, VideoUser, Word, WordUser


class CourseSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'image', 'is_viewed')

    def get_is_viewed(self, obj):
        return obj.is_viewed(self.context.get('request').user)


class CourseUserSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CourseUser
        exclude = ('created_at', 'updated_at', 'user')

    def create(self, validated_data):
        user = self.context.get('request').user
        course_id = validated_data['course_id']

        if CourseUser.objects.filter(user=user, course_id=course_id).exists():
            raise serializers.ValidationError(
                'This user has already viewed this course')

        validated_data['user'] = user
        return super().create(validated_data)


class VideoSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ('id', 'title', 'video', 'thumbnail', 'is_viewed')

    def get_is_viewed(self, obj):
        return obj.is_viewed(self.context.get('request').user)


class WordUserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordUser
        fields = ('status',)


class VideoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video', 'thumbnail')


class WordSerializer(serializers.ModelSerializer):
    is_viewed = serializers.SerializerMethodField()
    word_user = serializers.ListSerializer(child=WordUserStatusSerializer())
    video = VideoUrlSerializer()

    class Meta:
        model = Word
        fields = ('id', 'english_word', 'translate', 'word_user', 'is_viewed', 'video')

    def get_is_viewed(self, obj):
        return obj.is_viewed(self.context.get('request').user)


class VideoUserSerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True)
    video_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = VideoUser
        exclude = ('created_at', 'updated_at', 'user')

    def create(self, validated_data):
        user = self.context.get('request').user
        video_id = validated_data['video_id']

        if VideoUser.objects.filter(user=user, video_id=video_id).exists():
            raise serializers.ValidationError(
                'This user has already viewed this video')

        validated_data['user'] = user
        return super().create(validated_data)


class WordUserSerializer(serializers.ModelSerializer):
    word = WordSerializer(read_only=True)
    word_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = WordUser
        exclude = ('created_at', 'updated_at', 'user')

    def create(self, validated_data):
        user = self.context.get('request').user
        word_id = validated_data['word_id']

        if WordUser.objects.filter(user=user, word_id=word_id).exists():
            raise serializers.ValidationError(
                'This user has already viewed this video')

        validated_data['user'] = user
        return super().create(validated_data)
