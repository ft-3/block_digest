import feedparser

channel_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UCb53lXz2IzEFT5JNHSbdvPg"
playlist_url = "https://www.youtube.com/feeds/videos.xml?playlist_id=PLbdPWjvnsOMyyce4oxRZWo2fmV9Dhg42p"

channel_feed = feedparser.parse(channel_url)
playlist_feed = feedparser.parse(playlist_url)

# for post in channel_feed.entries:
    # print("Title: ", post.title)
    # print("Description: ", post.description)

for post in playlist_feed.entries:
    print ("====================================================================")
    print ("====================================================================")
    print ("====================================================================")
    # print("Title: ", post.title)
    for entry in post:
        print(entry)
        if entry != 'summary':
            print(post[entry])
    print ("====================================================================")
    print ("====================================================================")
    print ("====================================================================")

