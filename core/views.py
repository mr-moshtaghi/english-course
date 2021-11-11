from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from core import const
from core.models import Course, Video, CourseUser, VideoUser, Word, WordUser
from core.serializers import CourseSerializer, VideoSerializer, CourseUserSerializer, VideoUserSerializer, \
    WordSerializer, WordUserSerializer


class CourseView(viewsets.ViewSet):
    def list(self, request):
        context = {
            'request': request
        }
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, course_pk=None):
        context = {
            'request': request
        }
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=course_pk)
        serializer = CourseSerializer(course, context=context)
        return Response(serializer.data)


class VideoView(viewsets.ViewSet):
    def list(self, request):
        context = {
            'request': request
        }
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        context = {
            'request': request
        }
        queryset = Video.objects.all()
        video = get_object_or_404(queryset, pk=pk)
        serializer = VideoSerializer(video, context=context)
        return Response(serializer.data)


class WordView(viewsets.ViewSet):
    def list(self, request):
        context = {
            'request': request
        }
        queryset = Word.objects.all()
        serializer = WordSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        context = {
            'request': request
        }
        queryset = Word.objects.all()
        word = get_object_or_404(queryset, pk=pk)
        serializer = WordSerializer(word, context=context)
        return Response(serializer.data)


class CourseUserView(viewsets.ViewSet):
    queryset = CourseUser.objects.all()
    serializer_class = CourseUserSerializer

    def create(self, request, *args, **kwargs):
        context = {
            'request': request
        }

        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'ok'})


class VideoUserView(viewsets.ViewSet):
    queryset = VideoUser.objects.all()
    serializer_class = VideoUserSerializer

    def create(self, request, *args, **kwargs):
        context = {
            'request': request
        }

        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'ok'})


class WordUserView(viewsets.ViewSet):
    queryset = WordUser.objects.all()
    serializer_class = WordUserSerializer

    def create(self, request, *args, **kwargs):
        context = {
            'request': request
        }
        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'ok'})

    def learned(self, request, pk, *args, **kwargs):
        user = request.user
        word_user = self.queryset.filter(pk=pk).first()
        if not word_user:
            return Response(
                {'Bad Request': "Your request is not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        if not word_user.user == user:
            return Response(
                {'Bad Request': "The user does not have such a word-user"},
                status=status.HTTP_400_BAD_REQUEST
            )

        word_user.status = const.WORD_USER_STATUS_LEARNED
        word_user.save()
        return Response(status=status.HTTP_200_OK)


class CourseVideoView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        context = {
            'request': request
        }
        course_pk = kwargs.get('course_pk')
        videos = Video.objects.filter(course_id=course_pk)
        serializer = VideoSerializer(videos, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, video_pk=None, *args, **kwargs):
        context = {
            'request': request
        }
        course_pk = kwargs.get('course_pk')
        queryset = Video.objects.filter(course_id=course_pk)
        video = get_object_or_404(queryset, pk=video_pk)
        serializer = VideoSerializer(video, context=context)
        return Response(serializer.data)


class CourseVideoWordView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        context = {
            'request': request
        }
        course_pk = kwargs.get('course_pk')
        video_pk = kwargs.get('video_pk')
        words = Word.objects.filter(video__course_id=course_pk, video_id=video_pk)
        serializer = WordSerializer(words, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, word_pk=None, *args, **kwargs):
        context = {
            'request': request
        }
        course_pk = kwargs.get('course_pk')
        video_pk = kwargs.get('video_pk')
        queryset = Word.objects.filter(video__course_id=course_pk, video_id=video_pk)
        word = get_object_or_404(queryset, pk=word_pk)
        serializer = WordSerializer(word, context=context)
        return Response(serializer.data)
