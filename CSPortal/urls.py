from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration import views as reg_views
from Portal import views, forms
from django.contrib import admin
from django.contrib.auth.views import password_reset_confirm
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/faq/$', views.faq, name='faq_view'),
    url(r'^(?P<site>\w+)/$', views.main, name='main_view'),
    url(r'^$', views.index, name='index_view'),
    url(r'^post/delete/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.delete_post,name='delete_post'),
   
    url(r'^main/csclub/', views.csclub, name='csclub_view'),
    #marketplace
    url(r'^marketplace/post/project/(?P<post_id>\d+)/$',views.get_post_project, name='get_post_project'),
    url(r'^marketplace/post/new/project/$',views.create_post_project, name='create_post_project'),
    url(r'^marketplace/post/edit/project/(?P<post_id>\d+)/password/(?P<edit_or_delete>\w+)/$',views.edit_post_password_project, name='edit_post_password_project'),
    url(r'^marketplace/post/delete/project/(?P<post_id>\d+)/password/$',views.delete_password_project, name='delete_password_project'),
    url(r'^marketplace/post/edit/project/(?P<post_id>\d+)/$',views.edit_post_project, name='edit_post_project'),
    url(r'^marketplace/filter/', views.filter_posts_project, name='filter_posts_project'),
    url(r'^marketplace/post/project/(?P<post_id>\d+)/contact/$',views.contact_client, name='contact_project'),
    
    #jobs
    url(r'^jobs/post/(?P<post_id>\d+)/$',views.get_post_job, name='get_post_job'),
    url(r'^jobs/post/edit/job/(?P<post_id>\d+)/$',views.edit_post_job, name='edit_post_job'),
    url(r'^jobs/post/new/$',views.create_post_job, name='create_post_job'),
    url(r'^jobs/filter/', views.filter_posts_job, name='filter_posts_job'),
    url(r'^jobs/post/edit/(?P<post_id>\d+)/password/(?P<edit_or_delete>\w+)/$',views.edit_post_password_job, name='edit_post_password_job'),
    url(r'^jobs/post/delete/(?P<post_id>\d+)/password/$',views.delete_password_job, name='delete_password_job'),
    
    #gethired
    url(r'^gethired/post/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.get_post_gethired,name='get_post'),
    url(r'^gethired/post/new/(?P<post_type>\w+)/$',views.render_new_post_form, name='render_new_post'),
    url(r'^gethired/post/new/(?P<post_type>\w+)/(?P<post_id>\d*)/$',views.create_post_gethired,name='create_post'),
    url(r'^gethired/post/edit/(?P<post_type>\w+)/(?P<post_id>\d+)/$',views.render_new_post_form, name='render_edit_post'),
    url(r'^gethired/company/(?P<name>[0-9A-Za-z\-]+)/$', views.get_company, name='get_company'),
    url(r'^gethired/filter/', views.filter_posts_gethired, name='filter_posts_gethired'),
    url(r'^gethired/post/list/company/$', views.get_company_json_list),
   
    #Registration 
    url(r'^accounts/logout/$', views.logout_view),
    url(r'^accounts/profile/$', views.userprofile),
    url(r'^accounts/register/$',
        views.registrationview.as_view(),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

urlpatterns += staticfiles_urlpatterns()
