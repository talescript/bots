import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']

like_tag_list = ['vegan', 'veganfoodshare', 'veganfood', 'whatveganseat',
                 'veganfoodie', 'veganism', 'govegan',
                 'veganism', 'vegansofig', 'veganfoodshare', 'veganfit',
                 'veggies']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=15000)

    session.set_dont_like(dont_likes)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 250), interact=False)
    
