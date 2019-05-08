! /usr/bin/env python
# -*- coding: utf-8- -*-
""" Performs actions on your own feed / users

    * Likes pictures on your own feed
    * NEED TO SET RELATIONSHIP BOUNDS FOR MORE COMPLEX INTERACTIONS
"""

import os

from instapy import InstaPy
from instapy import smart_run

from plugins.get_smart_hashtags import get_hashtags
from plugins.better_comments.py import create_comment, WORD_LIST

insta_username = os.environ.get('IG_SOUR')
insta_password = os.environ.get('IG_SOURPASS')

SMART_HASHTAGS = 'sourdough'
HASHTAGS = get_hashtags(SMART_HASHTAGS)

COMMENTS = create_comment(WORD_LIST, 20)

session = InstaPy(username=insta_username, password=insta_password,
        headless_browser=True, disable_image_load=True, split_db=True)

with smart_run(session):
    # settings first
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True,
            max_followers=2000, min_followers=45, min_following=77)

    session.set_quota_supervisor(enabled=True,
            sleep_after=["likes", "follows"],
            sleepyhead=True, stochastic_flow=True,
            notify_me=False,
            peak_likes=(100, 1000),
            peak_comments=(21, 250),
            peak_follows=(200, None))

    # then actions
    session.set_do_follow(enabled=True, percentage=45, times=2)
    session.set_do_comment(enabled=True, percentage=85)
    session.set_comments(COMMENTS)
    # set_delimit_commenting has a bug that prevents comments from happening

    session.like_by_tags(HASHTAGS, amount=7, use_smart_hashtags=False,
            skip_top_posts=True)
    session.unfollow_users(amount=45, InstapyFollowed=(True, "nonFollowers"), 
            style="FIFO", unfollow_after=42*60*60, sleep_delay=450)
