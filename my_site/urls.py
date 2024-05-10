"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from sites.views import detail,home,noslivres,genre,genre_category,nosauteurs,newlivre,noslivresauteur,auteur,bioauteurs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('livre/<int:id_livre>',detail,name="detail"),
    path("noslivres",noslivres,name="noslivres"),
    path("auteur",auteur,name="auteur"),
    path("genre",genre,name="genre"),
    path('genres/<str:category>/', genre_category, name='genre_category'),
    path("nosauteurs",nosauteurs,name="nosauteurs"),
    path("auteurs/<str:auteur>/",bioauteurs,name='bioauteurs'),
    path("newlivre",newlivre,name="newlivre"),
    path('noslivresauteur/<int:auteur_id>',noslivresauteur,name="noslivresauteur"),


    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


