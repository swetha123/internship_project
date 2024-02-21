import pandas as pd
import numpy as np
import os
import sys

from dataclasses import dataclass

from sklearn import preprocessing
from src.CustomerAnalysis.logger import logging 
from src.CustomerAnalysis.exception import CustomException

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler,OneHotEncoder

from src.CustomerAnalysis.utils.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")



class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logging.info("data transformation initiated")

            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['relationship', 'Education_Level']
            numerical_cols = ['Income', 'Age', 'children',
             'num_purchases', 'expenses']
        
            one_cols = ['relationship']
            ord_cols = ['Education_Level']

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )
            
            ordinal_pipeline=Pipeline(
                    steps=[
                        ('ordinalencoder',OrdinalEncoder(categories=[['Undergraduate','Graduate','Postgraduate']]))
                    ] 
                )

            onehot_pipeline=Pipeline(
                    steps=[
                        ('onehotencoder',OneHotEncoder(categories=[['in_relationship', 'single']]))
                    ] 
                )

            preprocessor=ColumnTransformer(
                [
                    
                    ('num_pipeline',num_pipeline,numerical_cols),
                    ('ordinal_pipeline',ordinal_pipeline,ord_cols),
                    ('nominal_pipeline',onehot_pipeline,one_cols)
                ]
            )
            
            return preprocessor

            
        except Exception as e:
            logging.info("exception occured at the data transformation phase")
            raise CustomException(e,sys)

    def initiate_data_transformation(self,data_path):
        try:
            data = pd.read_csv(data_path)

            logging.info("reading the data completed")
            logging.info(f" dataframe head: \n{data.head().to_string()}")

            preprocessing_obj = self.get_data_transformation()

            preprocessed_arr=preprocessing_obj.fit_transform(data)
            
            logging.info("Applying preprocessing object on the dataset.")
            
    
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            logging.info("preprocessing pickle file saved")

            return (
               preprocessed_arr
            )


        except Exception as e:
            logging.info("exception occured at the data transformation phase")
            raise CustomException(e,sys)



