import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from sklearn.metrics import r2_score
import dill
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path,exist_ok=True)
    with open(file_path,'wb') as file_obj:
        dill.dump(obj,file_obj)

def evaluate_models(x_train, y_train,x_test,y_test,models,params):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(x_train,y_train)
            model.set_params(**gs.best_params_)

            model.fit(x_train, y_train)  # Train model
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
            
        return report

    except Exception as e:
        raise CustomException(e, sys)