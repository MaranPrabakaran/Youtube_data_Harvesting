#!/usr/bin/env python
# coding: utf-8

# In[37]:


from googleapiclient.discovery import build
import google.auth
import pandas as pd
import seaborn as sns


# In[38]:


api_key = 'AIzaSyASu2oPxYt7Qrt4hvujcNgr9DX3gtj-xuw'
channel_id_1 = "UCAiLfjNXkNv24uhpzUgPa6A" #mrbeast
channel_id_2 = "UCG7J20LhUeLl6y_Emi7OJrA" #MKBHD
channel_id_3 = "UCXv-co3EYHF7aOH4A93qAHQ" #unbox therapy
channel_id_4 = "UC9pRPRlo6wIOakEOi_2RWwA" #madan gowri
channel_id_5 = "UCMiJRAwDNSNzuYeN2uWa0pA" #mrwhosetheboss
channel_id_6 = "UCvrhwpnp2DHYQ1CbXby9ypQ" #vijaytv
channel_id_7 = "UCim0ZIz8SAQGPvg4mJHG3JA" #netflix india
channel_id_8 = "UC1Myj674wRVXB9I4c6Hm5zA" #apple
channel_id_9 = "UC56gTxNs4f9xZ7Pa2i5xNzg" #sony music south
channel_id_10 = "UChz5aEi3dfrDVC8-YJsMUDA" #T series

youtube = build('youtube','v3', developerKey=api_key)


# In[59]:


def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
                part='statistics',
                id=channel_id_10)
    response = request.execute()
    
    #data = dict(Channel_name = response['items'][0]['snippet']['title'],
                #Channel_Id = response['items'][0]['id'],
                #Subscription_Count = response['items'][0]['statistics']['subscriberCount'],
                #Channel_Views = response['items'][0]['statistics']['viewCount'],
                #Channel_Description = response['items'][0]['snippet']['description'])
    
    return response


get_channel_stats(youtube, id)


# ## Function to get channel statistics

# In[40]:


def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=channel_id_1)
    response = request.execute()
    
    #data = dict(Channel_name = response['items'][0]['snippet']['title'],
                #Channel_Id = response['items'][0]['id'],
                #Subscription_Count = response['items'][0]['statistics']['subscriberCount'],
                #Channel_Views = response['items'][0]['statistics']['viewCount'],
               # Channel_Description = response['items'][0]['snippet']['description'])
    
    return response


get_channel_stats(youtube, id)


# In[35]:


youtube = build("youtube", "v3", developerKey=api_key)

def get_latest_video_id(channel_id):
    # Request the channel's latest video
    search_response = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=1,  # Retrieve only the latest video
        order="date",  # Sort by date (latest first)
        type="video"  # Only retrieve videos
    ).execute()

    # Extract the video ID
    video_id = search_response["items"][0]["id"]["videoId"]

    return video_id

# Example usage
channel_id = "UC1Myj674wRVXB9I4c6Hm5zA"
latest_video_id = get_latest_video_id(channel_id)
print(latest_video_id)
video_Id = latest_video_id

def get_video_stats(youtube, video_Id):
    request = youtube.videos().list(
                part='snippet,statistics,contentDetails',
                id=video_Id)
    response = request.execute()
    
    data = dict(
                Video_Id = response['items'][0]['id'],
                Video_Name = response['items'][0]['snippet']['title'],
                Video_Discription = response['items'][0]['snippet']['description'],
                PublishedAt = response['items'][0]['snippet']['publishedAt'],
                View_Count = response['items'][0]['statistics']['viewCount'],
                Like_Count = response['items'][0]['statistics']['likeCount'],
                Favorite_Count = response['items'][0]['statistics']['favoriteCount'],
                #Comment_Count = response['items'][0]['statistics']['commentCount',0],
                Duration = response['items'][0]['contentDetails']['duration'],
                Thumbnail = response['items'][0]['snippet']['thumbnails']['default']['url'],
                Caption_Status = response['items'][0]['contentDetails']['caption']
            )
    
    return data
get_video_stats(youtube, video_Id)


# In[ ]:


video_Id = 'A6l764aNQKQ'
def get_comment_id(youtube, video_Id):
    # Request the comments for a specific video
    comments_request = youtube.commentThreads().list(
        part='id',
        videoId=video_Id
    )
    comments_response = comments_request.execute()
    
    # Extract the comment ID from the response
    comment_id = comments_response['items'][0]['id']
    
    return comment_id
get_comment_id(youtube, video_Id) 


# In[ ]:


comment_id = 'UgzKwmL-VC2cu0CjQch4AaABAg'
def get_comment_data(youtube, comment_id):
    # Request the comment data
    comment_request = youtube.comments().list(
        part='snippet',
        id=comment_id
    )
    comment_response = comment_request.execute()
    
    # Extract the desired data from the response
    comment_data = dict(
        Comment_Id = comment_response['items'][0]['id'],
        Comment_Text = comment_response['items'][0]['snippet']['textDisplay'],
        Comment_Author = comment_response['items'][0]['snippet']['authorDisplayName'],
        Comment_PublishedAt = comment_response['items'][0]['snippet']['publishedAt']
    )
    
    return comment_data
get_comment_data(youtube, comment_id)


# In[113]:


api_key = 'AIzaSyCc3ZbaIn9-uELQG8nUcQMq5_OiNYkZKy0'
video_Id2 = "qJBwk3SJeBw"

youtube = build('youtube','v3', developerKey=api_key)


# In[114]:


def get_video_stats(youtube, video_Id2):
    request = youtube.videos().list(
                part='snippet,statistics,contentDetails',
                id=video_Id2)
    response = request.execute()
    
    data = dict(
                Video_Id = response['items'][0]['id'],
                Video_Name = response['items'][0]['snippet']['title'],
                Video_Discription = response['items'][0]['snippet']['description'],
                PublishedAt = response['items'][0]['snippet']['publishedAt'],
                View_Count = response['items'][0]['statistics']['viewCount'],
                Like_Count = response['items'][0]['statistics']['likeCount'],
                Favorite_Count = response['items'][0]['statistics']['favoriteCount'],
                Comment_Count = response['items'][0]['statistics']['commentCount'],
                Duration = response['items'][0]['contentDetails']['duration'],
                Thumbnail = response['items'][0]['snippet']['thumbnails']['default']['url'],
                Caption_Status = response['items'][0]['contentDetails']['caption']
            )
    
    return data
get_video_stats(youtube, video_Id2)


# In[116]:


get_ipython().system('pip install pymongo')


# In[66]:


from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['mydatabase']
collection = db['youtube_data']


# In[74]:


channel = [
{
    'Channel_Name_1': {
        'Channel_name': 'Beast Philanthropy',
        'Channel_Id': 'UCAiLfjNXkNv24uhpzUgPa6A',
        'Subscription_Count': '14300000',
        'Channel_Views': '255564524',
        'Channel_Description': '100% of the profits from my ad revenue, merch sales, and sponsorships will go towards making the world a better place!'
    },
    'Channel_Name_2':{
         'Channel_name': 'The Studio',
         'Channel_Id': 'UCG7J20LhUeLl6y_Emi7OJrA',
         'Subscription_Count': '755000',
         'Channel_Views': '32377656',
         'Channel_Description': 'Behind-the-scenes content, event reactions, challenges, and more from the MKBHD Studio!'
         },
    'Channel_Name_3':{
         'Channel_name': 'Lew Later',
         'Channel_Id': 'UCXv-co3EYHF7aOH4A93qAHQ',
         'Subscription_Count': '838000',
         'Channel_Views': '92849049',
         'Channel_Description': 'Lew... Later'
    },
    'channel_name_4':{
         'Channel_name': 'MG X',
         'Channel_Id': 'UC9pRPRlo6wIOakEOi_2RWwA',
         'Subscription_Count': '318000',
         'Channel_Views': '3582572',
         'Channel_Description': "Welcome to the Madan Gowri Podcast, where insightful conversations and captivating stories come to life. Join Madan Gowri, the renowned Tamil YouTuber, as he delves deep into a myriad of topics, exploring thought-provoking ideas, and sharing inspiring tales. Through engaging interviews, thoughtfully crafted narratives, and thought-provoking discussions, Madan Gowri invites you on a journey of discovery and enlightenment. Whether you're seeking inspiration, knowledge, or simply a moment of reflection, this podcast is your gateway to a world of fascinating stories and ideas. Subscribe now and join the community of curious minds, embarking on a transformative journey of intellectual exploration and personal growth.\n\n Subscribe to the Madan Gowri Podcast now and get ready to be inspired, informed, and entertained as you navigate the depths of human knowledge and the wonders of the world through the power of audio storytelling.\n\n\n\n"
    },
    'channel_name_5':{
         'Channel_name': 'Mrwhosetheboss',
         'Channel_Id': 'UCMiJRAwDNSNzuYeN2uWa0pA',
         'Subscription_Count': '15300000',
         'Channel_Views': '3685776827',
         'Channel_Description': "Let's become the Greatest Tech Community on the Planet 🌍\n\nI'm Arun Maini, I'm a 27 year old Economics graduate whose life's passion is Technology, and I'm on a mission to make the most FUN and USEFUL Tech videos on the Planet! 🙏\n\n\n\n"
    },
    'channel_name_6':{
         'Channel_name': 'Vijay Television',
         'Channel_Id': 'UCvrhwpnp2DHYQ1CbXby9ypQ',
         'Subscription_Count': '20200000',
         'Channel_Views': '29115308110',
         'Channel_Description': 'Vijay Television ("Vijay") is a leading Tamil Language Entertainment Channel broadcasting innovative shows & programs from India.  Vijay TV is part of the STAR network and is commonly referred to as STAR VIJAY.'
    },
    'channel_name_7':{
         'Channel_name': 'Netflix India Shorts',
         'Channel_Id': 'UCim0ZIz8SAQGPvg4mJHG3JA',
         'Subscription_Count': '571000',
         'Channel_Views': '497532424',
         'Channel_Description': 'Long story short, this channel is where you can find everything we have to share about your favourite Netflix films and series in under 60 seconds.'
    },
    'channel_name_8':{
         'Channel_name': 'Apple TV',
         'Channel_Id': 'UC1Myj674wRVXB9I4c6Hm5zA',
         'Subscription_Count': '1460000',
         'Channel_Views': '943805356',
         'Channel_Description': 'Your next favorite story is waiting. Discover the best movies, series, and shows on the Apple TV app. \n\nApple TV+ is a streaming service with original stories from the most creative minds in TV and film. Watch now on the Apple TV app: https://apple.co/_AppleTVapp\n'
    },
    'channel_name_9':{
         'Channel_name': 'Sony Music India',
         'Channel_Id': 'UC56gTxNs4f9xZ7Pa2i5xNzg',
         'Subscription_Count': '57100000',
         'Channel_Views': '28749287665',
         'Channel_Description': "Sony Music India - Home To India's Biggest Music Hits. Subscribe to our channel to listen to chartbusters in the making, see premieres of blockbuster videos and get your daily dose of some great music right here."
    },
     'channel_name_10':{
         'Channel_name': 'T-Series Kids Hut',
         'Channel_Id': 'UChz5aEi3dfrDVC8-YJsMUDA',
         'Subscription_Count': '2920000',
         'Channel_Views': '1014139023',
         'Channel_Description': 'Kids Hut Channel is filled with all the popular NURSERY RHYMES, BEDTIME STORIES & THINGS YOU(KIDS) WANT TO KNOW. All The Voice Over Of The Channel Are Done By Renowned Bollywood Singer Tulsi Kumar. Popular Nursery Rhyme Characters comes alive to make you kids sing and dance, there is a new adventure to find with Tia and Tofu every time you visit Kids Hut. Tia and Tofu are all set to take you on this adventure trip to the Magical Place called Kids Hut, Join Kids Hut and be a part of our Kids Hut Family.'
     }
}
]

video = [
{
    'Video_Id_1': {
        'Video_Id': 'C680oxL__ck',
        'Video_Name': 'I Ate $100,000 Golden Ice Cream',
        'Video_Discription': 'I cant believe how insane that ice cream looked at the end\nNew Merch - https://shopmrbeast.com/\n\nSUBSCRIBE OR I TAKE YOUR DOG\n╔═╦╗╔╦╗╔═╦═╦╦╦╦╗╔═╗\n║╚╣║║║╚╣╚╣╔╣╔╣║╚╣═╣ \n╠╗║╚╝║║╠╗║╚╣║║║║║═╣\n╚═╩══╩═╩═╩═╩╝╚╩═╩═╝\n\n----------------------------------------------------------------\nfollow all of these or i will kick you\n• Facebook - https://www.facebook.com/MrBeast6000/\n• Twitter - https://twitter.com/MrBeast\n• Instagram - https://www.instagram.com/mrbeast\n--------------------------------------------------------------------',
        'PublishedAt': '2021-01-22T21:00:03Z',
        'View_Count': '203156455',
        'Like_Count': '5229019',
        'Favorite_Count': '0',
        'Comment_Count': '175256',
        'Duration': 'PT13M17S',
        'Thumbnail': 'https://i.ytimg.com/vi/C680oxL__ck/default.jpg',
        'Caption_Status': 'true'
        
    },
    'Video_Id_2':{
         'Video_Id': 'bRqZe0el4kQ',
         'Video_Name': 'We Fixed Our BIGGEST Mistake!',
         'Video_Discription': "The Motocrane had incredible potential, but we might have been a bit overly ambitious with regards to permits and location scouting. Our new rig for shooting car reviews is smaller, quicker to set up, and draws less attention.\n\nThanks to Hollyland for sponsoring this video! Check out the Lark Max and get 15% off everything on the store with code STUDIO15 at https://geni.us/HxLy for 30 days\n\nCheck out Motocrane's Radical at https://geni.us/TCfH\nKessler KillShock at https://geni.us/Qpqv\nDJI Ronin 2 at https://geni.us/KrWEv8W \nRED V-RAPTOR XL at https://geni.us/qURCX \nTilta Nucleus-M Lens Control at https://geni.us/XxeygGH \nTeradek Bolt 4K at https://geni.us/DvRW4IL \nSmallHD 1303 HDR Monitor at https://geni.us/yApOIi \nCineMilled Control Panel at https://geni.us/F2sJPU1\n~\nShop the merch:\nhttps://shop.mkbhd.com\n\nJoin the Discord:\nhttps://discord.gg/mkbhd\n\nMusic licensed from Epidemic Sound:\nhttps://www.epidemicsound.com/referral/8m00ja\n\nFollow The Studio:\nhttps://twitter.com/TheStudio\nhttps://www.instagram.com/thestudio/\n\nFollow the staff:\nMarques Brownlee https://twitter.com/MKBHD\nAdam Molina https://twitter.com/AdamLukas17\nAlex Wolfe https://twitter.com/thealexwolfe\nAndrew Manganelli https://twitter.com/AndyManganelli\nBrandon Havard https://twitter.com/b_hvrd\nDavid Imel https://twitter.com/DurvidImel\nEllis Rovin https://twitter.com/ellisrovin\nHayato Huseman https://twitter.com/hayatohuseman\nJono Tan https://twitter.com/jonotan86\nMariah Zenk https://www.instagram.com/totallynotabusinessacc/\nMichael Emerick https://twitter.com/Mikey_Emerick\nMiles Somerville https://twitter.com/SomeOfMiles\nTim McMahon https://twitter.com/timmcmahonn\nVinh Dang https://twitter.com/danggvinh\n\nEquipment used in this video and others:\nCanon EOS C70: https://geni.us/AtpxW\nCanon RF 15-35mm f/2.8L: https://howl.me/chHqd63eV8A\nCanon RF 28-70mm f/2.8L: https://geni.us/Tbimi\nSennheiser MKH-416: https://geni.us/jYxRVj\nSennheiser ME 2 lav: https://geni.us/0bpKiZX\nPowerDeWise lav: https://geni.us/SRX1Th\nZoom F8n Pro: https://geni.us/tuv7o8\nHollyland Lark Max: https://geni.us/mkJRt7\n\nShot by Miles Somerville, Jono Tan, and Hayato Huseman\nProduced by Miles Somerville, Vinh Dang, and Brandon Havard\nColor by Vinh Dang\nAudio by Ellis Rovin\nGraphics by Tim McMahon and Michael Emerick",
         'PublishedAt': '2023-06-28T19:00:00Z',
         'View_Count': '123770',
         'Like_Count': '10285',
         'Favorite_Count': '0',
         'Comment_Count': '341',
         'Duration': 'PT8M46S',
         'Thumbnail': 'https://i.ytimg.com/vi/bRqZe0el4kQ/default.jpg',
         'Caption_Status': 'true'
    },
    'Video_Id_3':{
         'Video_Id': 'D3y2h-LhCKw',
         'Video_Name': 'Elon Finally Said It...',
         'Video_Discription': 'Subscribe for more internet + tech news.\nCheck out LaterClips for quicker news - https://www.youtube.com/laterclips\n---\nEmail questions to will [at] lewlater dot com\nhttps://twitter.com/lewlater',
         'PublishedAt': '2023-05-12T16:56:43Z',
         'View_Count': '34816',
         'Like_Count': '1139',
         'Favorite_Count': '0',
         'Comment_Count': '315',
         'Duration': 'PT48M49S',
         'Thumbnail': 'https://i.ytimg.com/vi/D3y2h-LhCKw/default.jpg',
         'Caption_Status': 'false'
    },
    'Video_Id_4':{
         'Video_Id': 'nEzxj58fz1I',
         'Video_Name': 'Gautham on Parents and Separation | Madan Gowri x',
         'Video_Discription': "📧 For Business: work.madangowri@outlook.com\n-------------\nMy Gadgets and Books: https://www.amazon.in/shop/madangowri\n-------------\nGautham Karthik gets on a podcast with MADAN GOWRI IN MG X. \n\nWatch the full episode here: https://youtu.be/4cNdeSRuEwY\n\nIn this video hosted by Madan Gowri, join us as we dive into a heartfelt conversation with the talented actor Gautham Karthik. \n\nFrom professional growth to personal transformation, GK shares candidly about the ways in which Manjima's presence and influence have shaped his journey. \n\nDon't miss the inspiring discussion that explores the power of connections and the potential for profound change in an individual. \n\nAbout MG X\n\nMG X is a channel where we show you exclusive clips of the podcast. We invite important guests from various fields to reveal their hidden alter egos, showcasing their passions, talents, and untapped potential.",
         'PublishedAt': '2023-07-02T05:18:04Z',
         'View_Count': '890',
         'Like_Count': '84',
         'Favorite_Count': '0',
         'Comment_Count': '6',
         'Duration': 'PT4M59S',
         'Thumbnail': 'https://i.ytimg.com/vi/nEzxj58fz1I/default.jpg',
         'Caption_Status': 'false'
    },
    'Video_Id_5':{
         'Video_Id': 'kMiy8ZywF88',
         'Video_Name': 'I bought the most EXPENSIVE Tech on the internet.',
         'Video_Discription': "It's always fun to treat your parents 😁\nGet an exclusive Surfshark deal! Enter promo code BOSS for an extra 3 months free at https://surfshark.deals/BOSS\n\nI spend a LOT of time trying to make my videos as concise, polished and useful as possible for you - if you would like to support me on that mission then consider subscribing to the channel - you'd make my day 😁\n\nFor my tech hot takes: http://twitter.com/Mrwhosetheboss\nFor my Personal Posts: http://instagram.com/mrwhosetheboss\nDoes anyone still use this anymore?: https://facebook.com/mrwhosetheboss\n\nAmazon Affiliate links (if you buy anything through these it will support the channel and allow us to buy better gear!):\nAmazon US: https://amzn.to/3mFix9d\nAmazon UK: https://amzn.to/3GMPPtM\n\nMy Filming Gear:\nhttps://bit.ly/35CuxwI\n\nMusic is from Epidemic sound:\nhttp://share.epidemicsound.com/pHDFT",
         'PublishedAt': '2023-07-01T11:03:16Z',
         'View_Count': '1914816',
         'Like_Count': '117180',
         'Favorite_Count': '0',
         'Comment_Count': '5470',
         'Duration': 'PT28M1S',
         'Thumbnail': 'https://i.ytimg.com/vi/kMiy8ZywF88/default.jpg',
         'Caption_Status': 'false'
    },
    'Video_Id_6':{
         'Video_Id': 'OKF4eInPStI',
         'Video_Name': 'Chellamma | 3rd to 8th July 2023 - Promo',
         'Video_Discription': 'செல்லம்மா - திங்கள் முதல் சனி வரை மதியம் 2 மணிக்கு நம்ம விஜய் டிவில.. Click here to watch - https://www.hotstar.com/in/tv/chellamma/1260101194      #Chellamma #VijayTV #VijayTelevision #StarVijayTV #StarVijay #TamilTV',
         'PublishedAt': '2023-07-02T04:30:07Z',
         'View_Count': '224767',
         'Like_Count': '9362',
         'Favorite_Count': '0',
         'Comment_Count': '57',
         'Duration': 'PT50S',
         'Thumbnail': 'https://i.ytimg.com/vi/OKF4eInPStI/default.jpg',
         'Caption_Status': 'false'
    },
    'Video_Id_7':{
         'Video_Id': 'hscUboV-hzM',
         'Video_Name': 'Tamannaah and Vijay Reunited | #LustStories2 #Shorts',
         'Video_Discription': 'What would you do if you ever come across your ex? \r\n\r\nWatch Lust Stories 2, now streaming only on Netflix!\r\n\r\nFollow Netflix India on:\r\nWebsite: https://www.netflix.com/\r\nYouTube: http://bit.ly/NetflixIndiaYT\r\nInstagram: http://www.instagram.com/netflix_in\r\nFacebook: http://www.facebook.com/NetflixIN\r\nTwitter: http://twitter.com/netflixindia\r\n\r\n#NetflixIndia #NetflixIndiaShorts #LustStories2',
         'PublishedAt': '2023-07-01T13:30:00Z',
         'View_Count': '5724',
         'Like_Count': '274',
         'Favorite_Count': '0',
         'Comment_Count': '2',
         'Duration': 'PT24S',
         'Thumbnail': 'https://i.ytimg.com/vi/hscUboV-hzM/default.jpg',
         'Caption_Status': 'false'
    },
    'Video_Id_8':{
         'Video_Id': 'QQ6x6NjVM_E',
         'Video_Name': 'Silo — An Inside Look | Apple TV+',
         'Video_Discription': 'Get a behind the scenes look from the cast and crew. Silo is now streaming on Apple TV+ https://apple.co/_Silo\n\nIn a ruined and toxic future, thousands live in a giant silo deep underground. After its sheriff breaks a cardinal rule and residents die mysteriously, engineer Juliette (Rebecca Ferguson) starts to uncover shocking secrets and the truth about the silo. \n\nSubscribe to Apple TV’s YouTube channel: https://apple.co/AppleTVYouTube\n\nFollow Apple TV:\nInstagram: https://instagram.com/AppleTV\nFacebook: https://facebook.com/AppleTV\nTwitter: https://twitter.com/AppleTV\nGiphy: https://giphy.com/AppleTV\n\nMore from Apple TV: https://apple.co/32qgOEJ\n\nApple TV+ is a streaming service with original stories from the most creative minds in TV and film. Watch now on the Apple TV app: https://apple.co/_AppleTVapp Subscription required for Apple TV+\n\n#Silo #Clip #AppleTV',
         'PublishedAt': '2023-06-30T16:59:46Z',
         'View_Count': '32506',
         'Like_Count': '1515',
         'Favorite_Count': '0',
         'Comment_Count': '0',
         'Duration': 'PT2M9S',
         'Thumbnail': 'https://i.ytimg.com/vi/QQ6x6NjVM_E/default.jpg',
         'Caption_Status': 'true'
    },
    'Video_Id_9':{
         'Video_Id': '2MiuxsDOQqw',
         'Video_Name': 'I hare love story',
         'Video_Discription': '',
         'PublishedAt': '2023-07-01T10:05:41Z',
         'View_Count': '13397',
         'Like_Count': '516',
         'Favorite_Count': '0',
         'Comment_Count': '9',
         'Duration': 'PT55S',
         'Thumbnail': 'https://i.ytimg.com/vi/2MiuxsDOQqw/default.jpg',
         'Caption_Status': 'false'
    },
    'Video_Id_10':{
         'Video_Id': 'A6l764aNQKQ',
         'Video_Name': 'Moral Stories for Kids | Tia & Tofu | Bedtime Stories for Kids | English Stories for Kids',
         'Video_Discription': 'Kids Hut family presents "Moral Stories for Kids" by KIDS HUT.\n\n1.       Being Street Smart \n2.       Tale of Greedy Gloria \n3.       When Adversity Knocks\n \n#bedtimestories #kidsvideos #englishkidsvideos #kidsstories \n\n-------------------------------------\nNEW UPLOADS COLLECTION ► http://bit.ly/1TTDl6r\n-------------------------------------\n✿ Voice Credit: Tulsi Kumar\n--------------------------------------\n\n\n★ SUBSCRIBE us on YOUTUBE: http://bit.ly/1qsHVca\n★ LIKE us on FACEBOOK: https://www.facebook.com/kidshut\n★ FOLLOW us on TWITTER: https://twitter.com/kids_hut\n★ FOLLOW us on PINTEREST: http://www.pinterest.com/kidshut\n\n--------------------------------------\n\nNOW BUY,\xa0KIDS HUT’S FUN LEARNING GIFT PACK, WHICH INCLUDES DVD\'s OF RHYMES AND STORIES, MAGIC BOOK, COLORING BOOK, CRAYONS AND TIA-TOFU MAGNET.',
         'PublishedAt': '2023-06-30T12:30:04Z',
         'View_Count': '16772',
         'Like_Count': '120',
         'Favorite_Count': '0',
         'Comment_Count': '0',
         'Duration': 'PT15M47S',
         'Thumbnail': 'https://i.ytimg.com/vi/A6l764aNQKQ/default.jpg',
         'Caption_Status': 'false'
    }
}
]

comments = [ 
{
    'Comment_Id_1':{
         'Comment_Id': 'UgwYhRcoyPO3I-xkE9B4AaABAg',
         'Comment_Text': 'I love all of you :)',
         'Comment_Author': 'MrBeast',
         'Comment_PublishedAt': '2021-01-22T21:04:41Z'
        },
    'Comment_Id_2':{
         'Comment_Id': 'Ugy6T0WtKfeFJBlV53Z4AaABAg',
         'Comment_Text': 'What if it&#39;s raining? Will this setup work?',
         'Comment_Author': 'Ronak Rathod',
         'Comment_PublishedAt': '2023-07-02T03:53:33Z'
    },
    'Comment_Id_3':{
         'Comment_Id': 'UgxYI-DpzrW3Qz5F2Vp4AaABAg',
         'Comment_Text': 'Imagine building a community and then abandoning it',
         'Comment_Author': 'NickS',
         'Comment_PublishedAt': '2023-06-30T01:20:38Z'
    },
    'Comment_Id_4':{
         'Comment_Id': 'UgyNkAQ4Mg6bfnyKbR94AaABAg',
         'Comment_Text': 'Best wishes brothers.....❤🎉🎉🎉',
         'Comment_Author': 'Shy Ebi',
         'Comment_PublishedAt': '2023-07-02T07:01:56Z'
    },
    'Comment_Id_5':{
         'Comment_Id': 'Ugw095NMNzCFhr6JL6h4AaABAg',
         'Comment_Text': 'It&#39;s always fun to treat your parents 😊  (also to be VERY clear, I made a loss on this video, so if you did enjoy it, please subscribe ❤)<br>To see me buy the most CURSED Tech on the internet: <a href="https://youtu.be/nF_YtQkcyAM">https://youtu.be/nF_YtQkcyAM</a><br>Or to see me test the world&#39;s Cheapest Gaming Setup vs the most Expensive: <a href="https://youtu.be/QOfGZC6xEb8">https://youtu.be/QOfGZC6xEb8</a>',
         'Comment_Author': 'Mrwhosetheboss',
         'Comment_PublishedAt': '2023-07-01T11:05:38Z'
    },
    'Comment_Id_6':{
         'Comment_Id': 'UgypaWklHKU5WECUxXR4AaABAg',
         'Comment_Text': 'Saniyan intha saniyana paththaley kudumbatha pricha nai😡😡😡',
         'Comment_Author': 'Kavisara Kavisara',
         'Comment_PublishedAt': '2023-07-02T07:10:00Z'
    },
    'Comment_Id_7':{
         'Comment_Id': 'Ugw8uz0e73InKo5l43x4AaABAg',
         'Comment_Text': 'This part was not good only 2nd story among these were good',
         'Comment_Author': 'Gimox',
         'Comment_PublishedAt': '2023-07-02T07:07:48Z'
    },
    'Comment_Id_8':{
         'Comment_Id': 'null',
         'Comment_Text': 'null',
         'Comment_Author': 'null',
         'Comment_PublishedAt': 'null'
    },
    'Comment_Id_9':{
         'Comment_Id': 'UgzKwmL-VC2cu0CjQch4AaABAg',
         'Comment_Text': 'Lovely songs. And Bin tere too',
         'Comment_Author': 'rishabh',
         'Comment_PublishedAt': '2023-07-01T20:09:33Z'
    },
    'Comment_Id_10':{
         'Comment_Id': 'null',
         'Comment_Text': 'null',
         'Comment_Author': 'null',
         'Comment_PublishedAt': 'null'
    }
}
]


result = collection.insert_many(video)
result.inserted_ids


# In[7]:


import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="12345",database="youtube_data",auth_plugin='mysql_native_password')


# In[21]:


mycursor = mydb.cursor()
mycursor.execute("show tables")
for table in mycursor:
    print(table)


# In[13]:


mycursor.execute("insert into channel (sl_no,Channel_name,Channel_Id,Subscription_Count,Channel_Views,Channel_Description) values (1,'Beast Philanthropy','UCAiLfjNXkNv24uhpzUgPa6A','14300000','255564524','100% of the profits from my ad revenue, merch sales, and sponsorships will go towards making the world a better place!')")
mydb.commit()


# In[ ]:


mycursor.execute("insert into comment (sl_no,Comment_Id,Comment_Text,Comment_Author,Comment_PublishedAt) values (1,'UgwYhRcoyPO3I-xkE9B4AaABAg','I love all of you :)','MrBeast','2021-01-22T21:04:41Z')")
mydb.commit()


# In[31]:


channel_data = {
             'sl_no': '10',
             'Channel_name': 'T-Series Kids Hut',
             'Channel_Id': 'UChz5aEi3dfrDVC8-YJsMUDA',
             'Subscription_Count': '2920000',
             'Channel_Views': '1014139023',
             'Channel_Description': 'Kids Hut Channel is filled with all the popular NURSERY RHYMES, BEDTIME STORIES & THINGS YOU(KIDS) WANT TO KNOW. All The Voice Over Of The Channel Are Done By Renowned Bollywood Singer Tulsi Kumar. Popular Nursery Rhyme Characters comes alive to make you kids sing and dance, there is a new adventure to find with Tia and Tofu every time you visit Kids Hut. Tia and Tofu are all set to take you on this adventure trip to the Magical Place called Kids Hut, Join Kids Hut and be a part of our Kids Hut Family.'
         }


channel_query = "INSERT INTO channel (sl_no, Channel_name, Channel_Id, Subscription_Count, Channel_Views, Channel_Description) VALUES (%s, %s, %s, %s, %s, %s)"
channel_values = [channel_data[key] for key in ['sl_no', 'Channel_name', 'Channel_Id', 'Subscription_Count', 'Channel_Views',
                                            'Channel_Description']]

mycursor.execute(channel_query, channel_values)

mydb.commit()


# In[ ]:


comment_data = {
             'sl_no': '10',
             'Channel_name': 'T-Series Kids Hut',
             'Channel_Id': 'UChz5aEi3dfrDVC8-YJsMUDA',
             'Subscription_Count': '2920000',
             'Channel_Views': '1014139023',
             'Channel_Description': 'Kids Hut Channel is filled with all the popular NURSERY RHYMES, BEDTIME STORIES & THINGS YOU(KIDS) WANT TO KNOW. All The Voice Over Of The Channel Are Done By Renowned Bollywood Singer Tulsi Kumar. Popular Nursery Rhyme Characters comes alive to make you kids sing and dance, there is a new adventure to find with Tia and Tofu every time you visit Kids Hut. Tia and Tofu are all set to take you on this adventure trip to the Magical Place called Kids Hut, Join Kids Hut and be a part of our Kids Hut Family.'
         }


channel_query = "INSERT INTO channel (sl_no, Channel_name, Channel_Id, Subscription_Count, Channel_Views, Channel_Description) VALUES (%s, %s, %s, %s, %s, %s)"
channel_values = [channel_data[key] for key in ['sl_no', 'Channel_name', 'Channel_Id', 'Subscription_Count', 'Channel_Views',
                                            'Channel_Description']]

mycursor.execute(channel_query, channel_values)

mydb.commit()


# In[4]:


comments = [
    {
             'sl_no': '2',
             'Comment_Id': 'Ugy6T0WtKfeFJBlV53Z4AaABAg',
             'Comment_Text': 'What if it&#39;s raining? Will this setup work?',
             'Comment_Author': 'Ronak Rathod',
             'Comment_PublishedAt': '2023-07-02T03:53:33Z'
        },
        {
             'sl_no': '3',
             'Comment_Id': 'UgxYI-DpzrW3Qz5F2Vp4AaABAg',
             'Comment_Text': 'Imagine building a community and then abandoning it',
             'Comment_Author': 'NickS',
             'Comment_PublishedAt': '2023-06-30T01:20:38Z'
        },
        {
             'sl_no': '4',
             'Comment_Id': 'UgyNkAQ4Mg6bfnyKbR94AaABAg',
             'Comment_Text': 'Best wishes brothers.....❤🎉🎉🎉',
             'Comment_Author': 'Shy Ebi',
             'Comment_PublishedAt': '2023-07-02T07:01:56Z'
        },
        {
             'sl_no': '5',
             'Comment_Id': 'Ugw095NMNzCFhr6JL6h4AaABAg',
             'Comment_Text': 'It&#39;s always fun to treat your parents 😊  (also to be VERY clear, I made a loss on this video, so if you did enjoy it, please subscribe ❤)<br>To see me buy the most CURSED Tech on the internet: <a href="https://youtu.be/nF_YtQkcyAM">https://youtu.be/nF_YtQkcyAM</a><br>Or to see me test the world&#39;s Cheapest Gaming Setup vs the most Expensive: <a href="https://youtu.be/QOfGZC6xEb8">https://youtu.be/QOfGZC6xEb8</a>',
             'Comment_Author': 'Mrwhosetheboss',
             'Comment_PublishedAt': '2023-07-01T11:05:38Z'
        },
        {
             'sl_no': '6',
             'Comment_Id': 'UgypaWklHKU5WECUxXR4AaABAg',
             'Comment_Text': 'Saniyan intha saniyana paththaley kudumbatha pricha nai😡😡😡',
             'Comment_Author': 'Kavisara Kavisara',
             'Comment_PublishedAt': '2023-07-02T07:10:00Z'
        },
        {
             'sl_no': '7',
             'Comment_Id': 'Ugw8uz0e73InKo5l43x4AaABAg',
             'Comment_Text': 'This part was not good only 2nd story among these were good',
             'Comment_Author': 'Gimox',
             'Comment_PublishedAt': '2023-07-02T07:07:48Z'
        },
        {
             'sl_no': '8',
             'Comment_Id': 'null',
             'Comment_Text': 'null',
             'Comment_Author': 'null',
             'Comment_PublishedAt': 'null'
        },
        {
             'sl_no': '9',
             'Comment_Id': 'UgzKwmL-VC2cu0CjQch4AaABAg',
             'Comment_Text': 'Lovely songs. And Bin tere too',
             'Comment_Author': 'rishabh',
             'Comment_PublishedAt': '2023-07-01T20:09:33Z'
        },
        {
             'sl_no': '10',
             'Comment_Id': 'null',
             'Comment_Text': 'null',
             'Comment_Author': 'null',
             'Comment_PublishedAt': 'null'
        }
    
]
        

comment_query = "INSERT INTO comment (sl_no, comment_id, comment_text, comment_author, comment_publishedat) VALUES (%s, %s, %s, %s, %s)"

for comment_data in comments:
    comment_values = list(comment_data.values())
    mycursor.execute(comment_query, comment_values)

# Commit the changes to the database
mydb.commit()

# Close the cursor and database connection
mycursor.close()
mydb.close()


# In[11]:


get_ipython().system('pip install mysql-connector-python')


# In[13]:


get_ipython().system('pip install pymysql')


# In[14]:


import sqlalchemy
import pymysql

# Set the MySQL dialect to pymysql
pymysql.install_as_MySQLdb()

engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')


# In[15]:


engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:12345@localhost:3306/youtube_data')


# In[86]:


import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')
connection = engine.connect()

# Define the tables you want to join
channels_table = sqlalchemy.Table('channel', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
videos_table = sqlalchemy.Table('video', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
comments_table = sqlalchemy.Table('comment', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)


# In[28]:


query = sqlalchemy.select([videos_table.c.video_name, channels_table.c.channel_name]).\
    select_from(videos_table.join(channels_table, videos_table.c.sl_no == channels_table.c.sl_no))

result = connection.execute(query)
for row in result:
    video_name = row.video_name
    channel_name = row.channel_name
    print("Video Name:", video_name)
    print("Channel Name:", channel_name)
    print()

# Close the database connection
connection.close()



# In[63]:


# Construct the query
query = sqlalchemy.select([channels_table.c.channel_name, channels_table.c.video_count]).\
    order_by(channels_table.c.video_count.desc()).\
    limit(1)

# Execute the query
result = connection.execute(query)

# Fetch the results
row = result.fetchone()
channel_name = row.channel_name
video_count = row.video_count

# Close the database connection
connection.close()

# Print the result
print(f"The channel '{channel_name}' has the most number of videos with a count of {video_count}.")


# In[66]:


from sqlalchemy import create_engine, select, desc

# Create the engine and establish a connection
engine = create_engine('mysql://root:12345@localhost:3306/youtube_data')
connection = engine.connect()

# Construct the query
query = select([videos_table.c.video_name, channels_table.c.channel_name]).\
    select_from(videos_table.join(channels_table, videos_table.c.sl_no == channels_table.c.sl_no)).\
    order_by(desc(videos_table.c.view_count)).\
    limit(10)

# Execute the query
result = connection.execute(query)

# Fetch the results
for row in result:
    video_name = row.video_name
    channel_name = row.channel_name
    print(f"Video Name: {video_name}, Channel Name: {channel_name}")

# Close the connection
connection.close()



# In[69]:


import sqlalchemy

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')

# Create a connection
connection = engine.connect()

# Construct the query
query = sqlalchemy.select([videos_table.c.video_name, videos_table.c.comment_count])

# Execute the query
result = connection.execute(query)

# Fetch the results
for row in result:
    video_name = row.video_name
    comment_count = row.comment_count
    print(f"Video Name: {video_name}, Comment Count: {comment_count}")

# Close the connection
connection.close()


# In[75]:


import sqlalchemy

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')

# Create a connection
connection = engine.connect()

# Define the tables
videos_table = sqlalchemy.Table('video', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
channels_table = sqlalchemy.Table('channel', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)

# Construct the query
query = sqlalchemy.select([videos_table.c.video_name, channels_table.c.channel_name, videos_table.c.like_count]).\
        select_from(videos_table.join(channels_table, videos_table.c.sl_no == channels_table.c.sl_no)).\
        order_by(videos_table.c.like_count.desc()).\
        limit(10)

# Execute the query
result = connection.execute(query)

# Fetch the results
for row in result:
    video_name = row.video_name
    channel_name = row.channel_name
    like_count = row.like_count
    print(f"Video Name: {video_name}, Channel Name: {channel_name}, Like Count: {like_count}")

# Close the connection
connection.close()


# In[76]:


import sqlalchemy

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')

# Create a connection
connection = engine.connect()

# Define the tables
videos_table = sqlalchemy.Table('video', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)

# Construct the query
query = sqlalchemy.select([videos_table.c.video_name, sqlalchemy.func.sum(videos_table.c.like_count).label('total_likes')]).\
        group_by(videos_table.c.video_name)

# Execute the query
result = connection.execute(query)

# Fetch the results
for row in result:
    video_name = row.video_name
    total_likes = row.total_likes
    print(f"Video Name: {video_name}, Total Likes: {total_likes}")

# Close the connection
connection.close()


# In[77]:


import sqlalchemy

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')

# Create a connection
connection = engine.connect()

# Define the tables
channels_table = sqlalchemy.Table('channel', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
videos_table = sqlalchemy.Table('video', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)

# Construct the query
query = sqlalchemy.select([channels_table.c.channel_name, sqlalchemy.func.sum(videos_table.c.view_count).label('total_views')]).\
        select_from(channels_table.join(videos_table, channels_table.c.sl_no == videos_table.c.sl_no)).\
        group_by(channels_table.c.channel_name)

# Execute the query
result = connection.execute(query)

# Fetch the results
for row in result:
    channel_name = row.channel_name
    total_views = row.total_views
    print(f"Channel Name: {channel_name}, Total Views: {total_views}")

# Close the connection
connection.close()


# In[87]:


# Construct the query
subquery = sqlalchemy.select([videos_table.c.sl_no]).\
            where(sqlalchemy.extract('year', videos_table.c.publishedat) == 2022).\
            distinct().\
            subquery()

query = sqlalchemy.select([
        channels_table.c.channel_name,
        sqlalchemy.func.coalesce(sqlalchemy.func.count(subquery.c.sl_no), 0).label('video_count')
    ]).\
    select_from(channels_table).\
    outerjoin(subquery, channels_table.c.sl_no == subquery.c.sl_no).\
    group_by(channels_table.c.channel_name)

# Execute the query
result = connection.execute(query)

# Fetch the results
for row in result:
    channel_name = row.channel_name
    video_count = row.video_count
    print(f"Channel Name: {channel_name}, Video Count: {video_count}")

# Close the connection
#connection.close()


# In[88]:


import sqlalchemy

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')

# Create a connection
connection = engine.connect()

# Define the tables
channels_table = sqlalchemy.Table('channel', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
videos_table = sqlalchemy.Table('video', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)

# Construct the query
query = sqlalchemy.select([
        channels_table.c.channel_name,
        sqlalchemy.func.avg(videos_table.c.duration).label('average_duration')
    ]).\
    select_from(channels_table).\
    join(videos_table, channels_table.c.sl_no == videos_table.c.sl_no).\
    group_by(channels_table.c.channel_name)

# Execute the query
result = connection.execute(query)

# Fetch the results
for row in result:
    channel_name = row.channel_name
    average_duration = row.average_duration
    print(f"Channel Name: {channel_name}, Average Duration: {average_duration}")

# Close the connection
connection.close()


# In[90]:


import sqlalchemy

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine('mysql://root:12345@localhost:3306/youtube_data')

# Create a connection
connection = engine.connect()

# Define the tables
channels_table = sqlalchemy.Table('channel', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
videos_table = sqlalchemy.Table('video', sqlalchemy.MetaData(), autoload=True, autoload_with=engine)

# Construct the query
query = sqlalchemy.select([
        channels_table.c.channel_name,
        videos_table.c.video_name,
        videos_table.c.comment_count
    ]).\
    select_from(videos_table).\
    join(channels_table, channels_table.c.sl_no == videos_table.c.sl_no).\
    order_by(videos_table.c.comment_count.desc()).\
    limit(10)

# Execute the query
result = connection.execute(query)

# Fetch the results
for row in result:
    channel_name = row.channel_name
    video_name = row.video_name
    comment_count = row.comment_count
    print(f"Channel Name: {channel_name}, Video Name: {video_name}, Comment Count: {comment_count}")

# Close the connection
connection.close()


# In[1]:


import streamlit as st


# In[7]:


st.header('Youtube Data Harvesting')


# In[ ]:




