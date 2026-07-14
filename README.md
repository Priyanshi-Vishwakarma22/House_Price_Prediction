# 🏠 House Price Prediction using Machine Learning

A Machine Learning web application that predicts house prices based on property features such as area, bedrooms, bathrooms, stories, parking, furnishing status, and other amenities.

The application is built using **Python, Flask, Scikit-learn**, and follows an **end-to-end Machine Learning pipeline** including data preprocessing, model training, prediction, and deployment.

---

## 📌 Features

- Predict house prices instantly
- Interactive and user-friendly web interface
- End-to-End Machine Learning Pipeline
- Data Preprocessing using Scikit-learn Pipeline
- Model Serialization using Pickle
- Flask Web Application
- Responsive UI
- Input Validation
- Production-ready project structure

---

## 📂 Project Structure

```
House_Price_Prediction/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   └── House_Price_Prediction.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── setup.py
```

---

## 📊 Dataset

The dataset contains housing information with the following features:

- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

Target Variable:

- House Price

---

## ⚙️ Machine Learning Workflow

1. Data Ingestion
2. Data Cleaning
3. Feature Engineering
4. Data Transformation
5. Model Training
6. Model Evaluation
7. Model Saving
8. Flask Deployment

---

## 🤖 Models Used

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor

The best-performing model was selected based on evaluation metrics.

---

## 📈 Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 💻 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- CatBoost
- Flask
- Pickle

### Frontend

- HTML5
- CSS3
- JavaScript

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
```

Move to project folder

```bash
cd House-Price-Prediction
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🖥️ Application

The web application allows users to:

- Enter house details
- Predict estimated house price
- View prediction instantly

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
Home Page

Prediction Result
```

---

## 🔮 Future Improvements

- Deploy on Render
- Deploy on Railway
- Add Price Distribution Graph
- Add Prediction History
- User Authentication
- Database Integration
- Dark Mode
- REST API Support

---

## 👩‍💻 Author

**Priyanshi Vishwakarma**

B.Tech Computer Science Engineering (AI & ML)

Python | Machine Learning | Data Analytics | Flask | SQL

---

## ⭐ If you found this project useful, please give it a star.