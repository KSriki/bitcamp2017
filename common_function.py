from flask import Flask, render_template
app = Flask(__name__)
# app.config['DEBUG'] = True

        
@app.route('/')
def run_page():
    unfollow_name = "TechCrunch"
    import tweepy
    SCREEN_NAME = 'nisha131994'
    CONSUMER_KEY = '6zV5gjJa11GAosOQanfpkAmYs'
    CONSUMER_SECRET = 'DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f'
    ACCESS_TOKEN = '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt'
    ACCESS_TOKEN_SECRET = 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT'
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
        if unfollow_name in pk:
            o = "@"+ u.screen_name
            #print o
            suggestion.append(o)
    print len(suggestion)
    if len(suggestion) == 0:
        result = 'none'
    else:
        result = suggestion
    #result = twitter_user_suggestions('nisha131994',unfollow_name, '6zV5gjJa11GAosOQanfpkAmYs','DrbAdwlwg9ekezyIHOxAlGQIkITHhCoWFaY3EWbqjRVtrn9u3f', '136941431-mVOpaxVfdULOpRT26sbFli5CuxpVBooJkjTaYZWt', 'lfpjkJJvrgt9nt6OILVBgBlqZiPUydaq6QvdErIIXFFMT')
    if 'none' in result:
        print "Not found on Twitter"
    else:
        print "Here are some results, which one are you asking? Please enter username, if not listed."
        for r in result:
            print str(r)
        response = raw_input("enter input")
            #take_user_input_in_"input"
        #input = "@TechCrunch"
        api.destroy_friendship(response)
        api.create_friendship(response)  
    return render_template("templates/main.html")
    