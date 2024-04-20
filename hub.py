import streamlit as st
from sklearn.metrics import accuracy_score
import joblib
from streamlit_option_menu import option_menu
from tensorflow import keras
import tensorflow as tf
import pickle
import preprocess as pp
import numpy as np

with st.sidebar:
    selected = option_menu(
        menu_title="Hub",
        options=["Creator Info", "Dataset Info", "Dependencies Visualisation", "Prediction Tool(file)", "Prediction Tool(features)"],
        default_index=0,
        icons=[],
        styles={
            "nav-link-selected": {'background-color': 'purple'},
        },
    )

if selected == "Creator Info":
    st.title(f"Welcome to {selected}")

    st.header("***Developer's Name***")
    st.subheader("Kotov Sergey Vladimirovich")

    st.header("***Study Group***")
    st.subheader("FIT-222")

    st.header("***The Topic of CGW***")
    st.subheader('<<Development of a Web-application(dashboard) for ML model inference and data analysis>>')


if selected == "Dataset Info":
    st.title(f"Welcome to {selected}")

    st.header('**Dataset : "Diabetes Health Indicators Dataset"**')
    st.header('***Context:***')
    st.write('The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey that is collected annually by the CDC. Each year, the survey collects responses from over 400,000 Americans on health-related risk behaviors, chronic health conditions, and the use of preventative services. It has been conducted every year since 1984. For this project, a csv of the dataset available on Kaggle for the year 2015 was used. This original dataset contains responses from 441,455 individuals and has 330 features. These features are either questions directly asked of participants, or calculated variables based on individual participant responses.')
    st.header('***This dataset includes these columns:***')

    st.subheader('Diabetes_012')
    st.write('0 = no diabetes, 1 = prediabetes, 2 = diabetes')

    st.subheader('HighBp')
    st.write('0 = no high, BP 1 = high BP')

    st.subheader('HighChol')
    st.write('0 = no high cholesterol, 1 = high cholesterol')

    st.subheader('CholCheck')
    st.write('0 = no cholesterol check in 5 years, 1 = yes cholesterol check in 5 years')

    st.subheader('BMI')
    st.write('Body Mass Index')

    st.subheader('Smoker')
    st.write('Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] 0 = no 1 = yes')

    st.subheader('Stroke')
    st.write('(Ever told) you had a stroke. 0 = no, 1 = yes')

    st.subheader('HeartDiseaseorAttack')
    st.write('coronary heart disease (CHD) or myocardial infarction (MI) 0 = no, 1 = yes')

    st.subheader('PhysActivity')
    st.write('physical activity in past 30 days - not including job 0 = no 1 = yes')

    st.subheader('Fruits')
    st.write('Consume Fruit 1 or more times per day 0 = no, 1 = yes')

    st.subheader('Veggies')
    st.write('Consume Veggies 1 or more times per day 0 = no, 1 = yes')

    st.subheader('HvyAlcoholConsump')
    st.write('Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) 0 = no 1 = yes')

    st.subheader('AnyHealthcare')
    st.write('Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. 0 = no 1 = yes')

    st.subheader('NoDocbcCost')
    st.write('Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? 0 = no 1 = yes')

    st.subheader('GenHlth')
    st.write('Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor')

    st.subheader('MentHlth')
    st.write('Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? scale 1-30 days')

    st.subheader('PhysHlth')
    st.write('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? scale 1-30 days')

    st.subheader('DiffWalk')
    st.write('Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes')

    st.subheader('Sex')
    st.write('0 = female, 1 = male')

    st.subheader('Age')
    st.write('13-level age category (_AGEG5YR see codebook) 1 = 18-24 9 = 60-64 13 = 80 or older')

    st.subheader('Education')
    st.write('Education level (EDUCA see codebook) scale 1-6 1 = Never attended school or only kindergarten 2 = Grades 1 through 8 (Elementary) 3 = Grades 9 through 11 (Some high school) 4 = Grade 12 or GED (High school graduate) 5 = College 1 year to 3 years (Some college or technical school) 6 = College 4 years or more (College graduate)')

    st.subheader('Income')
    st.write('Income scale (INCOME2 see codebook) scale 1-8 1 = less than $10,000 5 = less than $35,000 8 = $75,000 or more')

if selected == "Dependencies Visualisation":
    st.title(f"Welcome to {selected}")

    st.header('Histogram of Values for each Column')
    st.image('imgs/hists.png')

    st.header('Correlation Heatmap')
    st.image('imgs/heatmap.png')

    st.header('Displot of Relation b/w Age and Diabetes')
    st.image('imgs/relation1.png')

    st.header('Countplot of Relation b/w BMI and Diabetes')
    st.image('imgs/relation2.png')

    st.header('Countplot of Relation b/w GenHealth and Diabetes')
    st.image('imgs/relation3.png')


if selected == "Prediction Tool(file)":
    st.title(f"Welcome to {selected}")
    st.header("Insert the .csv file and choose the model you'd like to use for prediction")

    uploaded_file = st.file_uploader("Insert the CSV-file", type="csv")
    df, y_test = pp.preprocess(uploaded_file)

    st.subheader('Choose one model from the list:')
    #selected_opt = st.checkbox(["GaussianNB", "GradientBoosting", "Bagging", "KMeans", "NW", "Stacking"])
    check1 = st.checkbox('GaussianNB')
    check2 = st.checkbox('Bagging')
    check3 = st.checkbox('GradientBoosting')
    check5 = st.checkbox('Stacking')
    check6 = st.checkbox('NW')

    if check1:
        with open('models/GaussianNB', 'rb') as file:
            model = pickle.load(file)
            predictions = model.predict(df)
            st.write("Accuracy score for GaussianNB:", accuracy_score(y_test, predictions))
    if check2:
        with open('models/Bagging', 'rb') as file:
            model = pickle.load(file)
            predictions = model.predict(df)
            st.write("Accuracy score for Bagging:", accuracy_score(y_test, predictions))
    if check3:
        with open('models/GradientBoosting', 'rb') as file:
            model = pickle.load(file)
            predictions = model.predict(df)
            st.write("Accuracy score for GradientBoosting:", accuracy_score(y_test, predictions))
    if check5:
        with open('models/Stacking', 'rb') as file:
            model = pickle.load(file)
            predictions = model.predict(df)
            st.write("Accuracy score for Stacking:", accuracy_score(y_test, predictions))
    if check6:
        model = tf.keras.models.load_model('models/NW_upd.h5')
        predictions = model.predict(df)
        accuracy = model.evaluate(df, y_test)
        st.write("Accuracy score for NW:", accuracy)


if selected == "Prediction Tool(features)":
    st.title(f"Welcome to {selected}")
    st.header("Defint the features and choose the model you'd like to use for prediction")

    a = st.slider("HighBP", 0, 1)
    b = st.slider("HighChol", 0, 1)
    c = st.slider("CholCheck", 0, 1)
    d = st.slider("BMI", 10, 100)
    e = st.slider("Smoker", 0, 1)
    f = st.slider("Stroke", 0, 1)
    g = st.slider("HeartDeseaseorAttack", 0, 1)
    h = st.slider("PhysActivity", 0, 1)
    i = st.slider("Fruits", 0, 1)
    j = st.slider("Veggies", 0, 1)
    k = st.slider("HvyAlcoholConsump", 0, 1)
    l = st.slider("AnyHealthcare", 0, 1)
    m = st.slider("NoDocbcCost", 0, 1)
    n = st.slider("GenHlth", 1, 5)
    o = st.slider("MentHlth", 0, 30)
    p = st.slider("PhysHlth", 0, 30)
    q = st.slider("DiffWalk", 0, 1)
    r = st.slider("Sex", 0, 1)
    s = st.slider("Age", 0, 13)
    t = st.slider("Education", 1, 6)
    u = st.slider("Income", 1, 8)

    features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]])

    st.subheader('Choose one model from the list:')
    #selected_opt = st.checkbox(["GaussianNB", "GradientBoosting", "Bagging", "KMeans", "NW", "Stacking"])
    check1 = st.checkbox('GaussianNB')
    check2 = st.checkbox('Bagging')
    check3 = st.checkbox('GradientBoosting')
    check5 = st.checkbox('Stacking')
    check6 = st.checkbox('NW')

    if check1:
        with open('models/GaussianNB', 'rb') as file:
            model = pickle.load(file)
            prediction = model.predict(features)
            st.subheader("Предсказанный диагноз:")
            if prediction == 0:
                st.write("Здоров")
            if prediction == 1:
                st.write("Преддиабет")
            if prediction == 2:
                st.write("Диабет")
    if check2:
        with open('models/Bagging', 'rb') as file:
            model = pickle.load(file)
            prediction = model.predict(features)
            st.subheader("Предсказанный диагноз:")
            if prediction == 0:
                st.write("Здоров")
            if prediction == 1:
                st.write("Преддиабет")
            if prediction == 2:
                st.write("Диабет")
    if check3:
        with open('models/GradientBoosting', 'rb') as file:
            model = pickle.load(file)
            prediction = model.predict(features)
            st.subheader("Предсказанный диагноз:")
            if prediction == 0:
                st.write("Здоров")
            if prediction == 1:
                st.write("Преддиабет")
            if prediction == 2:
                st.write("Диабет")
    if check5:
        with open('models/Stacking', 'rb') as file:
            model = pickle.load(file)
            prediction = model.predict(features)
            st.subheader("Предсказанный диагноз:")
            if prediction == 0:
                st.write("Здоров")
            if prediction == 1:
                st.write("Преддиабет")
            if prediction == 2:
                st.write("Диабет")
    if check6:
        model = tf.keras.models.load_model('models/NW_upd.h5')
        prediction = model.predict(features)
        st.subheader("Предсказанный диагноз:")
        if prediction == 0:
            st.write("Здоров")
        if prediction == 1:
            st.write("Преддиабет")
        if prediction == 2:
            st.write("Диабет")