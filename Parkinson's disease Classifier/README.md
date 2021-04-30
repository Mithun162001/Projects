<h1>Problem Statement provided by Great Learning</h1>

<h2>Data Description & Context:</h2>
<p>
Parkinson’s Disease (PD) is a degenerative neurological disorder marked by decreased dopamine levels in the brain. It manifests itself through a deterioration of movement, including the presence of tremors and stiffness. There is commonly a marked effect on speech, including dysarthria (difficulty articulating sounds), hypophonia (lowered volume), and monotone (reduced pitch range). Additionally, cognitive impairments and changes in mood can occur, and risk of dementia is increased.
Traditional diagnosis of Parkinson’s Disease involves a clinician taking a neurological history of the patient and observing motor skills in various situations. Since there is no definitive laboratory test to diagnose PD, diagnosis is often difficult, particularly in the early stages when motor effects are not yet severe. Monitoring progression of the disease over time requires repeated clinic visits by the patient. An effective screening process, particularly one that doesn’t require a clinic visit, would be beneficial. Since PD patients exhibit characteristic vocal features, voice recordings are a useful and non-invasive tool for diagnosis. If machine learning algorithms could be applied to a voice recording dataset to accurately diagnosis PD, this would be an effective screening step prior to an appointment with a clinician
</p>

<h2>Domain: Medicine</h2>

<h2>Attribute Information:<h2>
<p>
<ul>
<li>name - ASCII subject name and recording number
<li>MDVP:Fo(Hz) - Average vocal fundamental frequency
<li>MDVP:Fhi(Hz) - Maximum vocal fundamental frequency
<li>MDVP:Flo(Hz) - Minimum vocal fundamental frequency
<li>MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several measures of variation in fundamental frequency
<li>MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,S
<li>himmer:DDA - Several measures of variation in amplitude
<li>NHR,HNR - Two measures of ratio of noise to tonal components in the voice
<li>status - Health status of the subject (one) - Parkinson's, (zero) - healthy
<li>RPDE,D2 - Two nonlinear dynamical complexity measures
<li>DFA - Signal fractal scaling exponent
<li>spread1,spread2,PPE - Three nonlinear measures of fundamental frequency
variation 9. 
<li>car name: string (unique for each instance)
</ul>
</p>
  
<h2>Learning Outcomes:</h2>
<ul>
<li>Exploratory Data Analysis
<li>Supervised Learning
<li>Ensemble Learning
</ul>

<h2>Objective:</h2>
<p>Goal is to classify the patients into the respective lables using the attributes form their voice recordings</p>

<h2>Steps and Tasks:</h2>
<p>
<ol>
<li>Load the dataset
<li>It is always a good practice to eye-ball raw data to get a feel of the data in
terms of number of records, structure of the file, number of attributes, types of attributes and a general idea of likely challenges in the dataset. Mention a few comments in this regard (5 points)
<li>Using univariate & bivariate analysis to check the individual attributes for their basic statistics such as central values, spread, tails, relationships between variables etc. mention your observations (15 points)
<li>Split the dataset into training and test set in the ratio of 70:30 (Training:Test) (5 points)
<li>Prepare the data for training - Scale the data if necessary, get rid of missing values (if any) etc (5 points)
<li>Train at least 3 standard classification algorithms - Logistic Regression, Naive Bayes’, SVM, k-NN etc, and note down their accuracies on the test data (10 points)
<li>Train a meta-classifier and note the accuracy on test data (10 points)
<li>Train at least one standard Ensemble model - Random forest, Bagging, Boosting etc, and note the accuracy (10 points)
<li>Compare all the models (minimum 5) and pick the best one among them (10 points)
</ol>
</p>
