#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_posts(subreddit):
    """Print the titles of the top 10 posts on a given subreddit."""
    subreddit_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "My Application 1.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(subreddit_url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json().get("data")
    [print(post.get("data").get("title")) for post in data.get("children")]