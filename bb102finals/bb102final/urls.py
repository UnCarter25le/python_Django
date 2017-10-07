"""bb102final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from elephant import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^index_puli/', views.index_puli),
    url(r'index_googlemap/', views.index_googlemap),
    url(r'^googlemap1/', views.googlemap1),
    url(r'^googlemap2/', views.googlemap2),
    url(r'^googlemap3/', views.googlemap3),
    url(r'^daan_burglar/', views.daan_burglar),
    url(r'^daan_pets/', views.daan_pets),
    url(r'^daan_gogoro/', views.daan_gogoro),
    url(r'^daan_noise/', views.daan_noise),
    url(r'^daan_narrowroadway/', views.daan_narrowroadway),
    url(r'^daan_temple/', views.daan_temple),
    # url(r'^daan_suite/', views.daan_suite),
    url(r'^daan_room_test/', views.daan_room_test),
    url(r'^city_01/', views.city_01),
    url(r'^city_02/', views.city_02),
    url(r'^city_03/', views.city_03),
    url(r'^city_04/', views.city_04),
    url(r'^city_05/', views.city_05),
    url(r'^one_by_case/', views.one_by_case),
    url(r'^district/', views.district),
    url(r'^track_list/', views.track_list),
    url(r'^object_select/', views.object_select),
    url(r'^home/', views.home),
    url(r'^tucheng_test/', views.tucheng_test),

]
