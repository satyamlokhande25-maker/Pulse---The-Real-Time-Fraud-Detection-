from fastapi import FastAPI
from data_sources.reddit_client import fetch_reddit_posts
from sentiment.analyzer import analyze_posts

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API working"}

@app.get("/reddit/{subreddit}")
def reddit_sentiment(subreddit: str, limit: int = 5):
    posts = fetch_reddit_posts(subreddit, limit)
    analysis = analyze_posts(posts)
    return {
        "subreddit": subreddit,
        "total_posts": len(analysis),
        "results": analysis
    }



