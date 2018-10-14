from django.conf.urls import include, url
import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^getTest1/$', views.gettest1),
    url(r'^getTest2/$', views.gettest2),
    url(r'^getTest3/$', views.gettest3),
    url(r'^postTest1/$', views.posttest1),
    url(r'^postTest2/$', views.posttest2),
    url(r'^cookieTest/$', views.cookietest),
    url(r'^redTest1/$', views.redtest1),
    url(r'^redTest2/$', views.redtest2),
    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2_handle/$', views.session2_handle),
    url(r'^session3/$', views.session3),
]