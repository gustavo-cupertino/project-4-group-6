****Cardiovascular Condition App****

***Introduction***:

Heart disease or cardiovascular disease is a widespread health issue in Canada, affecting millions of people. According to the Heart and Stroke Foundation of Canada, heart disease accounts for approximately 29% of all deaths in the country. Several risk factors contribute to the development of heart disease, including high blood pressure, high cholesterol levels, smoking, obesity, diabetes, sedentary lifestyle, poor diet, family history of heart disease, and age.

***Collaborators***:  

Bhuvana Krish, Gustavo Cupertino Marinho Pires, Varun Vinodh, Hardik Gehlot


***Objective***:

The objective of this project is to develop a machine learning-based app that can predict the likelihood of heart disease based on user input. The project aims to address the following tasks:

1. Explore the raw data and discover hidden insights.
2. Perform data wrangling and analysis using the Pandas library.
3. Create machine learning models using different steps of the machine learning pipeline.
4. Develop a web application using Streamlit, integrating the machine learning models into the app.
5. Enhance the app to enable prediction of heart disease based on user input.

***Data Collection***:

The original dataset used for this project was obtained from the Centers for Disease Control and Prevention (CDC) and is a major part of the 2020 Behavioral Risk Factor Surveillance System (BRFSS) Survey.

***Languages/Tools***:

1. Programming Language: Python.
2. Development Environment: Jupyter Notebook.
3. Data Manipulation and Analysis: Pandas Library.
4. Data Visualization: Tableau.
5. Machine Learning: Scikit-learn.
   - Random Forest.
   - Logistic Regression.
6. Web Application Development: Streamlit.

***Analysis***:

1. Data Exploration:
The raw data was explored to gain insights into the dataset. Visualizations were created using tools such as Tableau to analyze and understand the data better.

2. Machine Learning:
Since the dataset is binary and linear in nature, regression models were used to distinguish the data. Two models were explored:

   a. Random Forest Classifier:
      The random forest classifier model performed poorly in predicting the positive class ("1").
      
      ![Screenshot 2023-06-12 194604](https://github.com/gustavo-cupertino/project-4-group-6/assets/120690578/46ad1142-89a2-4f1f-b1ed-a5a31b29288d)


   b. Logistic Regression:
      The logistic regression model showed fair and equal predictions for both the positive and negative classes ("1" and "0").
      
     ![logisitic](https://github.com/gustavo-cupertino/project-4-group-6/assets/120690578/8cfea5d5-dc0f-4eec-99bb-bd2eeeaa63e7)


3. Streamlit App:
The project was deployed as a web application using Heroku. To use the app on a local machine, the necessary modules specified in the requirements.txt file should be installed. The app allows users to input relevant factors and receive a prediction of their heart health condition. It can be accessed by running the "streamlit run app.py" command.

***Conclusion***:

1. Machine learning has demonstrated significant potential in revolutionizing healthcare by enabling improved and early healthcare assessments.

2. Implementing machine learning in healthcare can facilitate early self-diagnosis of patient conditions, leading to quick recovery and potentially reducing healthcare costs and deaths due to late detection.

3. As the field of machine learning continues to evolve, its integration in healthcare holds promise for transforming the industry and delivering more effective and efficient healthcare services to individuals worldwide.

***References***:

Kaggle: https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease?resource=download
