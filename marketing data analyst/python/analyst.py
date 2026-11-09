import pandas as pd
from sqlalchemy import create_engine
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def fetch_data_sql():
    engine = create_engine(
        "mssql+pyodbc://@localhost\\SQLEXPRESS/PortfolioProject_MarketingAnalytics"
        "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    query = """
        SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText
        FROM dbo.customer_reviews
    """
    df = pd.read_sql(query, engine)
    engine.dispose()
    return df

customers_review_df = fetch_data_sql()


# Sentiment analysis with VADER
sia =SentimentIntensityAnalyzer()
def analyze_sentiment(review):
    sentiment_score = sia.polarity_scores(review)

    return sentiment_score['compound']

def the_category_sentiment(score,Rating):
    if score >= 0.05 :
       if Rating >= 4:
            return 'Positive'
       elif score  == 3:    
            return 'mixed position'
       else :
            return 'mexid Negative'
    elif score <= -0.05:
       if Rating <= 2:
           return ' Negative'
       elif Rating == 3:
            return 'mixed position' 
       else :
            return 'mixed Negative'
    else:
        if Rating >= 4: 
            return 'mixed position'
        elif Rating <=2:
            return 'negative'
        else:
            return 'Neutral'

 #define a function to bucket sentiment scores into categories
def SentimentBucket(score):
    if score >= 0.05:
        return '0.5 to 1'
    elif 0.0 <=score <0.5:
        return '0 to 0.5'
    elif -0.5<= score <0.0:
        return '-0.5 to 0'
    else: 
        return '-1 to -0.5'

customers_review_df['SentimentScore'] = customers_review_df['ReviewText'].apply(analyze_sentiment)
customers_review_df['SentimentCategory'] = customers_review_df.apply(lambda row: the_category_sentiment(row['SentimentScore'], row['Rating']), axis=1)
customers_review_df['SentimentBucket'] = customers_review_df['SentimentScore'].apply(SentimentBucket)

customers_review_df.to_csv('customer_reviews_with_sentiment.csv', index=False)