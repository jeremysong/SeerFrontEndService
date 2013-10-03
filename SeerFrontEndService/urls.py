from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SeerFrontEndService.views.home', name='home'),
    # url(r'^SeerFrontEndService/', include('SeerFrontEndService.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'seerui.views.index', name='index'),
    url(r'^tab1/$', 'seerui.views.tab1', name='tab1'),
    url(r'^tab2/$', 'seerui.views.tab2', name='tab2'),
    url(r'^tab3/$', 'seerui.views.tab3', name='tab3'),

    #Test 404 page
    url(r'^404page', 'seerui.views.page_not_found_error', name='404'),
    url(r'^500page', 'seerui.views.server_error', name='500'),
)