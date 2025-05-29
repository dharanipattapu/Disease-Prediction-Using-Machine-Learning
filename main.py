# app/main.py

import sys
import numpy as np
from joblib import load

# Load the trained model and symptom encoder
model = load("../models/model.pkl")
encoder = load("../models/symptom_encoder.pkl")

# Get list of all known symptoms
all_symptoms = encoder.classes_

def predict_disease(user_symptoms):
    # Convert input symptoms to binary format
    input_vector = encoder.transform([user_symptoms])
    
    # Predict disease
    prediction = model.predict(input_vector)
    
    return prediction[0]

if __name__ == "__main__":
    print("🔍 Disease Prediction from Symptoms")
    print("📝 Enter symptoms separated by commas (e.g. fever, cough, headache):")
    symptoms_input = input(">> ")

    # Process input
    user_symptoms = [sym.strip().lower().replace(" ", "_") for sym in symptoms_input.split(",")]

    # Validate symptoms
    invalid = [sym for sym in user_symptoms if sym not in all_symptoms]
    if invalid:
        print(f"❌ Invalid symptoms: {', '.join(invalid)}")
        print("✅ Valid symptoms are:")
        print(", ".join(all_symptoms))
        sys.exit(1)

    # Predict
    disease = predict_disease(user_symptoms)
    print(f"\n✅ Predicted Disease: **{disease}**")
