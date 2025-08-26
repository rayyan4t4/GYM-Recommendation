💪 Personalized Workout & Diet Recommender
A smart, data-driven recommendation system that generates personalized workout routines, equipment suggestions, and diet plans based on user-specific health data and fitness goals.

🌟 Overview
This project leverages machine learning to provide tailored fitness recommendations. By inputting key personal metrics such as age, sex, BMI, and health conditions (like hypertension or diabetes), users receive a complete fitness plan. The system uses a Random Forest Classifier to predict the most suitable exercises, equipment, and dietary guidelines from a comprehensive dataset.

The goal is to eliminate the guesswork in fitness by providing a clear, actionable, and personalized path for users to achieve their health objectives, whether it's weight loss, weight gain, or muscle building.

✨ Key Features
Personalized Recommendations: Get custom suggestions for exercises, gym equipment, and diet plans.

Health-Aware: The model takes into account crucial health factors like hypertension and diabetes to provide safe and effective recommendations.

Goal-Oriented: Tailors recommendations based on the user's primary fitness goal (e.g., Weight Gain, Weight Loss).

Data-Driven: Built on a dataset of over 14,000 entries to ensure robust and varied suggestions.

Multi-Output Model: Predicts three distinct outputs (Exercises, Equipment, Diet) from a single user input.

🛠️ Technology Stack
This project is built using the following technologies and libraries:

Language: Python

Core Libraries:

Pandas: For data manipulation and loading the dataset from the .xlsx file.

Scikit-learn: For building and training the machine learning models (RandomForestClassifier, LabelEncoder).

NumPy: For numerical operations.

Development Environment: Jupyter Notebook

🚀 How It Works
The recommendation logic is powered by three distinct RandomForestClassifier models, each trained for a specific purpose:

Input Data: The system takes the following user attributes as input:

Sex (Male/Female)

Age

Hypertension (Yes/No)

Diabetes (Yes/No)

BMI (Body Mass Index)

Fitness Goal (e.g., Weight Gain)

Data Preprocessing: Categorical features like Sex and Fitness Goal are converted into numerical format using LabelEncoder.

Prediction: The processed input is fed into three trained models:

ex_model: Predicts the optimal set of Exercises.

eq_model: Recommends the necessary Equipment.

diet_model: Suggests a suitable Diet plan.

Output: The system returns a dictionary containing the complete, personalized recommendation.

Model Performance
The models achieved the following accuracies on the test set:

Exercises Model Accuracy: ~99.6%

Equipment Model Accuracy: ~92.1%

Diet Model Accuracy: ~68.3%

