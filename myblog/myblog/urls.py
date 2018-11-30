"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
# 上面这行多加了一个re_path
from django.views.static import serve
# 导入静态文件模块
from django.conf import settings
# 导入配置文件里的文件上传配置
import xadmin
from blog.views import IndexView,ListView,ContentView,TagView,SearchView,AboutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', xadmin.site.urls),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 增加此行
    path('', IndexView.as_view(), name='index'),
    path('list-<int:lid>.html/',ListView.as_view(),name='list'),
    path('show-<int:sid>.html',ContentView.as_view(),name='content'),
    path('tag/<tag>',TagView.as_view(),name='tag'),
    path('s/',SearchView.as_view(),name='search'),
    path('about/',AboutView.as_view(),name='about'),
]
