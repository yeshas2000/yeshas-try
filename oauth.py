import oauth2 as oauth
import json

CONSUMER_KEY = 'RQrYRKr7z62F2Ha5rlw6Q'
CONSUMER_SECRET = 'DyJQhnz3vu9xTgYbyFHxUWfzBdExPInm3pXJmxXWXlc'
skey = '725538942-eb6oJr7wZlbbpum8qF4vVZqC6uh6OGwjkc4yP3C9'
ssecret = '1JjWlGDpbw8zqUQRqsbcGDohmXGawbpIHZDmYDg'


def oauth_req(url, http_method="GET", post_body='',
        http_headers=None):
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=skey, secret=ssecret)
    client = oauth.Client(consumer, token)
 
    resp, content = client.request(
        url,
        method=http_method,
        body=post_body,
        headers=http_headers,
        #force_auth_header
    )
    return content
 
home_timeline = oauth_req(
  'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=1'
)
print home_timeline
with open('data.txt', 'w') as outfile:
    json.dump(home_timeline, outfile)