from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'page2$',views.page2, name='page2'),
]
