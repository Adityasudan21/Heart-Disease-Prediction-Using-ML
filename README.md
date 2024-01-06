# Heart Disease Prediction 
**Discription**
The project aims to develop a machine learning model that predicts the likelihood of an individual developing heart disease based on a set of input parameters. This model will provide valuable insights for early intervention and proactive management of heart disease risk factors.  

## Project Goals:

Develop an accurate predictive model for heart disease assessment.
Create a user-friendly interface for data input and model utilization.
![Work_Flow](https://github.com/Adityasudan21/Heart-Disease-Prediction-Using-ML/blob/main/Images/Work%20Flow.png "Work_Flow")

### Dataset

Utilize a heart disease dataset from Kaggle containing relevant features and target labels.

### Machine Learning Model:

Implement the logistic regression algorithm for binary classification (heart disease or no heart disease).

## Features:

Include 11 key parameters as features, such as age, gender, cholesterol levels, blood pressure, and other relevant health indicators.

## Data Splitting:

Split the dataset into training, validation, and test sets, with a suitable ratio (e.g., 70% training, 15% validation, 15% test).

## Evaluation Metrics:

Assess model performance using metrics like accuracy, precision, recall, F1-score, and ROC AUC.

## Data Preprocessing:

Perform data cleaning, handling missing values, and scaling if necessary.
Encode categorical variables and normalize numerical features.

## Hyperparameter Tuning:

Optimize hyperparameters, such as regularization strength, using techniques like cross-validation.

## Model Training:

Train the logistic regression model using the training data and monitor convergence.

## Model Evaluation:

Evaluate the model on the validation and test sets, reporting key performance metrics.
Provide insights into model behavior and any observed patterns.

## Deployment:

Deploy the trained model, allowing users to input data and receive predictions.

Command to Run- streamlit run "C:\THAPAR\Sem5\Machine Learning\Lab\Project\heart_ui.py”
### User Interface:

Create a Streamlit-based graphical interface for user-friendly data input and model execution.

### Screenshots

![StreamLit UI](https://github.com/Adityasudan21/Heart-Disease-Prediction-Using-ML/blob/main/Images/Interface.png "StreamLit UI")

![Prone Test](https://github.com/Adityasudan21/Heart-Disease-Prediction-Using-ML/blob/main/Images/Prone.png "Prone Test")

### Conclusion

In conclusion, the "Heart Disease Prediction" project has successfully achieved its primary objectives, providing a robust and accurate predictive model for assessing the likelihood of individuals developing heart disease. Leveraging the logistic regression algorithm and a comprehensive dataset from Kaggle, we have created a valuable tool for early intervention and proactive management of heart disease risk factors.

The project includes a user-friendly interface developed with Streamlit, allowing users to input relevant health parameters and receive predictions promptly. Model evaluation on validation and test datasets yielded an impressive accuracy rate of 80.97%, indicating the reliability and effectiveness of the predictive algorithm.

Furthermore, we have taken measures to ensure data security and privacy compliance, particularly when dealing with sensitive health-related information. The project adheres to industry-standard best practices for data handling and model deployment.

As we move forward, opportunities for future enhancements exist, including exploring additional features, fine-tuning hyperparameters, and considering the integration of other machine learning algorithms to further improve prediction accuracy. The "Heart Disease Prediction" project represents a significant step in leveraging machine learning for healthcare decision-making and underscores the potential for data-driven solutions to benefit society's well-being.