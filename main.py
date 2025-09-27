from flask import Flask, render_template, request 
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("Build_new_model_Medical_insurance.pkl", "rb"))

@app.route("/")
def home():
    # This will look for templates/index.html
    return render_template("index.html")

@app.route("/predict_charges", methods=["POST"])
def predict():
    try:
        # Get form values from index.html
        age = int(request.form.get("age"))
        gender = 1 if request.form.get("gender") == "Male" else 0
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = 1 if request.form.get("smoker") == "Yes" else 0
        region = request.form.get("region")

        # Region one-hot encoding
        region_dict = {
            "northeast": [1, 0, 0, 0],
            "northwest": [0, 1, 0, 0],
            "southeast": [0, 0, 1, 0],
            "southwest": [0, 0, 0, 1],
        }
        region_encoded = region_dict.get(region.lower(), [0, 0, 0, 0])

        # Prepare input array
        test_array = [age, gender, bmi, children, smoker] + region_encoded
        test_array = np.array([test_array])

        # Make prediction
        prediction = model.predict(test_array)[0]

        return render_template(
            "index.html",
            prediction_text=f"💡 Predicted Charges: ${prediction:.2f}"
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
