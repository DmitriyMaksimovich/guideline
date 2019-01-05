from django.conf.urls import url
from . import views

app_name = 'guides'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sort/(?P<filter>[\w]+)/$', views.SortedIndexView.as_view(), name='index_sorted'),
    url(r'^section/(?P<section>[\w]+)/$', views.SectionView.as_view(), name='section'),
    url(r'^sections_browser/$', views.SectionBrowserView.as_view(), name='sections_browser'),
    url(r'^(?P<pk>[0-9]+)/$', views.GuideView.as_view(), name='guide'),
    url(r'^about_us/$', views.about_us_view, name='about_us'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]
