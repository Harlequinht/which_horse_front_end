import streamlit as st
import pandas as pd
import numpy as np

st.markdown("""
    <style>
    section[data-testid="stSidebar"][aria-expanded="true"]{
        height: 40% !important;
    }
    section[data-testid="stSidebar"][aria-expanded="false"]{
        height: 10% !important;
    }
    .st-emotion-cache-16txtl3 {
        padding: 2rem 1.5rem;
    }
    </style>""", unsafe_allow_html=True)

st.markdown('## Which Horse')

st.markdown('## Model 1')
@st.cache_data
def get_line_chart_data():

    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

df = get_line_chart_data()

st.line_chart(df)

st.markdown('## Model 2')
@st.cache_data
def get_line_chart_data():

    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

df = get_line_chart_data()

st.line_chart(df)

st.markdown('## Model 3')
@st.cache_data
def get_line_chart_data():

    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

df = get_line_chart_data()

st.line_chart(df)

st.markdown('## Model 4')
@st.cache_data
def get_line_chart_data():

    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

df = get_line_chart_data()

st.line_chart(df)

# Add more content as needed

# Sidebar navigation
st.sidebar.page_link('webapp.py', label='home')
st.sidebar.page_link('pages/about_us.py', label='about us')
st.sidebar.page_link('pages/which_horse.py', label='which horse')
st.sidebar.page_link('pages/our_model.py', label='our model')

#     # Define the pages
# pages = ['Home', 'About Us', 'Which Horse', 'Our Model']

# # Sidebar navigation
# selected_page = st.sidebar.selectbox('Navigation', pages)

# # Display content based on the selected page
# if selected_page == 'Home':
#     st.switch_page('webapp.py')
    
# elif selected_page == 'About Us':
#     st.switch_page('pages/about_us.py')

# elif selected_page == 'Which Horse':
#     st.switch_page('pages/which_horse.py')
    
# elif selected_page == 'Our Model':
    # st.switch_page('pages/our_model.py')
