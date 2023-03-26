# 1) Import Modules
import csv
import streamlit as st
from PIL import Image
import pathlib

# Count number of data rows in csv file
nrows = 1

# Set page config
st.set_page_config(page_title='Home Page',layout='wide')


# Home Header
st.write('<h1 style = "text-align: center; margin-bottom: 48px;">Home</h1>', unsafe_allow_html=True)

# Create 2 X columns to lay out the apps
col1, col2 = st.columns(2, gap='small')

with col1:
    st.image('images/photo.jpg')

with col2:
        st.write('<h1 style = "font-size: 84px">Bobby Liu Ruming</h1>',unsafe_allow_html=True)
        st.write('<p style = "margin-bottom: 96px; font-size: 24px;">Bobby is a technology enthusiast who is eager to pursue Software Engineering as a profession'
                 'in the future. Audit"s Udemy course has been enriching so far, in that it taught me'
                 'many things from Python Basics to learning how to learn Python.'
                 'It is truly amazing to learn about applications of Python in areas such as '
                 'Web Development, App Development, Data Science, Automation. '
                 'I am excited to complete the Udemy course!</p>', unsafe_allow_html=True)

st.write("""
<h2 style = "text-align: center; margin-bottom: 32px;">Below you can find the apps that I have built throughout the course.</h2>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2, gap='small')

with open('data/data.csv') as csvfile:
    content = csv.reader(csvfile, delimiter=';')

    # Use `csv.Sniffer()` to check if csv file contains a header. Returns boolean
    hasHeader = csv.Sniffer().has_header(csvfile.read())

    # Rewind file reader to the start
    csvfile.seek(0)

    if hasHeader:
        # Skip the header row
        next(content)


    for index, row in enumerate(content):
        if (nrows <= 10):
            with col3:
                st.subheader(f'{index + 1}) {row[0]}')
                st.write(row[1])
                st.image(f'images/{row[-1]}')
                st.write('<a href ="https://google.com" style="color: black; font-weight: bold">Source Code</a>',unsafe_allow_html=True)

        else:
            with col4:
                st.subheader(f'{index + 1}) {row[0]}')
                st.write(row[1])
                st.image(f'images/{row[-1]}')
                st.write('<a href ="https://google.com" style="color: black; font-weight: bold">Source Code</a>',unsafe_allow_html=True)

        nrows += 1
