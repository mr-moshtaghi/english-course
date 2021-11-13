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
        path('', views.VideoView.as_view({
            'get': 'list'
        })),
        path('<int:pk>/', views.VideoView.as_view({
            'get': 'retrieve'
        })),
        path('viewed/', views.VideoUserView.as_view(
            {'post': 'create'}
        )),
    ]))),
    path('words/', include(([
        path('', views.WordView.as_view({
            'get': 'list'
        })),
        path('<int:pk>/', views.WordView.as_view({
            'get': 'retrieve'
        })),
        path('viewed/', include([
            path('', views.WordUserView.as_view({
                'post': 'create'
            })),
            path('<int:pk>/learned/', views.WordUserView.as_view({
                'patch': 'learned'
            }))
        ])),
    ]))),
    path('not-learned-word/', views.NotLearnedWord.as_view({
        'get': 'list'
    }))
]
