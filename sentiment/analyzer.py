from sentiment.model import predict_sentiment

def analyze_posts(posts: list):
    results = []

    for post in posts:
        sentiment = predict_sentiment(post["title"])
        results.append({
            "title": post["title"],
            "sentiment": sentiment,
            "score": post["score"]
        })

    return results
