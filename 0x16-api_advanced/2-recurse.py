#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Fetch the titles of the first 100 hot posts for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.
    hot_list (list, optional): A list to store the
    titles of the hot posts. Defaults to [].
    after (str, optional): The 'after' parameter for
    pagination in Reddit's API. Defaults to None.

    Returns:
    list: A list of the titles of the hot posts.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after
    )
    headers = {"User-Agent": "Reddit Scraper v1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    for post in response.json().get("data").get("children"):
        hot_list.append(post.get("data").get("title"))
    after = response.json().get("data").get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
