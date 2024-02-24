#!/usr/bin/python3
"""
Function that interacts with the Reddit API, retrieves the title of all
hot articles, and prints a sorted count of specified keywords.
"""
import requests


def count_words(subreddit_name, keyword_list, post_titles=[], next_page=""):
    """
    Retrieve the titles of the first 100 hot posts for
    a given subreddit and count occurrences of specified keywords.
    """
    subreddit_url = ("https://www.reddit.com/r/{}/hot.json"
                     "?limit=100&after={}").format(subreddit_name, next_page)
    request_headers = {"User-Agent": "My Application 1.0"}
    response = requests.get(
        subreddit_url,
        headers=request_headers,
        allow_redirects=False)
    if response.status_code != 200:
        return
    for post in response.json().get("data").get("children"):
        post_titles.append(post.get("data").get("title"))
    next_page = response.json().get("data").get("after")
    if next_page is None:
        keyword_counts = {}
        for keyword in keyword_list:
            keyword_counts[keyword] = 0
        for title in post_titles:
            for word in title.split():
                if word.lower() in keyword_counts:
                    keyword_counts[word.lower()] += 1
        for key, value in sorted(
            keyword_counts.items(), key=lambda x: x[1], reverse=True
        ):
            if value > 0:
                print("{}: {}".format(key, value))
        return
    return count_words(subreddit_name, keyword_list, post_titles, next_page)
