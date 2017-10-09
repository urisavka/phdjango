from django.conf.urls import url

from . import views
from . import run_config_views

app_name = 'models'
urlpatterns = [
    url(r'^$', views.ModelIndexView.as_view(), name='model-config-index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.ModelConfigDetailView.as_view(), name='model-config-detail'),
    url(r'^(?P<model_config_id>[0-9]+)/$', views.get_model_config_view, name='model-config-detail'),
    url(r'^result/(?P<pk>[0-9]+)$', views.ModelResultDetailView.as_view(), name='model-result-detail'),
    url(r'^run/$', views.run, name='run'),
    url(r'^prepare-run/$', views.prepareRun, name='prepare-run'),
    url(r'^model/create/$', views.create_model_config, name='model-config-create'),
    url(r'^model/(?P<model_config_id>[0-9]+)/edit/household/$', views.edit_model_config_household, name='model-config-edit-household_structure'),
    url(r'^model/(?P<model_config_id>[0-9]+)/edit/government/$', views.edit_model_config_government, name='model-config-edit-government_structure'),
    url(r'^model/(?P<model_config_id>[0-9]+)/edit/production-firm/$', views.edit_model_config_production_firm, name='model-config-edit-production_firm_structure'),
    url(r'^model/(?P<model_config_id>[0-9]+)/edit/raw-firm/$', views.edit_model_config_raw_firm, name='model-config-edit-raw_firm_structure'),
    url(r'^model/(?P<model_config_id>[0-9]+)/edit/capital-firm/$', views.edit_model_config_capital_firm, name='model-config-edit-capital_firm_structure'),
    url(r'^model/(?P<model_config_id>[0-9]+)/edit/$', views.edit_model_config, name='model-config-edit-basic'),

    url(r'^model-run-config/$', run_config_views.RunConfIndexView.as_view(), name='model-run-config-index'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/$', run_config_views.get_model_run_config_view, name='model-run-config-detail'),
    url(r'^model-run-config/create/$', run_config_views.create_model_run_config, name='model-run-config-create'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/household/$', run_config_views.edit_model_run_config_household, name='model-run-config-edit-household_config'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/government/$', run_config_views.edit_model_run_config_government, name='model-run-config-edit-government_config'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/raw-firm/$', run_config_views.edit_model_run_config_firm_raw, name='model-run-config-edit-raw_firm_config'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/capital-firm/$', run_config_views.edit_model_run_config_firm_capital, name='model-run-config-edit-capital_firm_config'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/production-firm/$', run_config_views.edit_model_run_config_firm_production, name='model-run-config-edit-production_firm_config'),

    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/(?P<key>.+)/add-learning/$', run_config_views.create_learning, name='model-run-config-edit-firm_config-add_learning'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/(?P<key>.+)/edit-learning/(?P<learning_id>[0-9]+)$', run_config_views.edit_learning, name='model-run-config-edit-firm_config-edit_learning'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/(?P<key>.+)/delete-learning/(?P<learning_id>[0-9]+)$', run_config_views.delete_learning, name='model-run-config-edit-firm_config-delete_learning'),

    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/outside-world$', run_config_views.edit_model_run_config_outside_world, name='model-run-config-edit-outside_world_config'),
    url(r'^model-run-config/(?P<model_run_config_id>[0-9]+)/edit/$', run_config_views.edit_model_run_config, name='model-run-config-edit-basic'),
]