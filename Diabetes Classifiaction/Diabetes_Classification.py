#!/usr/bin/env python
# coding: utf-8

# **DIABETES CLASSIFICATION**
# 

# In[1]:


# Here we will import the libraries required
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# We shall import the data to a DataFrame
from google.colab import files
uploaded = files.upload()


# In[3]:


# Converting it into a dataframe
df= pd.read_csv('diabetes_csv.csv')
df[:5]  # Displaying 1st 5 observations


# * Number of times pregnant
# * Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# * Diastolic blood pressure (mm Hg)
# * Triceps skin fold thickness (mm)
# * 2-Hour serum insulin (mu U/ml)
# * Body mass index (weight in kg/(height in m)^2)
# * Diabetes pedigree function
# * Age (years)
# * Class variable (0 or 1)
# * Class Distribution: (class value 1 is interpreted as "tested positive for
# diabetes")
# 
# 

# In[4]:


# Renaming the columns
df.rename(columns= {'preg':'n_pregnant','plas':'plasma','pres':'pressure','insu':'insulin','mass':'bmi','pedi':'pedigree'}, inplace= True)
df[:5]


# In[11]:


# class labelling
def labelling(param):
  if param == 'tested_positive':
    param = 1
    return param
  else:
    param = 0
    return param

df_new= df['class'].apply(lambda x: labelling(x))


# In[21]:


df_new.to_list()[:5]


# In[22]:


df['class_cat'] = df_new


# In[23]:


df[:5]


# In[25]:


# Now let's remove the class column
df.drop(columns= 'class', axis=1,inplace=True)


# In[26]:


df[:5]


# In[28]:


# Now we will check for missing values
df.isna().sum()
# Here we can see that there are no missing values present


# In[49]:


# we shall see how many values totally are tested_positive(1) and tested_negative(0)
df['class_cat'].value_counts()
sns.displot(df['class_cat'].values, kde= False, color='green')
sns.set_theme(style='dark', palette='rainbow')
# so we see that there are 500 negativelt tested patients and 268 tested for positive for Diabetes mellitus


# In[50]:


# Now we will see the plot of the entire dataset
sns.pairplot(df, hue= 'class_cat')
sns.set_theme(style='dark', palette='rainbow')


# We can see that the both the datapoints of 0 and 1 and present close to each other, so choosing a correct k value of KNN Classifier is important

# In[51]:


# Now let's look into the summary of dataframe
df.describe()


# * For age feature we see that minimum age found in patient is 21 and maximum age of a patient is found to be 81
# * On an average, there are people who are aged at around 29-33 years are the patients

# In[60]:


print("minimum age of a patient who has been tested positive for diabetes", min(df['age'][df['class_cat']==1])) 
print("maximum age of a patient who has been tested positive for diabetes", max(df['age'][df['class_cat']==1])) 


# In[70]:


print("Number of patients who have been pregnant more than 2 times", df['n_pregnant'][df['n_pregnant'] > 2].count())
print("Number of patients who have been pregnant more than 3 times", df['n_pregnant'][df['n_pregnant'] > 3].count())
print("Number of patients who have been pregnant more than 4 times", df['n_pregnant'][df['n_pregnant'] > 4].count())


# In[73]:


# Let's look into how the distribution of target array
sns.distplot(df['class_cat'])
# We can see that the distribution is normal for both the categories


# In[78]:


sns.scatterplot(x=df['age'],y=df['bmi'], hue=df['class_cat'],data= df)
# we can see that younger patients has more BMI as compared to older people as expected
# But there are few outliers in the data


# * Now, it's time for ML Classification
# * First, we shall scale the data we have

# In[79]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# In[80]:


df.columns


# In[82]:


scaler.fit(df[['n_pregnant', 'plasma', 'pressure', 'skin', 'insulin', 'bmi', 'pedigree', 'age']])


# In[84]:


scaled_features = scaler.transform(df[['n_pregnant', 'plasma', 'pressure', 'skin', 'insulin', 'bmi', 'pedigree', 'age']])
scaled_features[:5]


# In[86]:


# Now we shall create X and y
X= pd.DataFrame(scaled_features, columns= df.columns[:-1])
y= df['class_cat']


# In[87]:


X[:5]   # scaled feature matrix


# In[88]:


y[:5] # target array


# In[90]:


# time to split the data into training set and testing set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.3, random_state= 42)


# In[91]:


# 1st we try KNN model with k=1 and see the accuracy
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 1)


# In[92]:


# We train the model now
model.fit(X_train, y_train)


# In[93]:


# We test the model now 
predict = model.predict(X_test)
predict[:5]


# In[94]:


y_test[:5]


# In[96]:


df['class_cat'].value_counts()


# In[95]:


# We will evaluate the model using confusion matrix
from sklearn.metrics import classification_report, confusion_matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, predict))

print("Classification report:")
print(classification_report(y_test, predict))


# * from the confusion matrix we see that, out of 151 category 0 labels, only 108 have been predicted correctly as cat 0 and 43 predicted wrongly as cat 1
# * which gives the accuracy of predicting the cat 0 is 0.71
# 
# * out of 80 category 1 labels, only 44 predcied wrongly as cat 0 and just 36 predicted correctly as cat 1
# * which gives the accuracy of predicting the cat 1 is 0.45
# 
# * So, for k=1, the overall acuuracy is just 0.62 or 62%

# In[97]:


# Now we shall choose a better k value 
error_rate = []


# In[98]:


for i in range(1,40):
  model_i = KNeighborsClassifier(n_neighbors=i)
  model_i.fit(X_train, y_train)
  predict_i = model_i.predict(X_test)
  error_rate.append(np.mean(predict_i != y_test))


# In[104]:


# We shall plot K values vs Error rate and choose the best value of k
sns.lineplot(x=range(1,40), y= error_rate)
sns.set_style('whitegrid')
plt.title("K values VS Error rate")
plt.xlabel("k values ---->")
plt.ylabel("Error rate ---->")


# **We can choose k=21, as it is having the least error rate**

# In[105]:


model_final = KNeighborsClassifier(n_neighbors=21)


# In[106]:


model_final.fit(X_train, y_train)


# In[107]:


predict_final = model_final.predict(X_test)


# In[108]:


predict_final[:5]


# In[109]:


y_test[:5]


# In[110]:


# Model Evaluation
# We will evaluate the model using confusion matrix
from sklearn.metrics import classification_report, confusion_matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, predict_final))

print("Classification report:")
print(classification_report(y_test, predict_final))


# * So finally we were able to achieve the maximum accuracy of 75%, which is actually bad
# 
# * Since the data had limited observations, accuracy of the model is low
