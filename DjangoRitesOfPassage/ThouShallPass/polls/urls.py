#========================
#App: Thou Shall Pass
#Doc: urls.py
#========================

from django.conf.urls import patterns, include, url
from polls import views
from django.contrib import admin
admin.autodiscover()

create a URLconf so that Django can call a view by mapping it to a URL
urlpatterns = patterns('', 
	url(r'^$', views.index, name='index')
)

#point the root URLcong at the polls.urls module
urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', include(admin.site.urls)),
)

