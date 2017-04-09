def twitter_user_suggestions(SCREEN_NAME, unfollow_name, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    import tweepy
    #SCREEN_NAME = 'nisha131994'
    #CONSUMER_KEY = '6zV5gjJa11GAosOQanfpkAmYs'
    #CONSUMER_SECRET = 'DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f'
    #ACCESS_TOKEN = '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt'
    #ACCESS_TOKEN_SECRET = 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT'
    suggestion = []
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    followers = api.followers_ids(SCREEN_NAME)
    friends = api.friends_ids(SCREEN_NAME)
    for p in friends:
        u = api.get_user(p)
        pk = u.screen_name.lower()
        unfollow_name = unfollow_name.lower()
        #u2 = unfollow_name.split(" ")
        #print "Split names"
        #print u2
        if unfollow_name in pk:
            o = "@"+ u.screen_name
            #print o
            suggestion.append(o)
    print len(suggestion)
    if len(suggestion) == 0:
        return ['none']
    else:
        return suggestion

def twitter_unfollow(SCREEN_NAME, unfollow_name, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    import tweepy
    #SCREEN_NAME = 'nisha131994'
    #CONSUMER_KEY = '6zV5gjJa11GAosOQanfpkAmYs'
    #CONSUMER_SECRET = 'DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f'
    #ACCESS_TOKEN = '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt'
    #ACCESS_TOKEN_SECRET = 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT'
    suggestion = []
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    #unfollow_name
    api.destroy_friendship(unfollow_name)
    
def search_generator_and_unfollow(SCREEN_NAME, unfollow_name, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    result = twitter_user_suggestions('nisha131994',unfollow_name, '6zV5gjJa11GAosOQanfpkAmYs','DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f', '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt', 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT')
    if 'none' in result:
        print "Not found on Twitter"
    else:
        print "Here are some results, which one are you asking? Please enter username, if not listed."
        for r in result:
            print str(r)
        response = raw_input("enter input")
            #take_user_input_in_"input"
        input = "@TechCrunch"
            
        twitter_unfollow('nisha131994',response, '6zV5gjJa11GAosOQanfpkAmYs','DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f', '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt', 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT')
        return input
    
def revert_back(SCREEN_NAME, unfollow_name, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    import tweepy
    #SCREEN_NAME = 'nisha131994'
    #CONSUMER_KEY = '6zV5gjJa11GAosOQanfpkAmYs'
    #CONSUMER_SECRET = 'DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f'
    #ACCESS_TOKEN = '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt'
    #ACCESS_TOKEN_SECRET = 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT'
    suggestion = []
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.create_friendship(unfollow_name)
    
    
unfollowed_list = []
try:
    unfollowed = search_generator_and_unfollow('nisha131994','M', '6zV5gjJa11GAosOQanfpkAmYs','DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f', '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt', 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT')
    
    #revert_back('nisha131994',unfollowed, '6zV5gjJa11GAosOQanfpkAmYs','DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f', '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt', 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT')
except Exception as e:
    print "error"
    
