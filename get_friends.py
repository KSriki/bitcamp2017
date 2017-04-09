def get_friends_name_id(token):
    import json
    import pprint 
    from pprint import pprint
    import urllib2
    friends = {}
    link = "https://graph.facebook.com/me/friends?access_token="+token
    p = urllib2.urlopen(link).read()
    p1 = json.loads(p)
    for s in p1['data']:
        friends[s['name']] = s['id']
    while ('paging' in p) & ('next' in str(p1['paging'])):
        p = requests.get(p1['paging']['next']).text
        p1 = json.loads(p)
        for s in p1['data']:
            friends[s['name']] = s['id']
    print friends
    print len(friends)

get_friends_name_id("EAACEdEose0cBAKgncWRQFpjwutocv7INSHzZAVXYcKC7qwnLvFdEFdGnyehJCt06ZCTSEXJsSUmQLv7Ok84SnKxGCvgW17Uww7m38iBLVssbkRJQrKJLIxenDHG0IJZAdumy6UibNycl4XYllF2cedgdJFKM5STadZA7SDPfhfXZCbQJnpPDTK2OlQuG5uEDdBNeenibqCgZDZD")
