import logging
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Configure logging
logging.basicConfig(filename='api_logs.log', level=logging.INFO)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
        prediction = model.predict([features])[0]

        # Log prediction information
        logging.info(f"Prediction - Input: {data}, Prediction: {prediction}")

        return jsonify({'prediction': prediction})
    except Exception as e:
        # Log error information
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)

