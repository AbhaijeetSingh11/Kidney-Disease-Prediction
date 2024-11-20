from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np

# Load the trained model
model = joblib.load('kidney_disease_RFC.pkl')

# Initialize Flask app
app = Flask(__name__, template_folder='templates')
CORS(app)

# Serve the HTML file
@app.route('/')
def index():
    return render_template('new.html')

# API route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the request
        data = request.get_json()

        # Convert input data to numpy array
        features = np.array([
            float(data['age']), float(data['blood_pressure']), float(data['specific_gravity']),
            float(data['albumin']), float(data['sugar']), float(data['red_blood_cells']),
            float(data['pus_cell']), float(data['pus_cell_clumps']), float(data['bacteria']),
            float(data['blood_glucose_random']), float(data['blood_urea']), float(data['serum_creatinine']),
            float(data['sodium']), float(data['potassium']), float(data['haemoglobin']),
            float(data['packed_cell_volume']), float(data['white_blood_cell_count']),
            float(data['red_blood_cell_count']), float(data['hypertension']),
            float(data['diabetes_mellitus']), float(data['coronary_artery_disease']),
            float(data['appetite']), float(data['peda_edema']), float(data['aanemia'])
        ]).reshape(1, -1)

        # Predict using the model
        prediction = model.predict(features)
    
        # Return the prediction as JSON
        # return jsonify({'prediction': int(prediction[0])})
        if prediction[0] == 1:
            result = "Positive Report" 
        else: 
            result = "Negative Report" # Return the prediction as JSON 
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
