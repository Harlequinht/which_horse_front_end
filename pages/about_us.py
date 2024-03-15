import streamlit as st

st.markdown("""
    <style>
    section[data-testid="stSidebar"][aria-expanded="true"]{
        height: 31% !important;
    }
    section[data-testid="stSidebar"][aria-expanded="false"]{
        height: 10% !important;
    }
    .st-emotion-cache-16txtl3 {
        padding: 2rem 1.5rem;
    }
    </style>""", unsafe_allow_html=True)

st.markdown('## Meet the Which Horse Team')
st.write('''
            Meet the dedicated team behind Which Horse, responsible for the end-to-end development and delivery of our predictive models.
            ''')

team_data = [
    {"name": "Harlequin", "image_url": "./team_photos/harlequin_photo.jpeg", "bio": "As a former Cruise Director, he aspire to deepen their understanding of Data Science, particularly \nfocusing on Machine Learning and the practical applications of big data across diverse industries."},
    {"name": "Rob", "image_url": "./team_photos/rob_photo.jpeg", "bio": "Aspiring Data Scientist with a background in Mechanical Engineering, Project Management and Consultancy."},
    {"name": "Amanda", "image_url": "./team_photos/amanda_photo.jpeg", "bio": "She is a Data Science and Analytics professional, holding a degree in Veterinary Medicine, and currently \npursuing post-graduation studies in the field of Data Science and Analysis."},
    {"name": "Tomi", "image_url": "./team_photos/tomi_photo.jpeg", "bio": "After working in finance, she decided to learn coding to automate tasks that used to take hours, integrating \nGoogle's Query Language into various processes upon mastering basic SQL syntax."},
    {"name": "David", "image_url": "./team_photos/david_photo.jpeg", "bio": "A Levels graduate embracing a transformative gap year, I'm now eager to reimmerse myself in the world of learning! "},
]

for team_member in team_data:
    st.subheader(team_member["name"])
    st.image(team_member["image_url"], width=150,  use_column_width=False)
    st.text(team_member["bio"])
    st.markdown('---')  # Add a horizontal line between team members
    
    # Define the pages
# pages = ['Home', 'About Us', 'Which Horse', 'Our Model']

# Sidebar navigation
# with st.sidebar:
#     if st.button("home", key=5):
#         st.switch_page('webapp.py')
    
#     if st.button('about us', key=6):
#         st.switch_page('pages/about_us.py')
        
#     if st.button('our model', key=7):
#         st.switch_page('pages/our_model.py')

#     if st.button('which horse', key=8):
#         st.switch_page('pages/which_horse.py')
        
# with st.sidebar:
#     st.page_link('webapp.py', label='home')
#     st.page_link('pages/about_us.py', label='about us')
#     st.page_link('pages/our_model.py', label='our model')  
#     st.page_link('pages/which_horse.py', label='which horse') 

# # Display content based on the selected page
# if selected_page == 'Home':
#     st.switch_page('webapp.py')
    
# elif selected_page == 'About Us':
#     st.switch_page('pages/about_us.py')

# elif selected_page == 'Which Horse':
#     st.switch_page('pages/which_horse.py')
    
# elif selected_page == 'Our Model':
#     st.switch_page('pages/our_model.py')