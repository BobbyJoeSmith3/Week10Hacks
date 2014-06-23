from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ThouShallPass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#point the root URLconf at the polls.urls module
	url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
