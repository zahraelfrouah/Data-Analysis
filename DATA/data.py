import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

###--- create header , subheader
st.set_page_config(page_title='Data Visualization')
st.header('Covid Worldwide')
st.subheader('covid worldwide dashboard')

####--- LOAD DATAFRAME
df_csv = pd.read_csv('covid.csv')
df_csv

#---create pd.dataframe
my_dataframe = pd.DataFrame({
    'Country': ['France', 'Germany', 'Japan', 'Brazil', 'S.korea'],
    'Total Cases':[39.524, 37.779, 32.588, 36.824, 30.197],
    'Total Deaths': [164.233, 165.711, 697.074, 68.399, 33.486]
})
st.bar_chart(my_dataframe)

#---create a pie chart 
data = [104, 1.132, 101]
labels = ["Total cases" , "Total deaths" , "Total recoverd"]
fig, ax = plt.subplots()
ax.pie(data, labels=labels, colors=['#BFACE2', '#5BC0F8', 'pink'], autopct='%.1f%%')
ax.set_title('Covid worldwide')
st.pyplot(fig)