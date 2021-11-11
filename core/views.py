from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from core.models import Course, Video, CourseUser, VideoUser
from core.serializers import CourseSerializer, CourseVideoSerializer, CourseUserSerializer, VideoUserSerializer


class ListCourseView(viewsets.ViewSet):
    def list(self, request):
        context = {
            'request': request
        }
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        context = {
            'request': request
        }
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course, context=context)
        return Response(serializer.data)


class ListVideoView(viewsets.ViewSet):
    def list(self, request):
        context = {
            'request': request
        }
        queryset = Video.objects.all()
        serializer = CourseVideoSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        context = {
            'request': request
        }
        queryset = Video.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseVideoSerializer(course, context=context)
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


class ListCourseVideoView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        context = {
            'request': request
        }
        course_pk = kwargs.get('course_pk')
        videos = Video.objects.filter(course_id=course_pk)
        serializer = CourseVideoSerializer(videos, many=True, context=context)
        return Response(serializer.data)
