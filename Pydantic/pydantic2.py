from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import List, Dict, Optional,Annotated

# Pydantic Model
class Patient(BaseModel):
# defining the schema
# by default all these fields are required
    name: Annotated[str,Field(max_length=50,title='Name of the patient',description='give the name of the patient in less than 50 characters',examples=['Nidhi','Himanshu'])] # here field is setting metadata
    age:int = Field(gt=0,lt=100,strict=True) #here field is setting constraints
    linkedIn:Annotated[AnyUrl,Field(default=None,description='is linkedin available or not')] #Field for setting default values
    email: EmailStr
    married:bool = False #setting default value
    # if you want to store patient' alergies in a list
    # Optional makes the field optional to fill
    allergies: Optional[List[str]] = None #this type of syntax is used to validate not only the data is in List but also string so like 2 validations in dict too
    contact_details:Dict[str,str]


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('inserted into db')


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated into db')

patient_info = {'name':'nidhi','age': 21,'contact_details':{'email':'saraswatnidhi@gmail.com','phone':'416176'}}

# object for patient class
patient1 = Patient(**patient_info) #unlocking the dictionary

insert_patient_data(patient1)