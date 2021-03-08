import streamlit as st

import pandas as pd

import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from pickle import load
import numpy as np
from sklearn import metrics

st.markdown('<style>body{background-color:lightblue;}</style>',unsafe_allow_html=True)

st.sidebar.title('Description')
username = st.sidebar.text_input("Observation")
password = st.sidebar.text_input('Final Verdict')

st.markdown("<h1 style='text-align: center; color: red;'>Data Prediction</h1>", unsafe_allow_html=True)
dataset_loc = "data/train.csv"

@st.cache
def load_data(dataset_loc):
    df = pd.read_csv(dataset_loc)
    return df

def load_description(df):
        # Preview of the dataset
        st.header("Data Preview")
        preview = st.radio("Choose Head/Tail?", ("Top", "Bottom"))
        if(preview == "Top"):
            st.write(df.head())
        if(preview == "Bottom"):
            st.write(df.tail())

        # display the whole dataset
        if(st.checkbox("Show complete Dataset")):
            st.write(df)

        # Show shape
        if(st.checkbox("Display the shape")):
            st.write(df.shape)
            dim = st.radio("Rows/Columns?", ("Rows", "Columns"))
            if(dim == "Rows"):
                st.write("Number of Rows", df.shape[0])
            if(dim == "Columns"):
                st.write("Number of Columns", df.shape[1])

        # show columns
        if(st.checkbox("Show the Columns")):
            st.write(df.columns)






def main():

    #
    # loading the data
    df = load_data(dataset_loc)
    # display description
    load_description(df)


if(__name__ == '__main__'):
    main()

def display_info():
    column_names=['col1','col2']
    df = pd.DataFrame(columns = column_names)
    col1=st.number_input("Enter your col1 values", -1000.0, 1000.0)
    col2=st.number_input("Enter your col2 values", -1000.0, 1000.0)
    dict1 = {'col1': col1, 'col2': col2}
    df = df.append(dict1, ignore_index = True)
    return df



def predict(df):
    x=df
    x_test=np.array(x)
    classifier=load(open('Pickle/dump.pkl','rb'))
    predictions = classifier.predict(np.array(x_test))
    return predictions

def main():
    dataframe=display_info()
    click = st.button('SUBMIT')
    if click:
        Predictions=predict(dataframe)
        if Predictions==0:
            st.write('zero:cry:')
        else:
            st.write('one:sunglasses:')
if(__name__=='__main__'):
    main()
