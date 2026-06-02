import streamlit as st
import pandas as pd
import numpy as np

st.title("TITLE of Streamlit")

st.write("This is a simple text")

df = pd.DataFrame({
    'firstcol':[ 1, 2, 3, 4],
    'secondcol':[10, 20, 30, 40]
})

st.write("here is the dataframe")
st.write(df)


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

