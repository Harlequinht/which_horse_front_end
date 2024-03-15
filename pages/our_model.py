import streamlit as st
import pandas as pd
from pipeline_cleaning import clean_data
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from webapp import load_pipe_model  
from keras.utils import get_custom_objects


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

uploaded_file = st.file_uploader("Choose a csv file", type='csv')
# st.write(pipeline.get_feature_names_out())
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if df.empty:
            st.error("Error: Submitted file is empty")
        else:
            st.success("Performing relevant checks and displaying metrics...")
            if st.button('Predict'):
                df_clean = clean_data(df)
                X_pred = df_clean.drop(columns=['bsp','event_number','meeting_id', 'win_or_lose', 'horse_id', 'place', '15_mins', '10_mins', '5_mins', '3_mins', '2_mins', '1_min_'])
                print('Data cleaned')
                pipe, model = load_pipe_model()
                X_pred_transform = pd.DataFrame(pipe.transform(X_pred), columns= pd.Series(pipe.get_feature_names_out()).str.split('__', expand=True)[1])
                print('Data transformed')
                predct = model.predict(X_pred_transform)
                results_df = pd.DataFrame({'y_pred': predct.round(2)[:,0], 'y_true': df_clean['win_or_lose'].replace(0.5, 1.0)})
                results_df['y_pred_050'] = results_df.y_pred.map(lambda x: 1.0 if x>=0.5 else 0.0)
                st.write(results_df)

                scores = {
                    'accuracy': [accuracy_score(results_df.y_true, results_df.y_pred_050)],
                    'precision': [precision_score(results_df.y_true, results_df.y_pred_050)],
                    'recall': [recall_score(results_df.y_true, results_df.y_pred_050)],
                    'f1': [f1_score(results_df.y_true, results_df.y_pred_050)]
                }
                scores_df = pd.DataFrame(scores)
                scores_df
                X_pred_transform

    except Exception as e:
        st.error(f"Error: {e}")
        
# Sidebar navigation
with st.sidebar:
    if st.button("home"):
        st.switch_page('webapp.py')
    
    if st.button('about us'):
        st.switch_page('pages/about_us.py')
        
    if st.button('our model'):
        st.switch_page('pages/our_model.py')

    if st.button('which horse'):
        st.switch_page('pages/which_horse.py')
# with st.sidebar:
#     st.page_link('webapp.py', label='home')
#     st.page_link('pages/about_us.py', label='about us')
#     st.page_link('pages/our_model.py', label='our model')  
#     st.page_link('pages/which_horse.py', label='which horse')

        
#             # Define the pages
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
#     st.switch_page('pages/our_model.py')