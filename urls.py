from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'socialauth.views.index', name='social_auth'),
	url(r'^twitter/callback', 'socialauth.views.twitter_callback', name='twitter_callback'),
	url(r'^twitter/', 'socialauth.views.twitter', name='twitter'),
	url(r'^linkedin/callback', 'socialauth.views.linkedin_callback', name='linkedin_callback'),
	url(r'^linkedin/', 'socialauth.views.linkedin', name='linkedin'),
	# url(r'^lazycal/', include('lazycal.foo.urls')),
)
