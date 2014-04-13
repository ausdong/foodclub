from django.conf.urls import patterns, url
from dvc import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^fighters', views.fighters, name='fighters'),
    url(r'^fight', views.fight, name='fight'),
    url(r'^about', views.about, name='about'),
    url(r'^results', views.results, name='results'),
    url(r'^(?P<prompt_id>\d+)/vote/$', views.vote, name='vote'),
)