from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'guides'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sort/(?P<filter>[\w]+)/$', views.SortedIndexView.as_view(), name='index_sorted'),
    url(r'^section/(?P<section>[\w_-]+)/$', views.SectionView.as_view(), name='section'),
    url(r'^sections_browser/$', views.SectionBrowserView.as_view(), name='sections_browser'),
    url(r'^my_guides/$', login_required(views.MyGuidesView.as_view()), name='my_guides'),
    url(r'^(?P<pk>[0-9]+)/$', views.GuideView.as_view(), name='guide'),
    url(r'^create_guide/$', login_required(views.CreateGuideView.as_view()), name='create_guide'),
    url(r'^about_us/$', views.AboutUsView.as_view(), name='about_us'),
    url(r'^vote/(?P<guide_pk>[0-9]+)/$', login_required(views.vote), name='vote'),
]
