from django.urls import path, include

from core import views

app_name = 'core'
urlpatterns = [
    path('courses/', include(([
        path('', views.ListCourseView.as_view({
            'get': 'list',
        })),
        path('viewed/', views.CourseUserView.as_view(
            {'post': 'create'}
        )),
        path('<int:course_pk>/', include([
            path('', views.ListCourseView.as_view({
                'get': 'retrieve'
            })),
            path('videos/', views.ListCourseVideoView.as_view(
                {'get': 'list'}
            ))
        ])),
    ]))),
    path('videos/', include(([
        path('', views.ListVideoView.as_view({
            'get': 'list'
        })),
        path('viewed/', views.VideoUserView.as_view(
            {'post': 'create'}
        )),
    ])))
]
