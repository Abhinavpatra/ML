
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import streamlit as st


def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns= iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_name = load_data()
model = RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

st.sidebar.title("Input features")

sepal_length = st.sidebar.slider("Sepal Length")
sepal_width = st.sidebar.slider("Sepal width")


st.write("Prediction")
st.write("bullshit")