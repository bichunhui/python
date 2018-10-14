from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<a>\d{3})(?P<b>\d{3})(?P<c>\d+)', views.digital, name="digital"),
    url(r'^include/$', views.include, name="include"),
    url(r'^reverse/$', views.reverse, name="reverse"),
    url(r'^base/$', views.base, name="base"),
    url(r'^child/$', views.child, name="child"),
    url(r'^base_goods/$', views.base_goods, name="base_goods"),
    url(r'^base_user/$', views.base_user, name="base_user"),
    url(r'^content/$', views.content, name="content"),

]