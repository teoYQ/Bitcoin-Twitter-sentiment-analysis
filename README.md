# Bitcoin-Twitter-sentiment-analysis
## Computational Data Science project in SUTD.

This project revolves the use of twitter data and sentiment analysis to predict the price trend for bitcoin.



### Data Collection


Using GetOldTweets3 we are able to scrap twitter data from any specified date containing any keyword, in our case, bitcoin.
Tweets.zip contains a sample dataset to work with. Run "pip3 install GetOldTweets3" in terminal to install GetOldTweets3 and then we can perform the queries. The file Gen_tweet_queries creates a txt file for each month with all the commandline functions and for everyday of the month. Run the files created by this to start collecting data

For our project we used tweets from 1st Jan 2019 to 30th October 2019

### Cleaning tweets


Dropping useless columns to make csv files smaller and perform simple cleaning of tweets like urls, imgs, non alpha numeric and hashtags.
Filtered ads through LDA and bag of words


### Sentiment Analysis

Using Vader and textblob, we performed sentiment analysis on all the tweets collected. Both Vader and sentiment used a scoring system of -1 to 1. We aggregated the scores for each hour and got the hourly mean sentiment score for the 2019 dataset. 

### Preliminary Model

Logistic Regression was used back when we were still using the 2017 dataset.  

After using the 2019 dataset and attempting multiple models, we found that Logistic Regression with K-folds, K-nearest Neighbors and Random forest gave us a lowly accuracy of 53%.
Hence, we decided to implement a neural net that would take in all the features and also including a time series. Using a birectional LSTM model, we manage to bump this up to our current 77.8% accuracy.

