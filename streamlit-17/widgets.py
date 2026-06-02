import streamlit as st
import pandas as pd

st.title("Streamlit input")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}")
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose a language:", options,None)
st.write(f"You have selected: {choice}.")
if name:
    st.write(f"Hello, {name}")

data = {
    "Name":["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City":["New York", "Los Angeles", "Chicago", "Houston"]
}

# df = pd.DataFrame(data)
# df.to_csv("sample.csv")
# st.write(df) # converts it to a dataframe

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
