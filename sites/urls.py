from django.urls import path
from . import views

urlpatterns=[
    path("detail2",views.detail2,name="detail2"),
]
