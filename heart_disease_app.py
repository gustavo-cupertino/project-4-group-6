import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn


DATASET_PATH = "../testing/Resources/data_cleaned.csv"
LOG_MODEL_PATH = "lr_model.pkl"

def calculate_bmi(weight, height):
    bmi = weight / ((height/100) ** 2)
    return bmi

def main():
    @st.cache_data(persist=True)
    def load_dataset() -> pd.DataFrame:
        heart_df = pd.read_csv(DATASET_PATH)
        heart_df = pd.DataFrame(np.sort(heart_df.values, axis=0),
                                index=heart_df.index,
                                columns=heart_df.columns)
        return heart_df

    def user_input_features() -> pd.DataFrame:
        race = st.sidebar.selectbox("Race", options=(race for race in heart.Race.unique()))
        sex = st.sidebar.selectbox("Sex", options=(sex for sex in heart.Sex.unique()))
        age_cat = st.sidebar.selectbox("Age category",
                                       options=(age_cat for age_cat in heart.AgeCategory.unique()))
        bmi_cat = st.sidebar.selectbox("BMI category",
                                       options=(bmi_cat for bmi_cat in heart.BMICategory.unique()))
        gen_health = st.sidebar.selectbox("How can you define your general health?",
                                          options=(gen_health for gen_health in heart.GenHealth.unique()))
        phys_act = st.sidebar.selectbox("Have you played any sports (running, biking, etc.)"
                                        " in the past month?", options=("No", "Yes"))
        smoking = st.sidebar.selectbox("Have you smoked at least 100 cigarettes in"
                                       " your entire life (approx. 5 packs)?)",
                                       options=("No", "Yes"))
        alcohol_drink = st.sidebar.selectbox("Do you have more than 14 drinks of alcohol (men)"
                                             " or more than 7 (women) in a week?", options=("No", "Yes"))
        stroke = st.sidebar.selectbox("Did you have a stroke?", options=("No", "Yes"))
        diff_walk = st.sidebar.selectbox("Do you have serious difficulty walking"
                                         " or climbing stairs?", options=("No", "Yes"))
        diabetic = st.sidebar.selectbox("Have you ever had diabetes?",
                                        options=("No", "Yes"))
        asthma = st.sidebar.selectbox("Do you have asthma?", options=("No", "Yes"))
        kid_dis = st.sidebar.selectbox("Do you have kidney disease?", options=("No", "Yes"))
        skin_canc = st.sidebar.selectbox("Do you have skin cancer?", options=("No", "Yes"))
        columns = ['Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex',
                   'Diabetic', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer',
                   'BMICategory_Normal weight (18.5 <= BMI < 25.0)',
                   'BMICategory_Obese (30.0 <= BMI)',
                   'BMICategory_Overweight (25.0 <= BMI < 30.0)',
                   'BMICategory_Underweight (BMI < 18.5)', 'AgeCategory_18-24',
                   'AgeCategory_25-29', 'AgeCategory_30-34', 'AgeCategory_35-39',
                   'AgeCategory_40-44', 'AgeCategory_45-49', 'AgeCategory_50-54',
                   'AgeCategory_55-59', 'AgeCategory_60-64', 'AgeCategory_65-69',
                   'AgeCategory_70-74', 'AgeCategory_75-79', 'AgeCategory_80 or older',
                   'Race_American Indian/Alaskan Native', 'Race_Asian', 'Race_Black',
                   'Race_Hispanic', 'Race_Other', 'Race_White', 'GenHealth_Excellent',
                   'GenHealth_Fair', 'GenHealth_Good', 'GenHealth_Poor',
                   'GenHealth_Very good']
        num_rows = 1
        num_cols = len(columns)
        df = pd.DataFrame(0, index=range(num_rows), columns=columns)

        df["BMICategory_" + bmi_cat] = 1
        df["Smoking"] = (0 if smoking == "No" else 1)
        df["AlcoholDrinking"] = (0 if alcohol_drink == "No" else 1)
        df["Stroke"] = (0 if stroke == "No" else 1)
        df["DiffWalking"] = (0 if diff_walk == "No" else 1)
        df["Sex"] = (0 if sex == "Female" else 1)
        df["AgeCategory_" + age_cat] = 1
        df['GenHealth_' + gen_health] = 1
        df["Race_" + race] = 1
        df["Diabetic"] = (0 if diabetic == "No" else 1)
        df["PhysicalActivity"] = (0 if phys_act == "No" else 1)
        df["GenHealth"] = (0 if gen_health == "No" else 1)
        df["Asthma"] = (0 if asthma == "No" else 1)
        df["KidneyDisease"] = (0 if kid_dis == "No" else 1)
        df["SkinCancer"] = (0 if skin_canc == "No" else 1)

        # print(df.to_markdown())
        return df

    st.set_page_config(
        page_title="Heart Disease Prediction App",
        page_icon="🩺"
    )

    st.title("Heart Disease Prediction")
    st.subheader("Are you wondering about the condition of your heart? "
                 "This app will help you diagnose it!")

    st.markdown("""
    To predict your heart disease status, simply follow the steps below:
    1. Enter the parameters that best describe you.
    2. Press the Predict button and wait for the result on the 'Home' tab.
     """)

    # Add tabs to the sidebar
    tab = st.sidebar.radio("Navigation", ["Home", "BMI calculator", "About"])

    if tab == "Home":
        st.image("images/doctor.gif",
                 caption="I'll help you diagnose your heart health! - Dr. Logistic Regression",
                 width=200,
                )
    submit = st.button("Predict")

    if tab == "About":
        # Display the about page content
        st.markdown("""
        Did you know that machine learning models can help you
        predict heart disease pretty accurately? In this app, you can
        estimate your chance of heart disease (yes/no) in seconds!
        
        This a logistic regression model that uses an undersampling technique and
        was constructed using survey data of over 300k US residents from the year 2020.
        This application is based on it because it has proven to be better than the random forest
        (it achieves an accuracy of about 80%).
        
        To predict your heart disease status, simply follow the steps below:
        1. Enter the parameters that best describe you;
        2. Press the "Predict" button and wait for the result.         
            
        **Keep in mind that this result is not equivalent to a medical diagnosis!
        This model would never be adopted by healthcare facilities because of its less
        than perfect accuracy, so if you have any problems, consult a human doctor.**
        
        **Original app designed by: Kamil Pytlak ([GitHub](https://github.com/kamilpytlak/))**
        
        You can see the steps of building the model, evaluating it, and cleaning the data itself
        on my GitHub repo [here](https://github.com/gustavo-cupertino/project-4-group-6). 
        """)

    if tab == "BMI calculator":
        st.subheader("BMI Calculator")
        weight = st.number_input("Weight (in kg)")
        height = st.number_input("Height (in cm)")

        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.markdown(f"Your BMI: {bmi:.2f}")
        else:
            st.markdown("Please enter valid weight and height values.")

    heart = load_dataset()

    st.sidebar.title("Feature Selection")

    df = user_input_features()

    df = df[['Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex',
             'Diabetic', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer',
             'BMICategory_Normal weight (18.5 <= BMI < 25.0)',
             'BMICategory_Obese (30.0 <= BMI)',
             'BMICategory_Overweight (25.0 <= BMI < 30.0)',
             'BMICategory_Underweight (BMI < 18.5)', 'AgeCategory_18-24',
             'AgeCategory_25-29', 'AgeCategory_30-34', 'AgeCategory_35-39',
             'AgeCategory_40-44', 'AgeCategory_45-49', 'AgeCategory_50-54',
             'AgeCategory_55-59', 'AgeCategory_60-64', 'AgeCategory_65-69',
             'AgeCategory_70-74', 'AgeCategory_75-79', 'AgeCategory_80 or older',
             'Race_American Indian/Alaskan Native', 'Race_Asian', 'Race_Black',
             'Race_Hispanic', 'Race_Other', 'Race_White', 'GenHealth_Excellent',
             'GenHealth_Fair', 'GenHealth_Good', 'GenHealth_Poor',
             'GenHealth_Very good']]
    df = df[:1]
    df.fillna(0, inplace=True)
    # print(df.values.tolist())
    log_model = pickle.load(open(LOG_MODEL_PATH, "rb"))

    if submit:
        prediction = log_model.predict(df)
        prediction_prob = log_model.predict_proba(df)
        if prediction == 0:
            st.markdown(f"**The probability that you'll have"
                        f" heart disease is low at {round(prediction_prob[0][1] * 100, 2)}%."
                        f" You are healthy!**")
            st.image("images/heart-okay.jpg",
                     caption="Your heart seems to be okay! - Dr. Logistic Regression")
        else:
            st.markdown(f"**The probability that you will have"
                        f" heart disease is high at {round(prediction_prob[0][1] * 100, 2)}%."
                        f" You should consult a doctor.**")
            st.image("images/heart-not-okay.jpg",
                     caption="You may need medical attention! - Dr. Logistic Regression")

if __name__ == '__main__':
    main()
