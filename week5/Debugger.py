
#Week5-Debugger

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)


for patient in patients:
    print("patient:", patient)
    weight, height = patient[0], patient[1]
    print("weight:", weight)
    print("height:", height)
    bmi = calculate_bmi(weight, height)
    print("The Patients BMI are: %f" % bmi)
