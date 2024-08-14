from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the model
model = joblib.load('model.pkl')

# Create Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict_ckd():
    # Convert form inputs to float
    wbc = float(request.form.get('wbc'))
    glucose = float(request.form.get('glucose'))
    urea = float(request.form.get('urea'))
    creatinine = float(request.form.get('creatinine'))
    pcv = float(request.form.get('pcv'))
    albumin = float(request.form.get('albumin'))
    hemoglobin = float(request.form.get('hemoglobin'))
    age = float(request.form.get('age'))
    sugar = float(request.form.get('sugar'))
    hypertension = int(request.form.get('hypertension')) if request.form.get('hypertension') else 0

    # Prepare input data for prediction
    input_data = np.array([[wbc, glucose, urea, creatinine, pcv, albumin, hemoglobin, age, sugar, hypertension]])
    
    # Make prediction
    result = model.predict(input_data)[0]
    
    # Return result
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
