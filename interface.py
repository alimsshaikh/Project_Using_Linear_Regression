from flask import Flask, render_template, jsonify, request
from Utils import MedicalInsurance
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    """Render the home page with the insurance prediction form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_insurance_charges():
    """
    Predict medical insurance charges based on user input.
    
    Returns:
        JSON response containing the predicted charges or error message
    """
    try:
        # Get form data
        data = request.form
        
        # Validate required fields
        required_fields = ['age', 'gender', 'bmi', 'children', 'smoker', 'region']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Process input data
        age = int(data['age'])
        gender = data['gender'].lower()
        bmi = float(data['bmi'])
        children = int(data['children'])
        smoker = data['smoker'].lower()
        region = data['region'].lower()
        
        # Create insurance prediction instance
        med_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
        
        # Get prediction
        charges = med_ins.get_predict_charges()
        
        return jsonify({
            "status": "success",
            "prediction": float(charges[0]),
            "message": "Prediction successful"
        })
        
    except ValueError as e:
        return jsonify({"error": f"Invalid input data: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)