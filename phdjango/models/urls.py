from django.conf.urls import url

from . import views

app_name = 'models'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ModelConfigDetailView.as_view(), name='model-config-detail'),
    url(r'^result/(?P<pk>[0-9]+)$', views.ModelResultDetailView.as_view(), name='model-result-detail'),
    url(r'^run/$', views.run, name='run'),
    url(r'^prepare-run/$', views.prepareRun, name='prepare-run'),
]