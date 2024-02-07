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
            if prediction == 0:
                    pred_1 = 'cluster 0'

            elif prediction == 1:
                    pred_1 = 'cluster 1'

            elif prediction == 2:
                    pred_1 = 'cluster 2'


    
            
            return pred_1
            
            
        
        except Exception as e:
            raise CustomException(e,sys)
    
    
    

