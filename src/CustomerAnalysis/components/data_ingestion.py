import pandas as pd
import numpy as np
import os
import sys
from src.CustomerAnalysis.logger import logging 
from src.CustomerAnalysis.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","cleaned.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data","marketing_campaign.csv")),sep="\t")
            logging.info("read the data as dataframe")

            data['Age'] = 2024 - data['Year_Birth']
            #delete the outliers..
            #from age column
            data = data[data['Age'] < 80]
            #from income column
            data=data[data['Income']<150000]

            #handling Marital_Status column
            data['relationship']=data['Marital_Status'].replace(
                                    {'Married':'in_relationship' , 
                                    'Together':'in_relationship' , 
                                    'Single':'single' , 
                                    'Divorced':'single',
                                    'YOLO':'single' , 
                                    'Absurd':'single' , 
                                    'Widow':'single' ,
                                    'Alone':'single'})

            #Segmenting education levels in three groups
            data["Education_Level"]=data["Education"].replace(
                                    {"Basic":"Undergraduate",
                                    "2n Cycle":"Undergraduate", 
                                    "Graduation":"Graduate",
                                    "Master":"Postgraduate", 
                                    "PhD":"Postgraduate"})

            # counting the total number of people in the household
            data['members_home']=data['Kidhome']+data['Teenhome']+data['relationship'].replace({'single':0,'in_relationship':1})

            # creating single column for accepted column
            data['AcceptedCmp'] = data['AcceptedCmp1'] + data['AcceptedCmp2'] + data['AcceptedCmp3']
            + data['AcceptedCmp4'] + data['AcceptedCmp5'] + data['Response']

            # summing up the total number of purchases 
            data['num_purchases'] = data['NumWebPurchases'] + data['NumCatalogPurchases'] + data['NumStorePurchases'] + data['NumDealsPurchases']

            # calculating the total expenses
            data['expenses'] = data['MntWines'] + data['MntFruits'] + data['MntMeatProducts'] 
            + data['MntFishProducts'] + data['MntSweetProducts'] + data['MntGoldProds']

            #dropping unnecessary columns
            data.drop(labels=['Marital_Status','ID','Year_Birth'
                            ,'Dt_Customer', 'Kidhome','Teenhome',
                            'MntWines', 'MntFruits','MntMeatProducts', 'MntFishProducts',
                            'MntSweetProducts','MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases',
                            'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
                            'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1',
                            'AcceptedCmp2','Z_CostContact', 'Z_Revenue',"Recency", "Complain",'Education'], axis=1, inplace=True)

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("saving the raw data in artifacts folder")

            logging.info("data ingestion part is completed")

            return(
                self.ingestion_config.raw_data_path,   
            )

        except Exception as e:
            logging.info("exception occured at the data ingestion phase ")
            raise CustomException(e,sys)    

    