# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:31:22 2022

@author: chand
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open("C:/Users/chand/OneDrive/Desktop/project/spy/models/diabetes_model.sav", "rb"))

heart_disease_model = pickle.load(open("C:/Users/chand/OneDrive/Desktop/project/spy/models/heart_disease_model.sav", "rb"))

parkinsons_model = pickle.load(open("C:/Users/chand/OneDrive/Desktop/project/spy/models/parkinsons_model.sav", "rb"))

bcancer_model = pickle.load(open("C:/Users/chand/OneDrive/Desktop/project/spy/models/breast_cancer_model.sav", "rb"))
#sidebar

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction'],
                          icons=['activity','heart','person','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
if (selected == "Breast Cancer Prediction"):
    st.title("Breast Cancer Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        mean_radius = st.text_input('Enter the mean of distances from center to points on the perimeter')
    with col2:
        mean_texture = st.text_input('Enter standard deviation of gray-scale values')
    with col1:
        mean_perimeter = st.text_input('Enter mean size of the core tumor')
    with col2:
        mean_area = st.text_input('Enter area mean')
    with col1:
        mean_smoothness = st.text_input('Enter mean of local variation in radius lengths')
    with col2:
        mean_compactness = st.text_input('Enter mean of perimeter')
    with col1:
        mean_concavity = st.text_input('Enter mean of severity of concave portions of the contour')
    with col2:
        mean_concave_points = st.text_input('Enter mean for number of concave portions of the contour')
    with col1:
        mean_symmetry = st.text_input('Enter mean symmetry')
    with col2:
        mean_fractal_dimension = st.text_input('Enter mean for "coastline approximation" - 1')
    with col1:
        radius_error = st.text_input('Enter standard error for the mean of distances from center to points on the perimeter')
    with col2:
        texture_error = st.text_input('Enter standard error for standard deviation of gray-scale values')
    with col1:
        perimeter_error = st.text_input('Enter perimeter error')
    with col2:
        area_error = st.text_input('Enter area error')
    with col1:
        smoothness_error = st.text_input('Enter standard error for local variation in radius lengths')
    with col2:
        compactness_error = st.text_input('Enter standard error for perimeter^2 / area - 1.0')
    with col1:
        concavity_error = st.text_input('Enter standard error for severity of concave portions of the contour')
    with col2:
        concave_points_error = st.text_input('standard error for number of concave portions of the contour')
    with col1:
        symmetry_error = st.text_input('symmetry error')
    with col2:
        fractal_dimension_error = st.text_input('standard error for "coastline approximation" - 1')
    with col1:
        worst_radius = st.text_input('"worst" or largest mean value for mean of distances from center to points on the perimeter')
    with col2:
        worst_texture = st.text_input('"worst" or largest mean value for standard deviation of gray-scale values')
    with col1:
        worst_perimeter = st.text_input('wrost perimeter')
    with col2:
        worst_area = st.text_input('wrost area')
    with col1:
        worst_smoothness = st.text_input('"worst" or largest mean value for local variation in radius lengths')
    with col2:
        worst_compactness = st.text_input('"worst" or largest mean value for perimeter^2 / area - 1.0')
    with col1:
        worst_concavity = st.text_input('"worst" or largest mean value for severity of concave portions of the contour')
    with col2:
        worst_concave_points = st.text_input('"worst" or largest mean value for number of concave portions of the contour')
    with col1:
        worst_symmetry = st.text_input('wrost symmetry')
    with col2:
        worst_fractal_dimension = st.text_input('"worst" or largest mean value for "coastline approximation" - 1')
        
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        Breast_Cancer_prediction = bcancer_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]])                          
        
        if (Breast_Cancer_prediction[0] == 0):
          breast_cancer_diagnosis = 'The Breast cancer is Malignant'
        else:
          breast_cancer_diagnosis = 'The Breast Cancer is Benign'
        
    st.success(breast_cancer_diagnosis)



    