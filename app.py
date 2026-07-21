from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__,template_folder='templates')

# XGBoost మోడల్‌ను లోడ్ చేయడం
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # ఫామ్ నుండి వివరాలను సేకరించడం
        features = [
            int(request.form['Gender']),
            int(request.form['Married']),
            int(request.form['Dependents']),
            int(request.form['Education']),
            int(request.form['Self_Employed']),
            float(request.form['ApplicantIncome']),
            float(request.form['CoapplicantIncome']),
            float(request.form['LoanAmount']),
            float(request.form['Loan_Amount_Term']),
            float(request.form['Credit_History']),
            int(request.form['Property_Area'])
        ]
        
        final_features = [np.array(features)]
        
        # ప్రిడిక్షన్ చేయడం
        prediction = model.predict(final_features)
        
        if prediction[0] == 1:
            result_text = "🎉 Congratulations! Your Loan Application is Approved."
        else:
            result_text = "⚠️ Risk Alert! Your Application is High-Risk. Manual verification required."
            
        return render_template('index.html', prediction_text=result_text)

if __name__ == "__main__":
    app.run(debug=True)