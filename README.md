# 📊 Pulse - Real-Time Market Sentiment Analyzer

Pulse is a real-time market sentiment analyzer that fetches posts from Reddit and analyzes the sentiment of each post to determine market sentiment for various subreddits like Bitcoin, stocks, cryptocurrency, etc.

## 🚀 Features

- **Real-time Data Fetching**: Fetches latest posts from any Reddit subreddit
- **Sentiment Analysis**: Analyzes post titles using TextBlob sentiment analysis
- **Visual Dashboard**: Streamlit-based dashboard for visualizing sentiment results
- **RESTful API**: FastAPI-based API for programmatic access
- **Multiple Data Sources**: Support for Reddit (with extensible architecture for news sources)

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Dashboard**: Streamlit
- **Sentiment Analysis**: TextBlob
- **Data Validation**: Pydantic
- **HTTP Client**: Requests
- **ASGI Server**: Uvicorn

## 📁 Project Structure

```
Pulse-The Real time Market Sentiment Analyzer/
├── api/
│   ├── __init__.py
│   └── main.py              # FastAPI application
├── core/
│   ├── __init__.py
│   └── config.py            # Configuration settings
├── dashboard/
│   └── app.py               # Streamlit dashboard
├── data_sources/
│   ├── __init__.py
│   ├── news_client.py       # News API client
│   └── reddit_client.py     # Reddit API client
├── sentiment/
│   ├── __init__.py
│   ├── analyzer.py          # Sentiment analysis logic
│   └── model.py             # ML model for sentiment
├── utils/
│   ├── __init__.py
│   └── text_cleaner.py      # Text cleaning utilities
├── requirement/
│   └── requirement.txt       # Python dependencies
├── test/
│   └── __init__.py
└── README.md                 # This file
```

## 📋 Prerequisites

- Python 3.8 or higher
- Reddit account (for API access - uses public Reddit API)

## ⚙️ Installation

1. **Clone the repository**
   
```
bash
   git clone https://github.com/satyamlokhande25-maker/Pulse---The-Real-Time-Fraud-Detection-.git
   cd Pulse-The Real time Market Sentiment Analyzer
   
```

2. **Create a virtual environment** (optional but recommended)
   
```
bash
   python -m venv .venv
   
```

3. **Activate the virtual environment**
   - Windows:
     
```
bash
     .venv\Scripts\activate
     
```
   - Linux/Mac:
     
```
bash
     source .venv/bin/activate
     
```

4. **Install dependencies**
   
```
bash
   pip install -r requirement/requirement.txt
   
```

## 🚦 How to Run

### Option 1: Run API and Dashboard Together

1. **Start the API server** (Terminal 1)
   
```
bash
   cd "c:/Users/hp5cd/OneDrive/Desktop/Pulse-The Real time Market Sentiment Analyzer"
   uvicorn api.main:app --reload
   
```
   The API will run at `http://127.0.0.1:8000`

2. **Start the Dashboard** (Terminal 2)
   
```
bash
   cd "c:/Users/hp5cd/OneDrive/Desktop/Pulse-The Real time Market Sentiment Analyzer"
   streamlit run dashboard/app.py
   
```
   The dashboard will open at `http://localhost:8501`

### Option 2: Run Only API

```
bash
uvicorn api.main:app --reload
```

### Option 3: Run Only Dashboard

```
bash
streamlit run dashboard/app.py
```

## 📖 API Documentation

Once the API is running, visit:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### API Endpoints

#### 1. Root Endpoint
```
GET /
```
Returns a simple health check message.

**Response:**
```
json
{
  "message": "API working"
}
```

#### 2. Reddit Sentiment Analysis
```
GET /reddit/{subreddit}
```
Fetches posts from a subreddit and analyzes sentiment.

**Parameters:**
- `subreddit` (path): Name of the subreddit (e.g., "bitcoin", "stocks")
- `limit` (query, optional): Number of posts to fetch (default: 5, max: 20)

**Example Request:**
```
GET /reddit/bitcoin?limit=10
```

**Example Response:**
```
json
{
  "subreddit": "bitcoin",
  "total_posts": 10,
  "results": [
    {
      "title": "Bitcoin just hit $100k!",
      "sentiment": "positive",
      "score": 1500
    },
    {
      "title": "Market crash incoming",
      "sentiment": "negative",
      "score": 800
    }
  ]
}
```

## 📊 Using the Dashboard

1. Open the dashboard at `http://localhost:8501`
2. Enter a subreddit name (e.g., "bitcoin", "ethereum", "stocks", "wallstreetbets")
3. Adjust the number of posts to analyze using the slider
4. Click "Analyze Sentiment" button
5. View the sentiment analysis results:
   - Overall sentiment breakdown (Positive/Negative/Neutral)
   - Individual post analysis with sentiment and scores

## 🔧 Sentiment Analysis

The project uses **TextBlob** for sentiment analysis:

- **Positive**: Polarity > 0
- **Negative**: Polarity < 0
- **Neutral**: Polarity = 0

Sentiment is determined by analyzing the text polarity, where:
- Positive values indicate positive sentiment
- Negative values indicate negative sentiment
- Zero indicates neutral sentiment

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Reddit API](https://www.reddit.com/dev/api/) for providing access to subreddit data
- [TextBlob](https://textblob.readthedocs.io/) for sentiment analysis
- [FastAPI](https://fastapi.tiangolo.com/) for the API framework
- [Streamlit](https://streamlit.io/) for the dashboard

## 🔗 Links

- **GitHub Repository**: https://github.com/satyamlokhande25-maker/Pulse---The-Real-Time-Fraud-Detection-

---

Made with ❤️ for market sentiment analysis
