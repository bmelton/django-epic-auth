from social import Twitter, LinkedIn
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	return HttpResponse("Social Auth")

def linkedin(request):
	linkedin = LinkedIn()
	request.session["access_token"] 		= linkedin.request_token
	request.session["access_token_secret"] 	= linkedin.request_token_secret
	return HttpResponseRedirect("%s" % linkedin.authorize_url)
	
def twitter(request):
	twitter = Twitter()
	request.session["access_token"] = twitter.request_token
	request.session["access_token_secret"] = twitter.request_token_secret
	return HttpResponseRedirect("%s" % twitter.authorize_url)

def twitter_callback(request):
	if request.GET.get("oauth_token"):
		if request.GET.get("oauth_verifier"):
			if "access_token" in request.session:
				var = request.GET["oauth_verifier"]
				return HttpResponse("Twitter callback " + var)
			else:
				return HttpResponse("How did you get here?")
		else: 
			return HttpResponse("Received token, but no verification.")
	else:
		return HttpResponse("Twitter callback failed")

def linkedin_callback(request):
	if request.GET.get("oauth_token"):
		if request.GET.get("oauth_verifier"):
			if "access_token" in request.session:
				var = request.GET["oauth_verifier"]
				return HttpResponse("Linkedin callback " + var)
			else:
				return HttpResponse("How did you get here?")
		else: 
			return HttpResponse("Received token, but no verification.")
	else:
		return HttpResponse("Linkedin callback failed")
