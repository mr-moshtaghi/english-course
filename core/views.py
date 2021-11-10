from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Course
from core.serializers import CourseSerializer


class ListCourse(viewsets.ViewSet):
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
