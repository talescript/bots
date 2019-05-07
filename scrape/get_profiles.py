#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reports top rated instagram Profiles.

Given a hashtag, it will search for pictures
with the highest amount of likes. Then it will
go into each profile and extract information
suce as: Posts count, follower count, and
the last three pictures, when it was and how
many likes each one has.
"""
import csv
import os
import lzma
import json
import datetime
import shutil
from pathlib import Path

import instaloader
from instaloader import Profile

HASHTAGS = ['cat', 'beach']
path = Path.cwd()

L = instaloader.Instaloader(download_pictures=False, download_videos=False, 
        download_video_thumbnails=False, download_geotags=False,
        download_comments=False, post_metadata_txt_pattern="")

# Downloads compressed json files with the metadata into folder 
# and deleted once script is finished.
# post filter can be used to test whether data should be downloaded
# L.download_hashtag('beach', max_count=3)

usercount = 0
MAXUSERS = 3
MAXPOSTS = 3
LIKES = 50
user_profiles = []

with open('hashtag_profiles.csv', 'a') as csv_file:
    csv_data = csv.writer(csv_file, delimiter=',')
    # If file exists do not create header
    if os.stat('hashtag_profiles.csv').st_size == 0:
        csv_data.writerow(['Username', 'Full name', 'Likes', 'Comments', 'Followers', 'Following', 'Mediacount'])
    for post in L.get_hashtag_posts("beach"):
        if post.likes >= LIKES:
            print("Getting information of user: ", post.owner_profile.username)
            usercount += 1
            csv_data.writerow([post.owner_profile.username, post.owner_profile.full_name, post.likes,
                            post.comments, post.owner_profile.followers, post.owner_profile.followees,
                            post.owner_profile.mediacount])

            # get the last three posts
            profile = Profile.from_username(L.context, post.owner_profile.username)
            postcount = 0
            for p in profile.get_posts():
                L.download_post(p, target=profile.username)
                postcount += 1

                if postcount == MAXPOSTS:
                    break
            # Collect all usernames so it can be iterated over and deleted
            user_profiles.append(profile.username)

        if usercount == MAXUSERS:
            break

with open('liked_pictures.csv', 'a') as csv_pics:
    csv_pics = csv.writer(csv_pics, delimiter=',')
    if os.stat('liked_pictures.csv').st_size == 0:
        csv_pics.writerow(['Username', 'Date', 'Likes'])
    for user in user_profiles:
        for data in (path / user).iterdir():
            f = lzma.open(data, mode='rt', encoding='utf-8').read()
            js = json.loads(f)
            print("Writing data for user: ", js['node']['owner']['username'])
            csv_pics.writerow([js['node']['owner']['username'], 
                    datetime.datetime.fromtimestamp(js['node']['taken_at_timestamp']).strftime('%m/%d/%Y'), 
                    js['node']['edge_liked_by']['count']])

        print("deleting: ", user)
        shutil.rmtree(path / user)
