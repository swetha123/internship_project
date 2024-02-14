    
from src.CustomerAnalysis.pipelines.prediction_pipeline import PredictPipeline
import pandas as pd
import streamlit as st

def main():
       #page configuration
       st.set_page_config(page_title = 'Customer Segmentation Web App')
       st.title('Customer Segmentation Web App')

       Income = st.text_input("Type In The Household Income")
       Age = st.slider ( "Select Age", 18, 85 )
       relationship = st.radio ( "Livig With Partner? ", ('in_relationship', 'single') )
       Education_Level = st.radio ( "Select Education:", ('Undergraduate','Graduate','Postgraduate') )
       members_home = st.radio ( "select the total members at the house ", ( '1','2','3','4') )
       num_purschases = st.slider ( "select total number of purchases", 1, 148 )
       expenses = st.slider ( "select total amount of expenditure ", 0, 2500 )

       input_data = [[Income, Age,relationship,Education_Level,members_home,num_purschases,expenses]]
       features = pd.DataFrame(input_data, columns=['Income', 'Age', 'relationship', 'Education_Level',
       'members_home', 'num_purchases', 'expenses'])


       result = ""

       # when 'Predict' is clicked, make the prediction and store it
       if st.button("Segment Customer"):
              pipeline1 = PredictPipeline()

              result,info = pipeline1.predict(features)

              st.success(result)
              st.text_area(label = result,value = info,height = 150)


if __name__ == "__main__":
       main()