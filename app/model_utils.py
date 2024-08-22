import joblib

# Load the model
model = joblib.load('models/models.pkl')

def predict(input_data):
    # Implement preprocessing if needed
    # Make prediction
    return model.predict(input_data)
