import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            preds = np.expm1(preds)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
    
    

class CustomData:
    def __init__( self,
        area:int,
        bedrooms:int,
        bathrooms:int,
        stories:int,
        mainroad:str,
        guestroom:str,
        basement:str,
        hotwaterheating:str,
        airconditioning:str,
        parking:str,
        prefarea:str,
        furnishingstatus:str):

        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.stories = stories
        
        self.mainroad = mainroad
        
        self.guestroom = guestroom

        self.basement = basement
        
        self.hotwaterheating = hotwaterheating
        
        self.airconditioning = airconditioning
        
        self.parking = parking
        
        self.prefarea = prefarea
        
        self.furnishingstatus = furnishingstatus

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "area":[self.area],

                "bedrooms":[self.bedrooms],

                "bathrooms":[self.bathrooms],

                "stories":[self.stories],
            
                "mainroad":[self.mainroad],
            
                "guestroom":[self.guestroom],

                "basement":[self.basement],
            
                "hotwaterheating":[self.hotwaterheating],
            
                "airconditioning":[self.airconditioning],
            
                "parking":[self.parking],
            
                "prefarea":[self.prefarea],
            
                "furnishingstatus":[self.furnishingstatus],

            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)


        
              
        