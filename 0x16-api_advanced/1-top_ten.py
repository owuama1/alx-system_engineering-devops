#!/usr/bin/python3
"""
Query the Reddit API to
fetch the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Retrieve, print the titles of the first 10 hot posts for a given subreddit.

    Args:
    - subreddit (str): The name of the
      subreddit (e.g., 'python', 'learnprogramming').

    Prints:
    - Prints the titles of the first
      10 hot posts if the subreddit exists, otherwise prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(
            url, headers=headers, params={'limit': 10}, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"Error fetching data: Status Code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
