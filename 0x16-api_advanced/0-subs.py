#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetch the number of subscribers for a given subreddit.
    """
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    request_headers = {"User-Agent": "Reddit Scraper v1.0"}
    response = requests.get(
        subreddit_url,
        headers=request_headers,
        allow_redirects=False
    )
    if response.status_code != 200:
        return 0
    subscriber_count = response.json()['data']['subscribers']
    return subscriber_count
