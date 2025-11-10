# here we are making predictions for the ML model.
import pickle
import pandas as pd

# import the ML model
with open('model/model.pkl','rb') as f:
    model = pickle.load(f)

#showing model version self defined for now generally it comes from an appication called as MLFlow
MODEL_VERSION = '1.0.0'

# get class labels from model(important for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input:dict):
    df = pd.DataFrame(user_input)

    #provides the first prediction from the list of predictions by the model
    predicted_class = model.predict(df)[0]

    # get the probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    #create mapping : {class name:probability}
    class_probabs = dict(zip(class_labels,map(lambda p: round(p,4),probabilities)))
    
    return {
        "predicted_category":predicted_class,
        "confidence": round(confidence,4),
        "class_probabilities":class_probabs
    }

