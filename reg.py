import streamlit as st
import pandas as pd
import pickle
import time

st.title("Medical Cost Prediction")
st.markdown("This app predicts the medical cost based on user input features.")

#charger le modèle
with open('model.pkl','rb') as file:
    model = pickle.load(file)


#ajout de l'annimation de chargement
with st.spinner('Loading the model...'):
    time.sleep(2)

# Entrer les données de prédiction

col1, col2 = st.columns(2)
with col1:
    age = st.number_input('Age', min_value=0, max_value=120, value=30)
with col2:
    sex = st.selectbox('Sexe',['Male','Female'])

col3, col4 = st.columns(2)
with col3:
    bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=25.0)
with col4:
    children = st.slider('Number of Children', min_value=0, max_value=10, value=0)


col5, col6 = st.columns(2)
with col5:
    smoker = st.selectbox('Smoker?',['Yes','No'])
with col6:
    region = st.selectbox('Region',['northeast','northwest','southeast','southwest'])


sex_encoded = 1 if sex == 'male' else 0
smoker_encoded = 1 if smoker == 'yes' else 0
region_dict = {'northeast': 0.2423, 'northwest': 0.2423, 'southeast': 0.2722, 'southwest': 0.2430}
region_freq_encode = region_dict[region]

# preparation des données pour la prédiction
input_data = pd.DataFrame([[age, sex_encoded, bmi, children, smoker_encoded, region_freq_encode]],
                          columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region_freq_encode'])



# Prediction
if st.button('Predict Medical Cost'):
    with st.spinner('Predicting...'):
        Prediction = model.predict(input_data)[0]
        time.sleep(1)
    st.success(f'The predicted medical cost is: ${Prediction:.2f}')
    st.markdown("Developed by Calypso")