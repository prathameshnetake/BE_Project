# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Import all the libraries required for Twitter Authentication

# <codecell>

from twython import Twython
import urlparse
import oauth2 as oauth
import webbrowser

# <markdowncell>

# Set Keys and URL as variables for easier access

# <codecell>

consumer_key = 'zT5PEASW54S4EpCcNCSyUxuU4'
consumer_secret = 'AfeI9GFJDfAukd6OhNBzqh6eW5NzKNeo2Q3ZtRekchztCDOQYz'
request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

# <markdowncell>

# Initialise the OAuth library.

# <codecell>

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

# <markdowncell>

# Step 1: Get a request token. This is a temporary token that is used for having the user authorize an access token and to sign the request to obtain said access token.

# <codecell>

resp, content = client.request(request_token_url, "GET")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

request_token = dict(urlparse.parse_qsl(content))

print "Request Token:"
print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']

# <markdowncell>

# Step 2: Redirect to the provider. Open link in a new tab.

# <codecell>

url = authorize_url + "?oauth_token=" + request_token['oauth_token']
webbrowser.open_new_tab(url)

# <markdowncell>

# After the user has granted access, he/she needs to enter a PIN which will then be used to authenticate our application.

# <codecell>

accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
oauth_verifier = raw_input('What is the PIN? ')

# <markdowncell>

# Step 3: Once the consumer has successfully authenticated our app, new access tokens are generated which are specific to the user. We use the request token to sign this request. After this is done we throw away the request token and use the access token returned. We store this access token for future use, when the user logs in again.

# <codecell>

token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))
oauth_token = access_token['oauth_token']
oauth_token_secret = access_token['oauth_token_secret']

print "Access Token:"
print "    - oauth_token        = %s" % oauth_token
print "    - oauth_token_secret = %s" % oauth_token_secret
print
print "You may now access protected resources using the access tokens above." 
print

# <markdowncell>

# Prepare your twitter, you will need it for everything

# <codecell>

twitter = Twython(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

# <markdowncell>

# Get the name of the user and show a welcome message.

# <codecell>

user_data = twitter.verify_credentials()
print "Welcome %s, your Twitter handle is @%s." % (user_data['name'], user_data['screen_name'])

print "Number of Tweets: ", user_data['statuses_count']
print "Number of followers: ", user_data['followers_count']
print "Unique Twitter ID: ", user_data['id']

# <codecell>


