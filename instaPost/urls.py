"""
instaPost URL Configuration
"""
from django.conf.urls import url, include
from instaPost import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Instagram upload image
    url(r'^upload_image/$', views.upload_photo),
    # Splinter parse
    url(r'^get_info/$', views.splinter_parse),
    # Auth
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)