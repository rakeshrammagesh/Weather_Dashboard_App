import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the next few days")
place = st.text_input("Place:  ")
days = st.slider("Forecast Days", min_value = 1, max_value = 5, help = "Select the number if forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f" {option} for the next {days} days in {place}")


#use the command prompt option in the terminal press right click


dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
temperatures = [10, 11, 15]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(c)"})
st.plotly_chart(figure)
