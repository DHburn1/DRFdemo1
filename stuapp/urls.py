from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from stuapp import views

urlpatterns = [
    url(r'^actors/latest/$', views.ActorListView.as_view({'get':'latest'})),
    # url(r'^actors/$', views.ActorListView.as_view()),
    url(r'^actors/(?P<pk>\d+)/age/$', views.ActorListView.as_view({'put':'age'})),
]

