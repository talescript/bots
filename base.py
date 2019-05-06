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

COMMENTS = ['Your picture is great!!!',
        'Nice! This picture is fantastic.',
        'The pic is really beautiful.',
        'Lovely :open_mouth:',
        'Damn your picture is terrific. Keep it up.',
        'Love your posts @{}',
        'Your post is awesome.',
        'Your shot is quite lovely.',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# Interaction based on the numbers of followers / following a user has
# DELIMIT_BY_NUMBERS activates/deactivates the usage of max/min
# potency_ratio = followers / following.
# Positive numbers to route interactions to only potential users 
# whose followers count is higher than following count.
ENABLE_RELATIONSHIP_BOUNDS = True
POTENCY_RATIO = None
DELIMIT_BY_NUMBERS = True
MAX_FOLLOWERS = 500
MAX_FOLLOWING = 500 
MIN_FOLLOWERS = 50 
MIN_FOLLOWING = 50 
MIN_POSTS = 10
MAX_POSTS = 1000

# Conservative numbers for new accounts.
# Every day you can like 25-45 per session.

# Follow 50-75 per day. Increase each day with 50 until 
# it reaches 450 max followers per day
# Credits to: haetschgern for the tip.
PEAK_LIKES = (25, 75)
PEAK_FOLLOWS = (25, 75)
PEAK_UNFOLLOWS = (35, 100)
PEAK_SERVER_CALLS = (500, 4745)
PEAK_COMMENTS = (5, 15)

# PENDING
# Skip non English Users
# User posted in the last 90 days
# follow users who commented in the last 3 days (3660 minutes)


SMART_HASHTAG = 'sourdough'
IGNORE_LIKING_USERS = []

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
#     session.set_quota_supervisor(enabled=True,
#                     peak_likes=PEAK_LIKES,
#                     peak_comments=PEAK_COMMENTS,
#                     peak_follows=PEAK_FOLLOWS, 
#                     peak_unfollows=PEAK_UNFOLLOWS,
#                     peak_server_calls=PEAK_SERVER_CALLS,
#                     sleep_after=["likes", "comments", "follows", "unfollows", "server_calls"],
#                     sleepyhead=True,
#                     stochastic_flow=True, notify_me=False)

    # Skip business accounts
    # User has profile image
    session.set_skip_users(skip_private=True,
                    private_percentage=100,
                    skip_no_profile_pic=True,
                    no_profile_pic_percentage=100)

    # will prevent commenting on and unfollowing your good friends (the images will
    # still be liked)
    # session.set_dont_include(['friend1', 'friend2', 'friend3'])
    # Prevents unfollow followers who have liked one of your latest 5 posts
    # session.set_dont_unfollow_active_users(enabled=True, posts=5)

    # Actions for the bot
    session.set_ignore_users(IGNORE_LIKING_USERS)
    
    # Checks number of existing comments a post has.
    # set_delimit has a bug that prevents commenting
    # session.set_delimit_commenting(enabled=True, max=12, min=None)
    session.set_do_comment(enabled=True, percentage=70)
    session.set_comments(COMMENTS, media='Photo')

    # SMART HASHTAGS ISN'T WORKING FOR ME.
    # session.set_smart_hashtags(SMART_HASHTAG, limit=10, sort='random', log_tags=True)
    # amount of posts that will be liked.
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.set_delimit_liking(enabled=True, max=125, min=None)
    
    # Performs likes on your own feeds
    session.like_by_feed(amount=70, randomize=True)
    session.like_by_tags(HASHTAGS, amount=25, use_smart_hashtags=False, skip_top_posts=True, 
                        interact=True)

    # unfollow users who aren't following back
    session.unfollow_users(amount=75, nonFollowers=True, style="FIFO", 
                        unfollow_after=42*60*60, sleep_delay=450)
