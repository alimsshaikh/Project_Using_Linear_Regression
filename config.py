import os
PORT_NUMBER = 5000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_FILE_PATH = os.path.join(BASE_DIR, 'Build_new_model_Medical_insurance.pkl')
JSON_FILE_PATH = os.path.join(BASE_DIR, 'labelEncoding.json')