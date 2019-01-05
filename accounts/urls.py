from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]