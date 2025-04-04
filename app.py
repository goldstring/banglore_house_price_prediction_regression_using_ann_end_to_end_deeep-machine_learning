from flask import Flask, request, jsonify, render_template
import random  # Simulating a price predictiom
import json
import numpy as np
# Read the JSON file
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/')
def home():
    with open("property_data.json", "r") as file:
        json_data = json.load(file)
    return render_template('index.html', data=json_data)

@app.route('/predict', methods=['POST'])
def predict():
    from flask import request, jsonify
    import numpy as np
    import json
    from tensorflow.keras.models import load_model

    # Get form data from AJAX request
    data = request.json

    with open("property_data.json", "r") as file:
        categories = json.load(file)

    area_type_ = np.zeros(len(categories["area_type_"]))
    location_ = np.zeros(len(categories["location_"]))
    availability_ = np.zeros(len(categories["availability_"]))

    area = data.get('area')
    location = data.get('location')
    availability = data.get('availability')

    bhk = float(data.get('bhk'))
    bath = float(data.get('bath'))
    balcony = float(data.get('balcony'))

    per_sqft = np.log1p(float(data.get('per_sqft')))
    price_per_sqft = np.log1p(float(data.get('price_per_sqft')))

    # One-hot encoding
    if area in categories["area_type_"]:
        area_type_[categories["area_type_"].index(area)] = 1
    if location in categories["location_"]:
        location_[categories["location_"].index(location)] = 1
    if availability in categories["availability_"]:
        availability_[categories["availability_"].index(availability)] = 1

    basics = [bhk, bath, balcony, per_sqft, price_per_sqft]

    # Combine features
    features = np.concatenate([
        basics,
        area_type_,
        availability_,
        location_
    ]).astype('float')

    input_data = features.reshape(1, -1)

    # Load model (without compile to save time)
    model = load_model('regression_model.h5', compile=False)

    # Predict
    prediction = model.predict(input_data)

    return jsonify({
        'predicted_price': float(prediction[0][0])
    })

if __name__ == '__main__':
    app.run(debug=True)
