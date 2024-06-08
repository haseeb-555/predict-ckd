from flask import Flask,render_template
import pickle
import numpy as np
from flask import Flask, request

# Assuming the predict_ckd function is defined in a Flask route or view function

model=pickle.load(open('model.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_ckd():
  
    # Convert form inputs to float
    wbc = float(request.form.get('wbc'))
    glucose = float(request.form.get('glucose'))
    urea = float(request.form.get('urea'))
    creatinine = float(request.form.get('creatinine'))
    pcv = float(request.form.get('pcv'))
    albumin = float(request.form.get('albumin'))
    hemoglobin = float(request.form.get('hemoglobin'))
    age = float(request.form.get('age'))  # Convert to integer
    sugar = float(request.form.get('sugar'))
    hypertension = int(request.form.get('hypertension')) if request.form.get('hypertension') else 0  # Assign default value or handle the case when 'hypertension' is not submitted
    
    # Print input values
    print("White Blood Cell Count (cells/µL):", wbc)
    print("Blood Glucose Random (mg/dL):", glucose)
    print("Blood Urea (mg/dL):", urea)
    print("Serum Creatinine (mg/dL):", creatinine)
    print("Packed Cell Volume (%):", pcv)
    print("Albumin (gm/dL):", albumin)
    print("Hemoglobin (gm/dL):", hemoglobin)
    print("Age:", age)
    print("Sugar (1 if present, 0 if absent):", sugar)
    print("Hypertension (1 if present, 0 if absent):", hypertension)
    
    # Predict using the model
    input_data = np.array([[wbc, glucose, urea, creatinine, pcv, albumin, hemoglobin, age, sugar, hypertension]])
    print(input_data)
    result = model.predict(input_data)
    
    print(result)
    
    return str(result)

  

if __name__=='__main__':
  app.run(debug=True)
  
  