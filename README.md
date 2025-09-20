Taxi Fare Prediction App
Predict taxi fares using machine learning with a simple Streamlit web app.

Features
Input trip details: distance, duration, time, vendor, payment type
Predict fare instantly
Handles numeric and categorical features

Tech Stack
Python | pandas | numpy | scikit-learn | XGBoost | Streamlit | joblib | pyngrok

Setup
git clone https://github.com/VishvaSE/taxi-fare-app.git
cd taxi-fare-app
pip install -r requirements.txt
streamlit run app.py

**Note** : This a temprory link which has limit as 3 times

Access locally:
!pip install --quiet streamlit pyngrok joblib pandas numpy scikit-learn
# Set ngrok authtoken
!ngrok authtoken your_authtoken
from pyngrok import ngrok
ngrok.kill()  # Close previous tunnels
# Run Streamlit in background
get_ipython().system_raw("streamlit run app.py --server.port 8501 &")
# Create public URL
public_url = ngrok.connect(8501)
print("🚀 Open your app here:", public_url) 

Project Structure
app.py
best_taxi_pipeline.joblib
taxi_fare (1).csv
README.md
