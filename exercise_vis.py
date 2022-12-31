import streamlit as st
import pandas as pd
import exercise
import datetime
import time
import plotly.express as px


URL = 'http://programmer100.pythonanywhere.com/'
SLEEP = 60
DURATION = 600
ITERATION = int(DURATION/SLEEP)



st.title('Weather App')

start = st.button('Start', key='bStart')
show_graph = st.button('Show Graph', key='bShow')
check_box = st.sidebar.checkbox(label="Display dataset")

if start:

    count = 1

    while count <= ITERATION:
        scraped = exercise.scrape(URL)
        value = exercise.extract_info(scraped)
        today_date = datetime.datetime.now()
        exercise.write_data(today_date.strftime('%d/%m/%Y %H:%M:%S')+ ',' + str(value)+'\n')
        time.sleep(SLEEP)   
        count += 1    

if show_graph:
    df = pd.read_csv('temp.csv')
    if check_box:
        st.subheader('Temperature Dataset')
        st.write(df)
    
    st.subheader('Plotting the graph')

    plot_fig = px.line(x = df['date'], y = df['temperature'], title='Temperature timeline', 
                        labels={'x': 'Date-Time', 'y': 'Temperature (C)'})

    st.plotly_chart(plot_fig)
    
