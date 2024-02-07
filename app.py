    
from src.CustomerAnalysis.pipelines.prediction_pipeline import PredictPipeline
import pandas as pd
import streamlit as st

#page configuration
st.set_page_config(page_title = 'Customer Segmentation Web App', layout='centered')
st.title('Customer Segmentation Web App')

Income = st.text_input("Type In The Household Income")
response = st.radio("select the response from the customer",('0','1'))
Age = st.slider ( "Select Age", 18, 85 )
relationship = st.radio ( "Livig With Partner? ", ('in_relationship', 'single') )
Education_Level = st.radio ( "Select Education:Undergraduate-0, Graduate-1, Postgraduate-2", ('Undergraduate','Graduate','Postgraduate') )
members_home = st.radio ( "select the total members at the house ", ( '1','2','3','4') )
acceptedcmp = st.radio ( "Select if customers accepted the product", ('0', '1') )
num_purschases = st.slider ( "select total purchases", 1, 148 )
expenses = st.slider ( "select total purchases", 0, 2500 )
    
input_data = [[Income,response, Age,relationship,Education_Level,members_home,acceptedcmp,num_purschases,expenses]]
features = pd.DataFrame(input_data, columns=['Income', 'Response', 'Age', 'relationship', 'Education_Level',
       'members_home', 'AcceptedCmp', 'num_purchases', 'expenses'])

    
result = ""

 # when 'Predict' is clicked, make the prediction and store it
if st.button("Segment Customer"):
        pipeline1 = PredictPipeline()

        result= pipeline1.predict(features)
    
        st.success(result)
