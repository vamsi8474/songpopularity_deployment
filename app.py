###### Libraries #######
# Base Libraries
import pandas as pd
import numpy as np

# Deployment Library
import streamlit as st

# Model Pickled File Library
import joblib

############# Data File ###########
data = pd.read_excel('DataTrain.xlsx',sheet_name="Data")
data = data.dropna(axis=0).reset_index(drop=True)

########### Loading Trained Model Files ########
model = joblib.load("songsdeployment.pkl")

# Title
st.title(" estimation of songs popularity score using song features:")

# Description
st.write("""Built a Predictive model in Machine Learning to estimate the songs popularity score.
         Sample Data taken as below shown.
""")
# Data Display
st.dataframe(data.head())
st.write("From the above data , popularity score is the prediction variable")

###### Taking User Inputs #########
st.subheader("Enter Below Details to Get the Estimation of song popularityscore:")

col1, col2, col3 = st.columns(3) # value inside brace defines the number of splits
col4, col5, col6 = st.columns(3)


with col1:
    SongLength = st.number_input("Enter SongLength:")
    st.write(SongLength)

with col2:
    NumInstruments = st.number_input("Enter NumInstruments:")
    st.write(NumInstruments)

with col3: 
    Genre = st.selectbox("Enter Genre:", data.Genre.unique())
    st.write(Genre)

with col4:
    Tempo = st.number_input("Enter Tempo:")
    st.write(Tempo)

with col5:
    LyricalContent = st.number_input("Enter tLyricalContent:")
    st.write(LyricalContent)

with col6:
    ReleasedYear = st.selectbox("Enter ReleasedYear:",data.ReleasedYear.unique())
    st.write(ReleasedYear)


###### Predictions #########

if st.button("Estimate"):
    st.write("Data Given:")
    values = [SongLength,NumInstruments,Genre,Tempo,LyricalContent]
    record =  pd.DataFrame([values],
                           columns = ['SongLength','NumInstruments','Genre','Tempo','LyricalContent'])
    st.dataframe(record)
    popularity = round(model.predict(record)[0],2)
    st.subheader("Estimated popularityscore:")
    st.subheader(popularity)