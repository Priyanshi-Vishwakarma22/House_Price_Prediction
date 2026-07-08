import os
import sys

import pandas as pd
import numpy as np

from src.exception import CustomException

import dill
import pickle
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report = {}
        
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

              # Hyperparameter Tuning
            if len(para) > 0:

                rs = RandomizedSearchCV(
                    estimator=model,
                    param_distributions=para,
                    n_iter=20,
                    scoring="r2",
                    cv=5,
                    random_state=42,
                    n_jobs=-1
                )

                rs.fit(X_train, y_train)

                model = rs.best_estimator_

                print(f"{list(models.keys())[i]} Best Params: {rs.best_params_}")

            # Train Best Model
            model.fit(X_train, y_train)

            # Prediction
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            print(f"{list(models.keys())[i]}")
            print(f"Train R2 Score : {train_score:.4f}")
            print(f"Test R2 Score  : {test_score:.4f}")
            print("-" * 50)

            report[list(models.keys())[i]] = test_score

            # Save tuned model back
            models[list(models.keys())[i]] = model

        return report
    
    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)