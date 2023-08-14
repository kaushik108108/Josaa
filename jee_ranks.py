import streamlit as st
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob', 'Emily'],
    'Age': [25, 30, 22, 28]
})

# UI elements
st.title('Filtering App')
age_range = st.slider('Select Age Range', min_value=0, max_value=100, value=(0, 100))
filtered_data = data[(data['Age'] >= age_range[0]) & (data['Age'] <= age_range[1])]

# Display filtered results
st.write('Filtered Results:')
st.dataframe(filtered_data)
