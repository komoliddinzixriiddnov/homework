from django.urls import path
from .views import courses_view

urlpatterns=[
    path("courese/", courses_view,name='courses'),
]