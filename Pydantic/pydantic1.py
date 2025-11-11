# Why we use pydantic

# here we are taking patient data for exmaple

def insert_patient_data(name,age):
    print(name)
    print(age)
    print("inserted into database")

insert_patient_data('nidhi','thirty')
# here as we can see though age being an integer variable took 'thirty' which is a string so this is a problem to solve this typa problem we use pydantic.Here type validation is not happening.

# We can use 2 methods to solve this problem
# 1.type hinting: gives info and doesn't raise error on giving wrong info
# 2. Manually coding to check the error type
# 3. Using Pydantic.
def Update_patient_data(name,age):
    print(name)
    print(age)
    print("inseted into database")