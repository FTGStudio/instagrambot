#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
#sys.path.append(os.path.join(sys.path[0],'src'))

from src.instabot import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.unfollow_protocol import unfollow_protocol
from src.follow_protocol import follow_protocol
import time
import datetime

#IMPORTANT INFORMATION!
##Likes,Comments,Follows, and Unfollows have been tweaked to the amount of hours the bot runs for!
###So if your like_per_day=1000 and the bot runs for 2 hours, it will try to post that many in those two hours!
bot = InstaBot(login="westcottsupply", password="365273jsg",
               like_per_day=1000,
               comments_per_day=0,
               tag_list=["thrasher", "art", "design", "mensfashion", "bmx", "painting", "surfing", "pyramid",
                         "apparel", "warpedtour", "shred", "skateboard", "streetwear", "girlswhoride", "surfergirl"
                         "surfbabe", "fitchick", "crossfit", "wakeboarder", "boardsports", "cute", "puremichigan"],
               tag_blacklist=['follow4follow', 'f4f', "followers"],
               user_blacklist={},
               max_like_for_one_tag=50,
               follow_per_day=300,
               follow_time=1*60,
               unfollow_per_day=300,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0,
               proxy='',
               # Use unwanted username list to block users which have username contains one of this string
               ## Doesn't have to match entirely example: mozart will be blocked because it contains *art
               ### freefollowers will be blocked because it contains free
               unwanted_username_list=['second','stuff','art','project','love','life','food','blog','free','keren','photo','graphy','indo',
                                       'travel','art','shop','store','sex','toko','jual','online','murah','jam','kaos','case','baju','fashion',
                                        'corp','tas','butik','grosir','karpet','sosis','salon','skin','care','cloth','tech','rental',
                                        'kamera','beauty','express','kredit','collection','impor','preloved','follow','follower','gain',
                                        '.id','_id','bags', "followers", "+", ],
               # bot_running_hour_start = 0,
               # bot_running_hour_end = 23
			   #Change these to whatever hours you like
			   ##The bot will only run during these hours and sleep 
			   ### HOURS BETWEEN 0-24 ONLY!!!!!!!!!!!!!!!!
			   #### EXAMPLE 1
			   #####bot_running_hour_start = 5,
			   #####bot_running_hour_end = 16
			   #### EXAMPLE 2
			   #####bot_running_hour_start = 22,
			   #####bot_running_hour_end = 4
			   #### BOTH OF THESE ARE VALID HOURS AND WORK!
               )
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW PEOPLE WHO DON'T FOLLOW BACK BASED ON RECENT FEED ONLY")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW PEOPLE BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
           ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0 :
        bot.new_auto_mod()

    elif mode == 1 :
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10*60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) <50 :
                feed_scanner(bot)
                time.sleep(5*60)
                follow_protocol(bot)
                time.sleep(10*60)
                check_status(bot)

    elif mode == 2 :
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3 :
        unfollow_protocol(bot)
        time.sleep(10*60)

    elif mode == 4 :
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10*60)

    elif mode == 5 :
        bot.bot_mode=2
        unfollow_protocol(bot)

    else :
        print ("Wrong mode!")
