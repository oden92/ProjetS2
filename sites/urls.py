from django.urls import path
from . import views


urlpatterns=[
    path("",views.detail2,name="home"),
    path('noslivres',views.noslivres,name="noslivres")
]
