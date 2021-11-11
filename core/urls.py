from django.urls import path, include

from core import views

app_name = 'core'
urlpatterns = [
    path('courses/', views.CourseView.as_view({
        'get': 'list'
    })),
    path('courses/<int:course_pk>/', views.CourseView.as_view({
        'get': 'retrieve'
    })),
    path('courses/<int:course_pk>/videos/', views.CourseVideoView.as_view({
        'get': 'list'
    })),
    path('courses/<int:course_pk>/videos/<int:video_pk>/', views.CourseVideoView.as_view({
        'get': 'retrieve'
    })),
    path('courses/<int:course_pk>/videos/<int:video_pk>/words/', views.CourseVideoWordView.as_view({
        'get': 'list'
    })),
    path('courses/<int:course_pk>/videos/<int:video_pk>/words/<int:word_pk>/', views.CourseVideoWordView.as_view({
        'get': 'retrieve'
    })),

    path('courses/viewed/', views.CourseUserView.as_view({
        'post': 'create'
    })),
    path('videos/', include(([
        path('', views.ListVideoView.as_view({
            'get': 'list'
        })),
        path('viewed/', views.VideoUserView.as_view(
            {'post': 'create'}
        )),
    ])))
]
