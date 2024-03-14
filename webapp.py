import streamlit as st
import pandas as pd
import numpy as np
import toml
from pipeline_cleaning import clean_data
from custom_loss import custom_loss_function
from tensorflow.keras.models import load_model
import pickle
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


def main():
    # Set the page configuration
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
    )

if __name__ == "__main__":
    main()

# Your data loading and cleaning functions go here
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''
# Loading pipeline
pipe = pickle.load(open('softmax_pipeline.pkl', 'rb'))

# Loading model
model = load_model('softmax.h5')

st.markdown(page_bg_img, unsafe_allow_html=True)
# Define the pages
pages = ['Home', 'About Us', 'Which Horse', 'Our Model']

# Sidebar navigation
selected_page = st.sidebar.selectbox('Navigation', pages)

# Display content based on the selected page
if selected_page == 'Home':
    st.markdown('## Which Horse')
    st.write('''Horse racing holds significant economic and entertainment value, attracting widespread attention from enthusiasts and bettors.

             \nCreating machine learning models to predict horserace outcomes is crucial for enhancing betting strategies, improving the accuracy of odds, and providing valuable insights to both industry professionals and casual participants, ultimately contributing to a more informed and engaging horse racing experience.
             ''')

elif selected_page == 'About Us':
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

elif selected_page == 'Which Horse':
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

elif selected_page == 'Our Model':
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
