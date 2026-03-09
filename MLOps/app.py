from flask import Flask, request, render_template
import numpy as np
import joblib
import pandas as pd

# Load the models from the files
loaded_rf_model = joblib.load('./rf_model.joblib')
cat_encode_model = joblib.load('./cat_encoder.joblib')

# function for prediction
def predict_price(input_data, rf_model, ohe):
    df = pd.DataFrame([input_data])
    encoded_var = ohe.transform(df[['from', 'to', 'flightType', 'agency']])
    encoded_df = pd.DataFrame(encoded_var.toarray(), columns=ohe.get_feature_names_out(), dtype=int)
    df = pd.concat([df, encoded_df], axis=1)
    df.drop(columns=['from', 'to', 'flightType', 'agency'], inplace=True)
    y_pred = rf_model.predict(df)
    return y_pred[0]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')


@app.route('/predict', methods=['POST'])
def index():
    if request.method == 'POST':
        # Get input data from the form
        from_ = request.form.get('from')
        to = request.form.get('to')
        flightType = request.form.get('flightType')
        time = request.form.get('time')
        distance = request.form.get('distance')
        agency = request.form.get('agency')

        # input dictionary
        data = {
            'from': from_,
            'to': to,
            'flightType': flightType,
            'time': time,
            'distance': distance,
            'agency': agency
        }

        # Predict the price
        prediction = round(predict_price(data, loaded_rf_model, cat_encode_model), 2)

        # Render the HTML template with dynamic data
        return render_template('index.html', input_data=data, prediction=prediction)

# Author: Narasimman
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
