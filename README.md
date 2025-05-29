# Disease-Prediction-Using-Machine-Learning
A machine learning project that predicts diseases based on symptoms using a Decision Tree Classifier. Trained on a real-world medical dataset with complete CLI interface, model training notebook, and modular code structure. Built as part of Task 3 for the CodeAlpha Internship Program.

# 🧠 Disease Prediction Using Machine Learning

This project predicts diseases based on user-provided symptoms using a trained machine learning model. Built from scratch using Python, Pandas, and Scikit-learn.

---

## 📁 Project Structure

disease_prediction_ml/
├── app/
│ ├── main.py
│ └── predict.py
├── data/
│ └── disease_dataset.csv
├── models/
│ ├── model.pkl
│ └── symptom_encoder.pkl
├── notebooks/
│ └── EDA_and_Model_Training.ipynb
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🚀 Features

- Symptom-based disease prediction
- Decision Tree Classifier model
- Symptom encoding using `MultiLabelBinarizer`
- Modular code structure
- Command-line interface via `main.py`

---

## 📦 Installation

1. Clone the repo or download the ZIP
2. Open terminal in project directory
3. Create and activate virtual environment:

    python -m venv venv
    venv\Scripts\activate  # Windows
    ```

4. Install requirements:

    pip install -r requirements.txt
    ```

---

## 🧪 Training the Model

Run the notebook to train and save the model:

jupyter notebook notebooks/EDA_and_Model_Training.ipynb
💻 Running Prediction
Use the CLI tool to predict from symptoms:


python app/main.py
Example input:

fever, cough, fatigue
🎓 Internship Info
This project was completed as Task 3 under the CodeAlpha Internship Program.

🛠️ Tech Stack
Python

Scikit-learn

Pandas

Jupyter Notebook

Joblib

📌 Author
👤 Name: [Your Name]

🌐 LinkedIn: [Your LinkedIn URL]

✉️ Email: [Your Email]

⭐ Acknowledgements
CodeAlpha for the internship and guidance

Kaggle for the dataset

🏷️ Tags
#MachineLearning #DiseasePrediction #PythonProject #CodeAlphaInternship #MLfromScratch

yaml

---

Let me know if you also want a **web interface (Streamlit)** or **desktop GUI** ve
