#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Gets relevant hashtags for instagram.

"""
import requests

def get_hashtags(tag):
    URL = f'https://query.displaypurposes.com/tag/{tag}' 
    r = requests.get(URL).json()

    HASHTAGS = []
    for data in r['results']:
        if data['relevance'] >= 65:
                # 'rank': 50, 'relevance': 65
                # 'rank': 75, 'relevance': 35,
                HASHTAGS.append(data['tag'])
    
    return HASHTAGS

if __name__ == "__main__":
    print(get_hashtags())