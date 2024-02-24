#!/usr/bin/python3
"""
Query the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetch and print the titles of the first 10 hot posts for a given subreddit.
    subreddit (str): The name of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
