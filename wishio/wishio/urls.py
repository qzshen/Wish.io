from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wishlist.views.home', name='home'),
    #url(r'^wishio/', include('wishio.views.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'wishlist.views.home', name='home'),
    url(r'^register', 'wishlist.views.register', name='register'),
    url(r'^wishlist/(?P<board_id>\d+)', 'wishlist.views.wishlist', name='wishlist'),
    url(r'^wishlist', 'wishlist.views.wishlist', name='wishlist'),
    url(r'^friends', 'wishlist.views.friends', name='friends'),
)

