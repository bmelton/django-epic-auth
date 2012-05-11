from rauth.service import OAuth1Service

from lazycal.settings import * 

class Twitter():
	request_token 		= ""
	request_token_secret 	= ""
	authorize_url		= ""

	auth_service = OAuth1Service(
		name		  = 'twitter',
		consumer_key	  = TWITTER_CONSUMER_KEY,
		consumer_secret	  = TWITTER_CONSUMER_SECRET,
		request_token_url = 'https://api.twitter.com/oauth/request_token',
		access_token_url  = 'https://api.twitter.com/oauth/access_token',
		authorize_url 	  = 'https://api.twitter.com/oauth/authorize',
		header_auth	  = True)

	def __init__(self): 
		# This will be called as soon as our class is instantiated, which should be
		# as soon as the view is fired, effectively.
		request_token, request_token_secret = self.auth_service.get_request_token(method='GET')

		authorize_url = self.auth_service.get_authorize_url(request_token)

		self.request_token 	  = request_token
		self.request_token_secret = request_token_secret
		self.authorize_url 	  = authorize_url

		# At this point, redirect user to the authorize_url.  
		# They will be 'called back' to a URL we must define, and we will consume 
		# the 'oauth_verifier' value from the QueryString, then authenticate the 
		# user and redirect them to ... somewhere.

	def callback(self, oauth_verifier):
		response = self.auth_service.get_access_token(
			'GET', 
			request_token=self.request_token, 
			request_token_secret=self.request_token_secret, 
			params={'oauth_verifier': oauth_verifier}
		)
		data 			= response.content
		access_token 		= data['oauth_token']
		access_token_secret 	= data['oauth_token_secret']

		# After the response is consumed, we'll need to 'authenticate' them via 
		# Django methods and/or store their access_token and access_token_secret
		# to a model of some sort. 

class LinkedIn():
	request_token		= ""
	request_token_secret	= ""
	authorize_url		= ""

	auth_service = OAuth1Service(
		name 		= 'linkedin',
		consumer_key	= LINKEDIN_API_KEY,
		consumer_secret = LINKEDIN_SECRET_KEY,
		request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken',
		authorize_url 	= 'https://api.linkedin.com/uas/oauth/authorize',
		access_token_url= 'https://api.linkedin.com/uas/oauth/accessToken')

	def __init__(self):
		request_token, request_token_secret = self.auth_service.get_request_token(method='GET')
		authorize_url = self.auth_service.get_authorize_url(request_token)

		self.request_token 	  = request_token
		self.request_token_secret = request_token_secret
		self.authorize_url 	  = authorize_url

	def callback(self, oauth_verifier):
		response = self.auth_service.get_access_token('GET',
			request_token 		= self.request_token,
			request_token_secret	= request_token_secret,
			params			= {'oauth_verifier': oauth_verifier}
		)
		data 			= response.content
		access_token 		= data['oauth_token']
		access_token_secret	= data['oauth_token_secret']
