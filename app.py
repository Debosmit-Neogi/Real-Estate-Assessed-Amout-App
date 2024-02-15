import streamlit as st
from prediction import predict
st.title('Predicting Sale Amount')
st.markdown('Prediction of Sale Amount of Real Estate')

st.header("Real Estate Features")
col1, col2 = st.columns(2)
with col1:

  List_Year = st.slider('List Year', 0, 20, 1)
  Year = st.slider('Year', 0, 22, 1)
  Town = st.slider('Town', 1, 200, 1)
  Month = st.slider('Month', 1, 12, 1)
  Residential_Type = st.slider('Residential Type', 1, 10, 1)
  Property_Type = st.slider('Property Type', 1, 10, 1)
  Assessed_Value = st.number_input('Enter Normalized Assessed Value')
# st.button("Predict Sale Amount")

if st.button("Predict Sale Amount"):
  data = [[List_Year, Year, Town, Month, Residential_Type, Property_Type, Assessed_Value]]
  result = predict(data)
  st.write('Predicted Sale Amount From Attributes:', result[0])