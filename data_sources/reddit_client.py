import requests

HEADERS = {
    "User-Agent": "PulseMarketSentiment/1.0"
}

def fetch_reddit_posts(subreddit: str, limit: int = 5):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception("Reddit data fetch failed")

    data = response.json()
    posts = []

    for item in data["data"]["children"]:
        post = item["data"]
        posts.append({
            "title": post["title"],
            "score": post["score"]
        })

    return posts


