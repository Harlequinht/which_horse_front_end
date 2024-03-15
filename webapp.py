import streamlit as st
from tensorflow.keras.models import load_model
from keras.utils import get_custom_objects
from custom_loss import custom_loss_function
import pickle
import base64


def main():
    # Set the page configuration
    st.set_page_config(
        page_title="home",
        layout="wide",
        initial_sidebar_state="collapsed",
        page_icon=":horse:"
    )

if __name__ == "__main__":
    main()
    
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
# Your data loading and cleaning functions go here

# Loading pipeline
pipe = pickle.load(open('softmax_pipeline.pkl', 'rb'))

# Loading model
get_custom_objects().update({"custom_loss_function": custom_loss_function})
model = load_model('softmax.h5', custom_objects = {"custom_loss_function": custom_loss_function})

def load_pipe_model():
    return pipe, model

# Define the pages
pages = ['Home', 'About Us', 'Which Horse', 'Our Model']

# Sidebar navigation
# selected_page = st.sidebar.selectbox('Navigation', pages)


# Display content based on the selected page
# if selected_page == 'Home':
    
# st.switch_page('pages/home.py')
# @st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
        <style>
        .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size:  cover;
            background-repeat: no-repeat;
            background-color: transparent;
            background-position: center
        }
        </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('images/horse_racing.jpg')


# st.markdown('## Which Horse')
col1, inter_cols_pace = st.columns((3, 2))
with inter_cols_pace:
    with st.container():
        title = "Which Horse"
        content = """Horse racing holds significant economic and entertainment value, attracting widespread attention from enthusiasts and bettors. 
        Creating machine learning models to predict horserace outcomes is crucial for enhancing betting strategies, improving the accuracy of odds, and providing valuable insights 
        to both industry professionals and casual participants, ultimately contributing to a more informed and engaging horse racing experience."""
        # st.title("Which Horse")
        st.markdown(f'<h1 style="font-size: 65px; text-align:center; text-shadow: 3px 3px 12px black;font:raleway;">{title}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align:center; text-shadow: 3px 3px 12px black;font:raleway;">{content}</p>', unsafe_allow_html=True)
        #  st.write('''Horse racing holds significant economic and entertainment value, attracting widespread attention from enthusiasts and bettors.

        #          \nCreating machine learning models to predict horserace outcomes is crucial for enhancing betting strategies, improving the accuracy of odds, and providing valuable insights to both industry professionals and casual participants, ultimately contributing to a more informed and engaging horse racing experience.
        #          ''')

# Sidebar navigation
st.sidebar.page_link('webapp.py', label='home')
st.sidebar.page_link('pages/about_us.py', label='about us')
st.sidebar.page_link('pages/which_horse.py', label='which horse')
st.sidebar.page_link('pages/our_model.py', label='our model')   
# elif selected_page == 'About Us':
#     st.switch_page('pages/about_us.py')

# elif selected_page == 'Which Horse':
#     st.switch_page('pages/which_horse.py')
    
# elif selected_page == 'Our Model':
#     st.switch_page('pages/our_model.py')
