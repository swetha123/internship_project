import pandas as pd
import numpy as np
import os
import sys
from src.CustomerAnalysis.logger import logging 
from src.CustomerAnalysis.exception import CustomException
from dataclasses import dataclass


from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier


from src.CustomerAnalysis.utils.utils import save_object


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self,cluster,array1):
        try:
            logging.info('splitting the data into train and test cases')
            
            data_array = np.c_[ array1, np.array(cluster)]
            X,y = (data_array[:,:-1],data_array[:,-1])

            x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.25)

            classifier =  GradientBoostingClassifier(n_estimators=100,learning_rate=0.1).fit(x_train,y_train)

            y_predict = classifier.predict(x_test)

            print(classifier.score(x_test,y_test))
            
            
            

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=classifier
            )

          

        except Exception as e:
            logging.info('Exception occured at model training time')
            raise CustomException(e,sys)


