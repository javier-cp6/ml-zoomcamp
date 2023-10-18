import pickle

dv_file = 'dv.bin'
model_file = 'model1.bin'

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)
    
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)


def predict(customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    credit = y_pred >= 0.5

    result = {
        'credit_probability': float(y_pred),
        'credit': bool(credit)
    }

    print(result)
    return result


customer = {"job": "retired", "duration": 445, "poutcome": "success"}

predict(customer)