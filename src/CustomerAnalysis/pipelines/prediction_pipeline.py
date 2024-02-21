import os
import sys
import pandas as pd
from src.CustomerAnalysis.exception import CustomException
from src.CustomerAnalysis.logger import logging
from src.CustomerAnalysis.utils.utils import load_object

import pickle


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)


            
            scaled_data=preprocessor.transform(features)
            
            prediction=model.predict(scaled_data)

            print(prediction)
            pred_1 = 0
            info = ""
            if prediction == 0:
                    pred_1 = 'cluster 0'
                    info = "1. less number of customers with low income \n 2. almost equal number of graduates and postgraduates \n 3. most of them are in relationship. few are singles \n 4. have 1 to 3 kids \n 5. their spending is lowest "
                   
                    

            elif prediction == 1:
                    pred_1 = 'cluster 1'
                    info = "1. maximum number of customers with highest income \n 2. Graduates and post graduates \n 3. almost equal number of singles and in relationship people \n 4. no kids, only few have 1 kid \n 5. their spending is also high "

                   
            elif prediction == 2:
                    pred_1 = 'cluster 2'
                    info = "1. Average number of customers with middle income \n 2. equal number of graduates and post graduates \n 3. most of them are in relationship,few are singles \n 4. have 1 or 2 kids \n 5. their spending is the less"

                    

    
            
            return (pred_1 , info)
            
            
        
        except Exception as e:
            raise CustomException(e,sys)
    
    
    

