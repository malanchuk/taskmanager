# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),     # после admin/ в урле переходить 
  # url(r'^basicview/', include('task.urls')),     # после basicview переходить в приложение article, там искать файл urls.py, дальнейшие инструкции в нем
    url(r'^auth/', include('loginsys.urls')),	   # после auth/ переходить в приложение loginsys, там искать файл urls.py, дальнейшие инструкции в нем
    url(r'^', include('task.urls')),	           # после доменного имени(с главной) переходить в приложение article, там искать файл urls.py, дальнейшие инструкции в нем
)

"""

url(r'^basicview/', include('task.urls')) - 
include обозначает, что после basicview/
Джанго пойдёт искать продолжение урла 
в task.urls(приложение task, файл urls)

url(r'^', include('task.urls')) - 
при заходе на главную сайта будет осуществляться 
переход на страницу со всеми статьями

"""

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)