from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        time = float(request.form['time'])
        amount = float(request.form['amount'])
        pc1 = float(request.form['pc1'])
        pc2 = float(request.form['pc2'])
        pc3 = float(request.form['pc3'])

        # Construct input for model
        input_data = [time, pc1, pc2, pc3, amount]
        input_array = np.array(input_data).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)[0]
        result = "⚠️ Fraudulent Transaction Detected" if prediction == 1 else "✅ Transaction is Legitimate"

        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
