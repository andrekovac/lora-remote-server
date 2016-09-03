import tweepy


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)


def tweet():
    # Fill in the values noted in previous step here
    cfg = {
        "consumer_key": "VALUE",
        "consumer_secret": "VALUE",
        "access_token": "VALUE",
        "access_token_secret": "VALUE"
    }

    api = get_api(cfg)
    tweet = "Hello, world!"
    return api.update_status(status=tweet)