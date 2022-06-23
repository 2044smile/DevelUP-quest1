from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    ]
