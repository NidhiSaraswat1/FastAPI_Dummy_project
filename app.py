# Handling all the API points here
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from Model.predict import predict_output,model, MODEL_VERSION
import pandas as pd
app = FastAPI()

        
# creating a home endpoint for the API 
@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction API'}

# while hosting this API on AWS it demands a health endpoint so this is for machine reading not human use while the home one is ofr human readability.    
@app.get('/health')
def health_check():
     return {
         'status':'working',
         'built_by':'Nidhi Saraswat',
         'version': MODEL_VERSION,
         'model_loaded':model is not None
     }
    
# creating the endpoint for prediction
@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data:UserInput):

# giving the input to the model in the form of pandas df 
    user_input = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }])
    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200,content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))