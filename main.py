import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from io import StringIO

# Load the CSV data from the provided link
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes-vid.csv"
response = requests.get(url)
data_csv = StringIO(response.text)
df = pd.read_csv(data_csv)

# Streamlit app
st.title("Diabetes Dashboard")

# Sidebar with interactive components
selected_outcome = st.sidebar.selectbox('Select Outcome:', df['Outcome'].unique())
age_filter = st.sidebar.slider('Filter by Age:', min_value=df['Age'].min(), max_value=df['Age'].max(),
                               value=(df['Age'].min(), df['Age'].max()))

# Filtered dataframe based on selected 'Outcome' and age range
filtered_df = df[(df['Outcome'] == selected_outcome) & (df['Age'] >= age_filter[0]) & (df['Age'] <= age_filter[1])]

# Display scatter plot
st.plotly_chart(px.scatter(filtered_df, x="BMI", y="BloodPressure", color="Age").update_traces(marker=dict(size=8)),
                use_container_width=True)

# Display histogram for 'Age' column
st.plotly_chart(
    px.histogram(filtered_df, x="Age", nbins=20, labels={'Age': 'Age (years)', 'Count': 'Number of Records'}),
    use_container_width=True)

# Display bar chart for count of each unique value in 'Outcome' column
st.plotly_chart(px.bar(filtered_df['Outcome'].value_counts(), x=filtered_df['Outcome'].unique(),
                       y=filtered_df['Outcome'].value_counts(),
                       labels={'x': 'Outcome', 'y': 'Count'}, title='Outcome Distribution').update_traces(
    marker_color='royalblue'), use_container_width=True)
