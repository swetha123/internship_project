import pandas as pd
import numpy as np
import os
import sys
from src.CustomerAnalysis.logger import logging 
from src.CustomerAnalysis.exception import CustomException
from dataclasses import dataclass

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


from src.CustomerAnalysis.utils.utils import save_object

from src.CustomerAnalysis.components.data_transformation import DataTransformation

@dataclass
class ClusterFormerConfig:
    cluster_file_path = os.path.join("artifacts","cluster.pkl")

class ClusterFormer:
    def __init__(self):
        self.cluster_config = ClusterFormerConfig()
    
    def initiate_clustering(self,preprocessed_array):
        try:
            logging.info('using kmeans clustering on the data')

            # using k-means to form clusters
            kmeans = KMeans(n_clusters=3, random_state=42)
            target = kmeans.fit_predict(preprocessed_array) 

            kmeans_score = silhouette_score(preprocessed_array, target)
            print(kmeans_score)
            
            

            save_object(
                 file_path=self.cluster_config.cluster_file_path,
                 obj=kmeans
            )

            return target,preprocessed_array
          

        except Exception as e:
            logging.info('Exception occured at cluster forming')
            raise CustomException(e,sys)

