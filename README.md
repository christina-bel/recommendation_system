# recommendation_system
Restaurant recommendation system based on collaborative filtering


Recommendation System is aimed to provide the most relevant place for eating out in North Carolina and South Carolina (it is possible to choose any state you want). Yelp dataset is used for this purpose. 

Yelp is a crowd-sourced local business review and social networking site, which can help people to choose where to stay, to go or to eat. Yelp users can submit a review of their products or services using a one to five star rating system.

This restaurant recommendation system is based on the Collaborative Filtering, and to be accurate on the Matrix Factorization. Matrix of users’ ratings can be broken down into user-feature and item-feature matrixes. These features are extracted from texts of reviews with the help of the TFIDF Vectorizer. Text should be prepared for analyses by removing punctuation, stop-words, lemmatization and so on…

At the end you can see predicted ratings and compare it with the given one. This model has a good level of accuracy both on train and test data. The model is trained with the help of Stochastic gradient descent and Least Square Error with regularization: ![formula](https://github.com/christina-bel/recommendation_system/blob/main/loss_function.png)

The final loss is calculated by the Mean Squared Error.

As the matrix of predicted ratings can be rather big, it is calculated and reduced to a given range of ratings (1-5) by using multiprocessing. 

The result of user’s request can be seen in the `recommendation.ipynb`.



## Dependencies

* json
* numpy 
* pandas 
* nltk (nltk.corpus, nltk.stem, nltk.tokenize)
* csv
* swifter
* sklearn
* pickle 
* arrow
* multiprocessing

Also you can find the dataset with this link **https://www.yelp.com/dataset**
