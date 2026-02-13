from textblob import TextBlob

def predict_sentiment(text: str) -> str:
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    return "neutral"

