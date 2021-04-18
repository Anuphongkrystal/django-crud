from django.contrib import admin
from django.urls import path
from Cryptocurrencies import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('insert/',views.insert,name="insert"),
     path('search/',views.search,name="search"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name='delete'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit, name='edit')
]

if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
