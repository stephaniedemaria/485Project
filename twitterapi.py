import twitter

ipython

api = twitter.Api(consumer_key='6y72BDZ2J92EUpRDFdpkaNEKX',
consumer_secret='WIH6SoyIESgycaHm8Zr8jye3jcu54dWW9b9Bqbzs5cNrNhVV2w',
access_token_key='1118980620598808602-ezBC0CClGot06RNDPpdQ99WyG9RGfr',
access_token_secrets='INw7C24NJcyT0bFhIPnR3Y5LGvxr9PC1jSNHfPGhqve3T')

print(api.VerifyCredentials())

search = api.GetSearch("happy") # Replace happy with your search 
for tweet in search: 
    print(tweet.id, tweet.text)

t = api.GetUserTimeline(screen_name="RealDonaldTrump", count=10)

tweets = [i.AsDict() for i in t]

for t in tweets:
    print(t['id'], t['text'])