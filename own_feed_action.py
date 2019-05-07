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

insta_username = os.environ.get('IG_SOUR')
insta_password = os.environ.get('IG_SOURPASS')

session = InstaPy(username=insta_username,
        password=insta_password,
        headless_browser=True,
        disable_image_load=True,
        split_db=True)

with smart_run(session):
    session.like_by_feed(amount=70, randomize=True)
    # session.unfollow_users(amount=10, nonFollowers=True,
    #        style="FIFO", unfollow_after=42*60*60,
    #        sleep_delay=450)
    
