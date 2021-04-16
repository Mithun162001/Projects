# -*- coding: utf-8 -*-
"""Parkinson's Disease.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hn_kp9pS-2kpsCjuM81qNjmJbr9FHeyu

# PARKINSON'S DISEASE ANALYSIS AND CLASSIFICATION

Since there is no definitive laboratory test to diagnose PD, diagnosis is often difficult, particularly in the early stages when motor effects are not yet severe. Monitoring progression of the disease over time requires repeated clinic visits by the patient. An effective screening process, particularly one that doesn’t require a clinic visit, would be beneficial. Since PD patients exhibit characteristic vocal features, voice recordings are a useful and non-invasive tool for diagnosis. If machine learning algorithms could be applied to a voice recording dataset to accurately diagnosis PD, this would be an effective screening step prior to an appointment with a clinician
"""

# Commented out IPython magic to ensure Python compatibility.
# Importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import files
uploaded = files.upload()

# we store the csv file in a dataframe
df= pd.read_csv('datasets_410614_786211_parkinsons.csv')
df[:5]

"""Attribute Information:

* name - ASCII subject name and recording number
* MDVP:Fo(Hz) - Average vocal fundamental frequency
* MDVP:Fhi(Hz) - Maximum vocal fundamental frequency
* MDVP:Flo(Hz) - Minimum vocal fundamental frequency
* MDVP:Jitter(%),
* MDVP:Jitter(Abs),
* MDVP:RAP,MDVP:PPQ,
* Jitter:DDP - Several measures of variation in fundamental frequency
* MDVP:Shimmer,MDVP:Shimmer(dB),
* Shimmer:APQ3,
* Shimmer:APQ5,
* MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude
* NHR,HNR - Two measures of ratio of noise to tonal components in the voice
* status - Health status of the subject (one) - Parkinson's, (zero) - healthy
* RPDE,D2 - Two nonlinear dynamical complexity measures
* DFA - Signal fractal scaling exponent
spread1,spread2,
* PPE - Three nonlinear measures of fundamental frequency
variation 9. 
* car name: string (unique for each instance)
"""

df.info()

"""There are 195 observations and 24 features in the dataframe"""

# We check whether there are any missing values present in the data
sns.heatmap(df.isna(), yticklabels= False, cbar= False, cmap= 'viridis')

"""We see that there are no missing values present in the dataframe

# EDA
"""

# We shall see the distribution of target variable status
sns.countplot(x= 'status', data= df)

"""* We see that there are more number of patients who has been tested positive for Parkinson's disease"""

df.columns

# We shall see how the average vocal fundamental frequnecy are distributed
sns.barplot(x='status', y='MDVP:Fhi(Hz)', data=df, palette= 'seismic')
plt.title('Status vs Average Vocal Fundamental Frequency')

"""* it is clear that the patients having less vocal frequency are tend to have Parkinson's disease"""

# Visulaisation of NHR, a measure of ratio of noise to tonal components of voice vs the Status of the patient
sns.barplot(x='status', y='NHR', data=df, palette= 'seismic')
plt.title('Status vs Noise to Tonal Ratio')

"""* From the viz, we see that the patients who are having more NHR value (or) having more noise component in the numerator of the ratio (or) having less tonal component in the ratio are tend to be affected by Parkinson's disease"""

sns.barplot(x='status', y='MDVP:Shimmer(dB)', data=df, palette= 'seismic')
plt.title('Status vs MDVP Shimmer in dB')

"""* This tells us that patients who have higher decibals of Shimmer are tend to have Parkinson's disease"""

sns.kdeplot(x='DFA', hue='status',data= df)
plt.title('Distribution of DFA- Signal Fractional Scaling')

"""* Pateints having parkinson's disease are found to be have more density in Signal Fractional Scaling test- DFA"""

sns.kdeplot(x= 'PPE', data= df, hue= 'status')
plt.title('Distribution of PPE')

"""* from this distribution plot it's clear that patients with higher density are tend to be positive for Parkinson's disease"""

# We see the correlation of the data 
df.corr()[:5]

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), cmap= 'viridis')

"""# SUPERVISED LEARNING"""

df.info()

df.columns

# Creating feature matrix
# We leave out the target variable & categorical features since our machine learning lagorithms can't make out anything of categorical values
X = df[['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
       'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
       'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
       'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA',
       'spread1', 'spread2', 'D2', 'PPE']]
X[:5]

X.info()

"""* we have our feature matrix X which only contains numerical values in it"""

# Creating target variable y
y = df['status']
y[:5]

# we split the data into training and testing test of the ratio 70:30
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.3, random_state = 42)

"""*Standard Classification Algorithms*

* KNN
* Logistic Regression
* Decision Trees

* K Nearest Neighbour Algorithm
"""

# Scaling the data since KNN evalutes based upon the Eucleadean Distance between the points
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(X)

scaled_features = scaler.transform(X)
scaled_features[:5]

df_knn = pd.DataFrame(scaled_features, columns= [['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
       'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
       'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
       'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA',
       'spread1', 'spread2', 'D2', 'PPE']])
df_knn[:5]

from sklearn.model_selection import train_test_split
X_train_knn, X_test_knn, y_train_knn, y_test_knn = train_test_split(df_knn,y,test_size= 0.3, random_state = 42)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)   # 1st we see how the model performs for 1 neighbor

knn.fit(X_train_knn, y_train_knn)

pred_knn = knn.predict(X_test_knn)
pred_knn[:5]

y_test_knn[:5]

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test_knn, pred_knn))
print("\n")
print(classification_report(y_test_knn, pred_knn))

"""We see that we have attained 97% accuracy for k=1, but we can find best k value and maximise acuuracy as possible"""

error_rate = []
for i in range(1,40):
  knn_i = KNeighborsClassifier(n_neighbors=i)
  knn_i.fit(X_train_knn, y_train_knn)
  pred_i = knn_i.predict(X_test_knn)
  error_rate.append(np.mean(pred_i != y_test_knn))

sns.lineplot(x=range(1,40), y=error_rate)
plt.title('K values vs Error Rate')
plt.xlabel('K values')
plt.ylabel('Error rate')

"""We see that, at k=1 the error rate is low, so the model we built at the beginning is the most accurate KNN model we can build"""

print(confusion_matrix(y_test_knn, pred_knn))
print("\n")
print(classification_report(y_test_knn, pred_knn))

"""* Out of 15 values of not having parkinson's disease, our model has predicted all 15 cases as not having parkinson's giving a F1 score of 0.94
* Out of 44 cases of having Parkinson's disease, our model was able to predict 42 of the cases correctly and 2 of them have been predicted wrong(FP) giving an F1 score of 0.98
"""

knn_accuracy = 0.97 # So we store the accuracy value here, so we can compare it with other classification models
print("The accuracy recorded in KNN model: ", knn_accuracy*100, "%")

"""* Logistic Regression"""

from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression()   # intializing the Logistic regreesion classifier

lr_model.fit(X_train, y_train)

pred_lr = lr_model.predict(X_test)
pred_lr[:5]

y_test[:5]

print(confusion_matrix(y_test_knn, pred_lr))
print("\n")
print(classification_report(y_test_knn, pred_lr))

"""* Out of 15 values of not having parkinson's disease, our model has predicted 9 cases as not having parkinson's and 6 of them have been predcited wrongly giving a F1 score of 0.67
* Out of 44 cases of having Parkinson's disease, our model was able to predict 41 of the cases correctly and 3 of them have been predicted wrong(FP) giving an F1 score of 0.90
"""

lr_accuracy = 0.85
# So we store the accuracy value here, so we can compare it with other classification models
print("The accuracy recorded in Logistic Regression model: ", lr_accuracy*100, "%")

"""* Decision trees"""

from sklearn.tree import DecisionTreeClassifier
model_tree = DecisionTreeClassifier()   # Intializing the model

model_tree.fit(X_train, y_train)

pred_tree = model_tree.predict(X_test)
pred_tree[:5]

y_test[:5]

print(confusion_matrix(y_test_knn, pred_tree))
print("\n")
print(classification_report(y_test_knn, pred_tree))

"""* Out of 15 values of not having parkinson's disease, our model has predicted 11 cases as not having parkinson's and 4 of them have been predcited wrongly giving a F1 score of 0.76
* Out of 44 cases of having Parkinson's disease, our model was able to predict 41 of the cases correctly and 3 of them have been predicted wrong(FP) giving an F1 score of 0.92
"""

tree_accuracy = 0.88
# So we store the accuracy value here, so we can compare it with other classification models
print("The accuracy recorded in Decision tree model: ", tree_accuracy*100, "%")

"""*Ensemble Model*

* Random Forest Algorithm
"""

from sklearn.ensemble import RandomForestClassifier
model_forest = RandomForestClassifier(n_estimators=100)  # intialising the model

model_forest.fit(X_train, y_train)

pred_forest = model_forest.predict(X_test)
pred_forest[:5]

y_test[:5]

print(confusion_matrix(y_test_knn, pred_forest))
print("\n")
print(classification_report(y_test_knn, pred_forest))

"""* Out of 15 values of not having parkinson's disease, our model has predicted 12 cases as not having parkinson's and 3 of them have been predicted wrongly giving a F1 score of 0.89
* Out of 44 cases of having Parkinson's disease, our model was able to predict all 44 cases correctly gicing an F1 score of 0.97
"""

forest_accuracy = 0.95
# So we store the accuracy value here, so we can compare it with other classification models
print("The accuracy recorded in Random Forest model: ", forest_accuracy*100, "%")

"""# Comparing all the models and choosing the best one"""

print("The accuracy recorded in KNN model: ", knn_accuracy*100, "%")
print("The accuracy recorded in Logistic Regression model: ", lr_accuracy*100, "%")
print("The accuracy recorded in Decision tree model: ", tree_accuracy*100, "%")
print("The accuracy recorded in Random Forest model: ", forest_accuracy*100, "%")

"""* From the above cell, it's clear that K Nearest Neighbor algorithm has worked well with the data we provided giving an accuracy of 97%
* the next best is to use Random Forest Classifier giving an accuracy of 95%
"""