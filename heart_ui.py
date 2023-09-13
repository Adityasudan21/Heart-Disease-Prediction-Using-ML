import pickle
import streamlit as st
st.set_page_config(page_title="Heart Disease Predictor",
                   page_icon=":heart:", layout="wide")
# loading the saved models
heart_disease_model = pickle.load(open(
    'C:/THAPAR/Sem5/Machine Learning/Lab/Project/heart_disease_model.sav', 'rb'))
# page title
st.title('Heart Disease Prediction')
st.write("Please Enter the Following details ")
col1, col2 = st.columns(2)

with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex (M-Male/F-Female)')

with col1:
    cp = st.text_input('Chest Pain types (ATA/NAP/ASY/TA)')

with col2:
    trestbps = st.text_input('Resting Blood Pressure')

with col1:
    chol = st.text_input('Serum Cholestoral in mg/dl')

with col2:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
    restecg = st.text_input('Resting Electrocardiographic results (Normal/ST)')

with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')

with col1:
    exang = st.text_input('Exercise Induced Angina Y-YES N-NO')

with col2:
    oldpeak = st.text_input('ST depression induced by exercise')

with col1:
    slope = st.text_input('Slope of the peak exercise ST segment (UP/Flat)')

with col1:
    # code for Prediction
    heart_diagnosis = ''
    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        if sex == 'M':
            sex = 1
        else:
            sex = 0

        if(exang == 'Y'):
            exang = 1
        else:
            exang = 0

        if(cp == 'ATA'):
            cp = 1
        elif(cp == 'NAP'):
            cp = 2
        elif(cp == 'ASY'):
            cp = 3
        else:
            cp = 0

        if(slope == 'Up'):
            slope = 1
        else:
            slope = 0

        if(restecg == 'Normal'):
            restecg = 1
        else:
            restecg = 0
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is prone to heart disease'
        else:
            heart_diagnosis = 'The person is not prone to any heart disease'

    st.success(heart_diagnosis)
st.write("ML Project By Aditya Sudan, Akshita Tayal ")
st.write("[Learn More about the Dataset Used >](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)")
