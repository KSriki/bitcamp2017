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
        print "unfollowed "+str(response)
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
    print "followed back"+str(response)
    #print "you paid about $"+money
    #return money
    

def sentiment(text, Emotion):
    try:
        Emotion = Emotion.lower()
        import urllib
        data = urllib.urlencode({"text": text}) 
        u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
        the_page = u.read()
        data = json.loads(the_page)
        if Emotion == 'positive':
            return data['probability']['pos']
        elif Emotion == 'negative':
            return data['probability']['neg']
        else:
            return data['probability']['neutral']
    except Exception as e:
        return 0
#print sentiment("hello", 'neg')
    
    
unfollowed_list = []
time = 0
money = 5
initial_amount = 0
response1 = raw_input("Enter how this person makes you feel?")
print("\n oh I see, dont worry, i am here!!!")
resp = raw_input("Whom do you want to ex-terminate?")
sent = sentiment(resp, 'neg') + 1
try:
    unfollowed = search_generator_and_unfollow('nisha131994',resp, '6zV5gjJa11GAosOQanfpkAmYs','DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f', '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt', 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT')
    print("Congratulations! You dont need that negativity in your life!")
    resp = raw_input("Are you having second thoughts ? Nooooooo !!!! ")
    see = (sent-1)*100
    print("Please dont! Remember last time you were unhappy about % "+str(see))
    print(response1)
    resp = raw_input("Do you still want to continue? ")
    if "yes" in resp.lower():
        money = money*sent
        print "you spent ="
        print money
        revert_back('nisha131994',unfollowed, '6zV5gjJa11GAosOQanfpkAmYs','DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f', '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt', 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT')
        
        
except Exception as e:
    pas
