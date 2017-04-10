from flask import Flask, render_template
app = Flask(__name__)
# app.config['DEBUG'] = True

        
@app.route('/')
def run_page():
    unfollow_name = "TechCrunch"
    import tweepy
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
    
