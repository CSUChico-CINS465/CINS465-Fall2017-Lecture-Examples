from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'page2$',views.page2, name='page2'),
    url(r'register/$',views.register, name='register'),
    url(r'suggestions/$',views.suggestions, name='suggestions'),
    url(r'suggest/$',views.suggest, name='suggest'),

]
