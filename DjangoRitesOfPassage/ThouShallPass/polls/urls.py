#========================
#App: Thou Shall Pass
#Doc: urls.py
#========================

from django.conf.urls import patterns, url
from polls import views


#create a URLconf so that Django can call a view by mapping it to a URL
urlpatterns = patterns('', 
	#ex: /polls/
	#url(r'^$', views.index, name='index'),
	#This is the simpler updated version "Generic Views Version"
	url(r'^$', views.IndexView.as_view(), name='index'),
	
	#ex: /polls/5/
	#url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
	#This is the "Generic Views Version"
	url(r'^(?P<poll_id>\d+)/$', views.DetailView.as_view(), name='detail'),
	
	#ex: /poll/5/results/
	#url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
	#This is the "Generic Views Version"
	url(r'^(?P<poll_id>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	
	#ex: /polls/5/vote/
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)

