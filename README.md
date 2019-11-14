# Bitcoin-Twitter-sentiment-analysis
Computational Data Science project in SUTD.

This project revolves the use of twitter data and sentiment analysis to predict the price trend for bitcoin.

Data Collection
Using GetOldTweets3 we are able to scrap twitter data from any specified date containing any keyword, in our case, bitcoin.
Tweets.zip contains a sample dataset to work with.

Cleaning tweets
Dropping useless columns to make csv files smaller and perform simple cleaning of tweets like urls, imgs, non alpha numeric and hashtags
To be done : filter out ads as well

Sentiment Analysis
Using Vader and textblob, we performed sentiment analysis on all the tweets collected.

Preliminary Model
Logistic Regression was used.
