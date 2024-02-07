from src.CustomerAnalysis.components.data_ingestion import DataIngestion

from src.CustomerAnalysis.components.data_transformation import DataTransformation

from src.CustomerAnalysis.components.model_trainer import ModelTrainer
from src.CustomerAnalysis.components.cluster import ClusterFormer 

import pandas as pd
import numpy as np
import os
import sys
from src.CustomerAnalysis.logger import logging 
from src.CustomerAnalysis.exception import CustomException

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion=DataIngestion()
            cleaned_data_path=data_ingestion.initiate_data_ingestion()
            return cleaned_data_path
        except Exception as e:
            raise CustomException(e,sys)
        
    def start_data_transformation(self,data_path):
        
        try:
            data_transformation = DataTransformation()
            print(data_path,data_path[0])
            pre_arr=data_transformation.initiate_data_transformation(data_path[0])
            return pre_arr
        except Exception as e:
            raise CustomException(e,sys)

    def start_cluster_formation(self,pre_arr):
        cluster_formation = ClusterFormer()
        target,arr = cluster_formation.initiate_clustering(pre_arr)
        return target,arr

    
    def start_model_training(self,target,arr):
        try:
            model_trainer=ModelTrainer()
            model_trainer.initiate_model_training(target,arr)
        except Exception as e:
            raise CustomException(e,sys)
                
    def start_trainig(self):
        try:
            cleaned_data_path=self.start_data_ingestion()
            print(cleaned_data_path)
            pre_arr=self.start_data_transformation(cleaned_data_path)
            target,arr = self.start_cluster_formation(pre_arr)
            self.start_model_training(target,arr)
        except Exception as e:
            raise CustomException(e,sys)



obj1 = TrainingPipeline()
obj1.start_trainig()




