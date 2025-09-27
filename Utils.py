import pickle
import json
import numpy as np
import config

class MedicalInsurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region  = 'region_' + region 


    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)


        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_predict_charges(self):
        self.load_model()
        column_names =  self.model.feature_names_in_


        region_index = np.where(column_names == self.region)[0]

        test_array = np.zeros((1,len(column_names)))
        test_array[0,0] = self.age # 34
        test_array[0,1] = self.json_data['gender'][self.gender]
        test_array[0,2] = self.bmi
        test_array[0,3] = self.children
        test_array[0,4] = self.json_data['smoker'][self.smoker]

        print("TEST_ARRAY:",test_array) # 9 values

        predict_charges = self.model.predict(test_array)

        return predict_charges


# if __name__ == "__main__":
#     age = 35
#     gender = 'male'
#     bmi = 26.9
#     children  = 2
#     smoker = 'no'
#     region = 'southeast'

#     med_insu = MedicalInsurance(age,gender,bmi,children,smoker,region)
#     med_insu.get_predict_charges()