from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.ndt_index, name='ndt_index'),
    url(r'^ndt_new$', views.ndt_new, name='ndt_new'),
    url(r'^ndt_new_submit$', views.ndt_new_submit, name='ndt_new_submit'),
    url(r'^ndt_edit$', views.ndt_edit, name='ndt_edit'),
    url(r'^ndt_edit_submit$', views.ndt_edit_submit, name='ndt_edit_submit'),
    url(r'^ndt_delete$', views.ndt_delete, name='ndt_delete')

)