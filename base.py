#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Opinionated base script

The script runs a headless firefox instance by default and
does not download images to save bandwidth. These settings
can be changed.
"""
import os

from instapy import InstaPy
from instapy import smart_run

from get_smart_hashtags import get_hashtags

# Using environment variables instead of hardcoding your username and password.
# Place in .bashrc file or whichever is used by your distro.
# Remember to reload the file and restart the terminal.
insta_username = os.environ.get('IG_USER')
insta_password = os.environ.get('IG_PASSWORD')

COMMENTS = ['This picture is great!!!',
        'Nice! This picture is great.',
        'The pic is really amazing.',
        'Just incredible :open_mouth:',
        'Damn your picture is really quite impressive. Keep it up.',
        'Love your posts @{}',
        'Nice! Your post is terrific.',
        'Darn, your shot is really quite lovely.',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# Interaction based on the numbers of followers / following a user has
ENABLE_RELATIONSHIP_BOUNDS = False
POTENCY_RATIO = 1.34
DELIMIT_BY_NUMBERS = True
MAX_FOLLOWERS = 3000
MAX_FOLLOWING = 900 
MIN_FOLLOWERS = 50 
MIN_FOLLOWING = 50 
MIN_POSTS = 10
MAX_POSTS = 1000

# Conservative numbers for new accounts.
# Every day you can add 20 follows and 50 likes.
# First value is the hourly and second daily value. They are peak values.
# Credits to: haetschgern for the tip.
PEAK_LIKES = (35, 100)
PEAK_FOLLOWS = (35, 100)
PEAK_UNFOLLOWS = (35, 100)
PEAK_SERVER_CALLS = (500, 4745)
PEAK_COMMENTS = (None, None)

SMART_HASHTAG = 'sourdough'

# Smart hashtags wasn't working so I implemented the function
HASHTAGS = get_hashtags(SMART_HASHTAG)


# Get an InstaPy session!
# Set headless_browser to true to run InstaPy in the background
# split_db splits the database per username
session = InstaPy(username=insta_username, 
            password=insta_password,
            headless_browser=True,
            use_firefox=True,
            disable_image_load=True,
            split_db=True,
            multi_logs=True)


with smart_run(session):
    """ Activity flow """
    # Interaction based on the numbers of followers / following a user has
    # Change to True to use these checks
    # Documentation is your friend.
    session.set_relationship_bounds(enabled=ENABLE_RELATIONSHIP_BOUNDS, 
                    potency_ratio=POTENCY_RATIO, 
                    delimit_by_numbers=DELIMIT_BY_NUMBERS, 
                    max_followers=MAX_FOLLOWERS,
                    max_following=MAX_FOLLOWING, 
                    min_followers=MIN_FOLLOWERS, 
                    min_following=MIN_FOLLOWING, 
                    min_posts=MIN_POSTS, 
                    max_posts=MAX_POSTS)

    # Once it reaches it's peak, it will jump every other action and it will
    # do all available actions.
    # If server calls reachs its peak, it will exit the program.
    # Sleeping: likes_h for hourly. likes_d for daily
    session.set_quota_supervisor(enabled=True, 
                    peak_likes=PEAK_LIKES,
                    peak_comments=PEAK_COMMENTS,
                    peak_follows=PEAK_FOLLOWS, 
                    peak_unfollows=PEAK_UNFOLLOWS,
                    peak_server_calls=PEAK_SERVER_CALLS,
                    sleep_after=["likes", "comments", "follows", "unfollows", "server_calls"],
                    sleepyhead=True,
                    stochastic_flow=True, notify_me=True)

    # will prevent commenting on and unfollowing your good friends (the images will
    # still be liked)
    #session.set_dont_include(['friend1', 'friend2', 'friend3'])
    # Prevents unfollow followers who have liked one of your latest 5 posts
    #session.set_dont_unfollow_active_users(enabled=True, posts=5)

    # Actions for the bot
    
    # Checks number of existing comments a post has.
    session.set_delimit_commenting(enabled=True, max=12, min=None)
    session.set_do_comment(enabled=True, percentage=70)
    session.set_comments(COMMENTS, media='Photo')

    # SMART HASHTAGS ISN'T WORKING FOR ME.
    #session.set_smart_hashtags(SMART_HASHTAG, limit=10, sort='random', log_tags=True)
    # amount of posts that will be liked.
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.like_by_tags(HASHTAGS, amount=25, use_smart_hashtags=False, skip_top_posts=True, 
                        interact=True)
    
    # Performs likes on your own feeds
    session.like_by_feed(amount=70, randomize=True)