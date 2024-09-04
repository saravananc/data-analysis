import streamlit as st
import pandas as pd
st.title("🎈 My new app")

df= pd.read_csv("./sample-data-line.csv")
st.line_chart(df)