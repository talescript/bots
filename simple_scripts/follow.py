from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''  #<- enter username between the quotes 'amanc555'
insta_password = ''  #<- enter password

s = InstaPy(username=insta_username, password=insta_password,
        headless_browser=True, use_firefox=False)

# Enter the hashtags you want to use here.
# place them between quotes and separate each one with a comma
# place only three or ten
HASHTAGS = ['first_hashtag', 'second_hashtag', 'third_hashtag']

with smart_run(s):
    # in this block of code place the rules of who you would like to
    # follow. This will only follow people with a max amount of 2000
    # followers
    s.set_relationship_bounds(enabled=True, delimit_by_numbers=True,
            max_followers=2000,
            min_followers=45,
            min_following=77)

    # remove hashtags in the next two lines to enable likes
    #s.like_by_tags(HASHTAGS, amount=5, use_smart_hashtags=False,
    #        skip_top_posts=False)

    # In amount, place how many you would like to follow / unfollow
    s.follow_by_tags(HASHTAGS, amount=20)
