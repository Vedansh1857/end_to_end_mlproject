# Same as app.py file. This is created just for deployment purpose

from flask import Flask,request,render_template
import numpy as np
import pandas as pd
# A small code change just to check the working of runner.

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application = Flask(__name__)
app = application

# Creating a route for our homepage...
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        preds_df = data.get_data_as_data_frame()
        print(preds_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(preds_df)
        return render_template('home.html',results=results[0])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

# Note :- while deploying the application we must make sure that we remove "debug=True" in the "app.run"
    
