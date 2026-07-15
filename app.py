from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("model/fraud_model.pkl")


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Single Transaction Prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        features = np.array(features).reshape(1, -1)

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "⚠️ Fraudulent Transaction Detected!"
        else:
            result = "✅ Genuine Transaction"

        return render_template(
            'index.html',
            prediction_text=result
        )

    except Exception as e:
        return str(e)


# CSV Upload Prediction
@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']

        if file.filename == '':
            return render_template(
                'index.html',
                prediction_text="No file selected."
            )

        # Read CSV
        data = pd.read_csv(file)

        # Remove target column if present
        if 'Class' in data.columns:
            features = data.drop('Class', axis=1)
        else:
            features = data

        # Predict
        prediction = model.predict(features)

        fraud = int(sum(prediction))
        genuine = len(prediction) - fraud
        total = len(prediction)

        # Fraud Percentage
        fraud_percent = (fraud / total) * 100

        if fraud_percent < 1:
            risk = "🟢 Low Risk"
        elif fraud_percent < 5:
            risk = "🟡 Medium Risk"
        else:
            risk = "🔴 High Risk"

        result = f"""
Total Transactions : {total}

Fraud Transactions : {fraud}

Genuine Transactions : {genuine}
"""

        return render_template(
            'index.html',
            prediction_text=result,
            fraud=fraud,
            genuine=genuine,
            total=total,
            risk=risk
        )

    except Exception as e:
        return str(e)


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)