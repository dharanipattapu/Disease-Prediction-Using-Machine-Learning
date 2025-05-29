import joblib
import numpy as np

# Load model
model = joblib.load('../models/model.pkl')

# Sample user input (replace with real input)
user_input = [1, 0, 1, 1, 0, 0, 1]  # Dummy binary features

# Convert to numpy array and reshape
user_input_np = np.array(user_input).reshape(1, -1)

# Predict
prediction = model.predict(user_input_np)
print("Predicted Disease:", prediction[0])
