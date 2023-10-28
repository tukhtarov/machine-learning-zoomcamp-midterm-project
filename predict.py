import pickle
from flask import Flask
from flask import request
from flask import jsonify

output_file = 'model.bin'

with open(output_file, 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

app = Flask('deposit_prediction')  

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    # client = {'age': 59.0,
    #             'job': 'admin.',
    #             'marital_status': 'married',
    #             'education': 'secondary',
    #             'credit_in_default': 'no',
    #             'average_balance': 2343.0,
    #             'has_housing_loan': 'yes',
    #             'has_personal_loan': 'no',
    #             'contact_type': 'unknown',
    #             'day': 5.0,
    #             'month': 'may',
    #             'duration': 1042.0,
    #             'number_contacts': 1.0,
    #             'pdays': -1.0,
    #             'number_contacts_before': 0.0,
    #             'previous_outcome': 'unknown'}
    X_client = dv.transform([client])
    y_pred = model.predict_proba(X_client)[0, 1]
    result = {
       'deposit_subscription_probability': y_pred
    }
    return jsonify(result)



if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=9696)
