# Bitcoin-Twitter-sentiment-analysis
Computational Data Science project in SUTD.

This project revolves the use of twitter data and sentiment analysis to predict the price trend for bitcoin.



Data Collection


Using GetOldTweets3 we are able to scrap twitter data from any specified date containing any keyword, in our case, bitcoin.
Tweets.zip contains a sample dataset to work with. Run "pip3 install GetOldTweets3" in terminal to install GetOldTweets3 and then we can perform the queries. The file Gen_tweet_queries creates a txt file for each month with all the commandline functions and for everyday of the month. Run the files created by this to start collecting data

Cleaning tweets


Dropping useless columns to make csv files smaller and perform simple cleaning of tweets like urls, imgs, non alpha numeric and hashtags
To be done : filter out ads as well

Sentiment Analysis


Using Vader and textblob, we performed sentiment analysis on all the tweets collected.

Preliminary Model


Logistic Regression was used.
