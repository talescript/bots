! /usr/bin/env python
# -*- coding: utf-8- -*-
""" Performs actions on your own feed / users

    * Likes pictures on your own feed
    * NEED TO SET RELATIONSHIP BOUNDS FOR MORE COMPLEX INTERACTIONS
"""

import os

from instapy import InstaPy
from instapy import smart_run

from get_smart_hashtags import get_hashtags

insta_username = os.environ.get('IG_SOUR')
insta_password = os.environ.get('IG_SOURPASS')

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

SMART_HASHTAGS = 'sourdough'
HASHTAGS = get_hashtags(SMART_HASHTAGS)

session = InstaPy(username=insta_username, password=insta_password,
        headless_browser=True, disable_image_load=True)

with smart_run(session):
    # settings first
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True,
            max_followers=800, min_followers=45, min_following=77)

    # then actions
    session.set_do_comment(enabled=True, percentage=85)
    session.set_comments(COMMENTS)
    # set_delimit_commenting has a bug that prevents comments from happening

    session.like_by_tags(HASHTAGS, amount=7, use_smart_hashtags=False,
            skip_top_posts=True)
   # session.unfollow_users(amount=5, nonFollowers=True, style="FIFO",
   #         unfollow_after=42*60*60, sleep_delay=450)
