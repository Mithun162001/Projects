<h1 align="left">What is Cancer?</h1>
<h3 align="left">Cancer is an abnormal growth of cells. Cancer cells rapidly reproduce despite restriction of space, nutrients shared by other cells, or signals sent from the body to stop reproduction. Cancer cells are often shaped differently from healthy cells, they do not function properly, and they can spread to many areas of the body. Tumors, abnormal growth of tissue, are clusters of cells that are capable of growing and dividing uncontrollably; their growth is not regulated. </h3>

-Tumors can be benign (noncancerous) or malignant (cancerous). 
- Benign tumors tend to grow slowly and do not spread. 
- Malignant tumors can grow rapidly, invade and destroy nearby normal tissues, and spread throughout the body.

# How it affects
<p align="center">
<img src="https://media.giphy.com/media/g0LLQH1rVf4xlGB5jD/giphy.gif" width="50%"></p>

# Aim of the Project
- To classify the patients based on their features and observation records whether they have cancerous cells in the body or not

# Description of project
- Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. 
- They describe characteristics of the cell nuclei present in the image.
- This database can be found on UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

# Attribute Information:-
1) ID number
2) Diagnosis (M = malignant, B = benign)
3-32)

Ten real-valued features are computed for each cell nucleus:

a) radius (mean of distances from center to points on the perimeter)

b) texture (standard deviation of gray-scale values)

c) perimeter

d) area

e) smoothness (local variation in radius lengths)

f) compactness (perimeter^2 / area - 1.0)

g) concavity (severity of concave portions of the contour)

h) concave points (number of concave portions of the contour)

i) symmetry

j) fractal dimension ("coastline approximation" - 1)

- The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius.
- All feature values are recoded with four significant digits.

