# 🏡 Bangalore House Price Prediction (ML + Deep Learning)
<img src="https://github.com/goldstring/banglore_house_price_prediction_regression_using_ann_end_to_end_deeep-machine_learning/blob/main/output/output.png?raw=true"/>
## 📌 Problem Statement

The goal is to **predict housing prices** in Bangalore based on various features such as location, number of bedrooms, total square feet, and more. Accurate price prediction is crucial for buyers, sellers, and real estate platforms to make informed decisions.

---

## ✅ Proposed Solution

This project builds and compares:
- Traditional **Machine Learning models** (Linear Regression, Lasso, Decision Tree, Random Forest, etc.)
- A **Deep Learning Artificial Neural Network (ANN)** model

The ANN model achieved an impressive **R² score of 0.9465**, showing superior performance.

---

## 🛠️ Technologies & Tools Used

| Category          | Stack                                  |
|------------------|-----------------------------------------|
| Programming      | Python                                  |
| ML Models        | Scikit-learn                            |
| Deep Learning    | TensorFlow, Keras                       |
| Web Framework    | Flask                                   |
| Data Handling    | Pandas, NumPy                           |
| Visualization    | Matplotlib, Seaborn                     |
| Deployment       | HTML/CSS (basic for UI), Flask API      |
| Environment Mgmt | `venv`, `requirements.txt`, Git         |

---

## 🔄 Data Science Lifecycle Applied

1. **Problem Understanding**  
   Define scope: Predict price based on location, area, BHK, etc.

2. **Data Collection**  
   Dataset sourced from housing data in Bangalore.

3. **Data Preprocessing**  
   - Handle missing values  
   - Outlier removal  
   - Feature engineering (location encoding, total sqft cleanup)

4. **Model Building**  
   - Train/test split  
   - Applied Linear Regression, Decision Tree, Random Forest  
   - Built ANN using Keras

5. **Evaluation**  
   - R² score, RMSE for each model  
   - ANN achieved highest R² of **0.9465**

6. **Deployment**  
   - Model saved using `joblib` / `pickle`  
   - Flask used to create web app for live prediction

---

## 📊 Output / Results

- The ANN model outperformed others with an R² score of **0.9465**.
- A simple web UI allows users to enter location, sqft, BHK, bath — and get a predicted price.
- Visualizations show distribution, correlation heatmaps, model comparisons.

---

## 🧱 Project Structure

```
bangalore_house_price_prediction/
├── static/
├── templates/
│   └── index.html
├── model/
│   └── ann_model.h5
├── app.py
├── utils.py
├── data/
│   └── bangalore.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 How to Run This Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/goldstring/banglore_house_price_prediction_regression_using_ann_end_to_end_deeep-machine_learning.git
cd banglore_house_price_prediction_regression_using_ann_end_to_end_deeep-machine_learning
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Run the Flask App

```bash
python app.py
```

The app will start at `http://127.0.0.1:5000/`

---

## 🌐 Web App Output

- Input: Location, Square Feet, BHK, Bath  
- Output: **Predicted Price** in lakhs  
- UI: Simple HTML form with dropdowns and inputs

---

## 🧠 Conclusion

- ANN model provides highly accurate predictions of house prices.
- This end-to-end project demonstrates the complete **data science pipeline**: from raw data to deployment.
- Can be extended to include:
  - Map-based visualization
  - More features like amenities, distance to landmarks
  - Integration with front-end frameworks

