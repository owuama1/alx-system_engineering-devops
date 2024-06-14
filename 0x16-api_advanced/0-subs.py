#!/usr/bin/python3
"""
Query the Reddit API to fetch the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
    - subreddit (str):
      The name of the subreddit (e.g., 'python', 'learnprogramming').

    Returns:
    - int: Number of subscribers if the subreddit exists, otherwise 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            print(f"Error fetching data:"
                  f"Status Code {response.status_code}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
