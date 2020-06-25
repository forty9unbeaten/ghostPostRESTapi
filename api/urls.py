from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from api import views

router = DefaultRouter()

router.register(r'posts', views.PostsViewSet)

url_patterns = [
    url(r'^api/', include(router.urls))
]
