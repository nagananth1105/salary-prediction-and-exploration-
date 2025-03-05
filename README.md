Salary Prediction

Project Overview

This project aims to predict salaries based on input features such as country, years of experience, and education level. The model is trained using a Decision Tree algorithm, and the frontend interface is built using Streamlit. The dataset used for training is sourced from the Stack Overflow Developer Survey 2024.

Features

Predicts salary based on Country, Years of Experience, and Education Level.

Uses a Decision Tree model for training and predictions.

Built with a Streamlit frontend for an interactive user experience.

Dataset sourced from Stack Overflow Developer Survey 2024.

Tech Stack

Backend: Python, Scikit-Learn (for Decision Tree model)

Frontend: Streamlit

Dataset: Stack Overflow Developer Survey 2024

Installation

Clone the repository:

git clone https://github.com/yourusername/salary-prediction.git
cd salary-prediction

Create and activate a virtual environment (optional but recommended):

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Dataset

The dataset is obtained from Stack Overflow Developer Survey 2024.

It contains salary information based on various factors, including country, years of experience, and education level.

The dataset is preprocessed before training the model.

Dataset Link: Stack Overflow Developer Survey 2024

Model Training

Load and preprocess the dataset.

Train a Decision Tree model using Scikit-Learn.

Evaluate the model's performance using appropriate metrics.

Save the trained model for deployment.

Running the Application

Train the model (if not already trained):

python train_model.py

Run the Streamlit app:

streamlit run app.py

Open the provided URL in a web browser to interact with the salary prediction tool.

Usage

Enter Country, Years of Experience, and Education Level in the Streamlit app.

Click on the Predict button to get the estimated salary.

Future Improvements

Enhance model performance using advanced techniques like Random Forest or XGBoost.

Expand dataset preprocessing for better feature engineering.

Deploy the model using Docker or cloud services.
