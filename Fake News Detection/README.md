<h1 style="border: 0;"> FAKE NEWS DETECTION </h1>

<img src="https://media.giphy.com/media/3ohzdJeMka5heqSbZu/giphy.gif" height="200px">

<h2>What is Fake News?</h2>
A type of yellow journalism, fake news encapsulates pieces of news that may be hoaxes and is generally spread through social media and other online media. This is often done to further or impose certain ideas and is often achieved with political agendas. Such news items may contain false and/or exaggerated claims, and may end up being viralized by algorithms, and users may end up in a filter bubble.

<h2>What is a TfidfVectorizer?</h2>

- TF (Term Frequency): The number of times a word appears in a document is its Term Frequency. A higher value means a term appears more often than others, and so, the document is a good match when the term is part of the search terms.

- IDF (Inverse Document Frequency): Words that occur many times a document, but also occur many times in many others, may be irrelevant. IDF is a measure of how significant a term is in the entire corpus.

The TfidfVectorizer converts a collection of raw documents into a matrix of TF-IDF features.


# Table Of Contents

-   [Prerequisites](#prerequisites)
-   [Contribute](#Contribute)
-   [About](#About)
-   [Evaluation](#Evaluation)
-   [Licence](#Licence)



## Prerequisites

-   Install python packages such as `numpy` `pandas` `scikit-learn` `seaborn` `matplotlib`



## Contribute

-   Fork the repository
-   Commit your changes
-   create Pull request

## About
This advanced python project of detecting fake news deals with fake and real news. Using sklearn, we build a TfidfVectorizer on our dataset. Then, we initialize a PassiveAggressive Classifier and fit the model. In the end, the accuracy score and the confusion matrix tell us how well our model fares.

## Evaluation
```
Classification report: 
              precision    recall  f1-score   support

        FAKE       0.92      0.95      0.93       943
        REAL       0.95      0.91      0.93       958

    accuracy                           0.93      1901
   macro avg       0.93      0.93      0.93      1901
weighted avg       0.93      0.93      0.93      1901

Confusion matrix: 
[[897  46]
 [ 83 875]]
```

## Clone the project

```
git clone git@github.com:Mithun162001/Projects/Fake-News-Detection-.git
```
