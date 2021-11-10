from django.urls import path, include

from core import views

app_name = 'core'
urlpatterns = [
    # path('courses/',include ListCourse.as_view({'get': 'list'}), name='list_course'),

    path('courses/', include(([
        path('', views.ListCourse.as_view({
            'get': 'list',
        })),
        path('<int:pk>', views.ListCourse.as_view({
            'get': 'retrieve'
        }))
    ]))),
]
