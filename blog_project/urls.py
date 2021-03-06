# -*- coding: utf-8 -*-

"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
# from blog.upload import upload_image
from DjangoUeditor import urls as djud_urls

urlpatterns = [
    # # 文件上传
    # url(
    #     r"^uploads/(?P<path>.*)$",
    #     "django.views.static.serve",
    #     {"document_root": settings.MEDIA_ROOT,}),
    # # admin文件上传
    # url(
    #     r'^admin/upload/(?P<dir_name>[^/]+)$',
    #     upload_image,
    #     name='upload_image'),
    # # admin
    url(r'^admin/', include(admin.site.urls)),
    # 主站
    url(r'^', include('blog.urls')),
    url(r'^ueditor/',include(djud_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)