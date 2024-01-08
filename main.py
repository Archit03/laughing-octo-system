import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from io import StringIO

# Load the CSV data from the provided link
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes-vid.csv"
response = requests.get(url)
data_csv = StringIO(response.text)
df = pd.read_csv(data_csv)

# Scatter plot using Plotly Express
scatter_plot = px.scatter(df, x="BMI", y="BloodPressure", color="Age",
                          labels={'Age': 'Age (years)', 'BMI': 'BMI', 'BloodPressure': 'Blood Pressure'})

# Histogram for 'Age' column
age_histogram = px.histogram(df, x="Age", nbins=20, labels={'Age': 'Age (years)', 'Count': 'Number of Records'})

# Bar chart for count of each unique value in 'Outcome' column
outcome_counts_bar = px.bar(df['Outcome'].value_counts(), x=df['Outcome'].unique(), y=df['Outcome'].value_counts(),
                            labels={'x': 'Outcome', 'y': 'Count'}, title='Outcome Distribution')

# Streamlit app
st.title("Diabetes Dashboard")

# Dropdown for filtering based on 'Outcome' column
selected_outcome = st.selectbox('Select Outcome:', df['Outcome'].unique())

# Filtered dataframe based on selected 'Outcome'
filtered_df = df[df['Outcome'] == selected_outcome]

# Display scatter plot
st.plotly_chart(scatter_plot.update_traces(marker=dict(size=8)), use_container_width=True)

# Display histogram for 'Age' column
st.plotly_chart(age_histogram, use_container_width=True)

# Display bar chart for count of each unique value in 'Outcome' column
st.plotly_chart(outcome_counts_bar.update_traces(marker_color='royalblue'), use_container_width=True)
