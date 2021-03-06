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
    url(r'^vote_for_comment/$', login_required(views.vote_for_comment), name='vote_for_comment'),
    url(r'^create_guide/$', login_required(views.CreateGuideView.as_view()), name='create_guide'),
    url(r'^about_us/$', views.AboutUsView.as_view(), name='about_us'),
    url(r'^vote/$', login_required(views.vote), name='vote'),
    url(r'delete/$', login_required(views.delete_guide), name='delete_guide'),
    url(r'^edit/(?P<pk>[0-9]+)/$', login_required(views.EditGuideView.as_view()), name='edit_guide'),
]
