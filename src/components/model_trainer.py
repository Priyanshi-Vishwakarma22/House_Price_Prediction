import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path =os.path.join("artifacts",'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Linear": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "GradientBoost": GradientBoostingRegressor(random_state=42),
                "CatBoost": CatBoostRegressor(verbose=False, random_state=42),
                "XGB": XGBRegressor(random_state=42),
            }

            params = {
                "Linear": {},

                "Ridge": {
                    "alpha": [0.1,1,10]
                },

                "Lasso": {
                    "alpha": [0.001,0.01,0.1]
                },

                "GradientBoost": {
                    "n_estimators": [100, 200, 300],
                    "max_depth": [2, 3, 4],
                    "learning_rate": [0.01, 0.03, 0.05, 0.1],
                    "subsample": [0.6, 0.8, 1.0],
                    "min_samples_leaf": [1, 3, 5, 10]
                },

                "CatBoost": {
                    "iterations": [200, 300, 500],
                    "depth": [3, 4, 5, 6],
                    "learning_rate": [0.01, 0.03, 0.05, 0.1],
                    "l2_leaf_reg": [1, 3, 5, 7, 9]
                },

                "XGB": {
                    "n_estimators": [100, 200, 300, 500],
                    "max_depth": [2, 3, 4, 5, 6],
                    "learning_rate": [0.01, 0.03, 0.05, 0.1],
                    "subsample": [0.6, 0.8, 1.0],
                    "colsample_bytree": [0.6, 0.8, 1.0],
                    "min_child_weight": [1, 3, 5, 7],
                    "reg_alpha": [0, 0.1, 1],
                    "reg_lambda": [1, 1.5, 2]
                }

            }
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)
            
            ## to get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## to get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)
            
            r2_square = r2_score(y_test,predicted)
            return r2_square




        except Exception as e:
            raise CustomException(e,sys) 



