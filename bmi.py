from pywebio.input import *
from pywebio.output import *

def bmi_cal():
    
    height = input('Enter height : ', type = FLOAT)
    weight = input('Enter weight : ', type = FLOAT)
    
    BMI = weight / (height / 100) ** 2
    
    check = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    
    for i,j in check:
        if BMI <= i:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, j))
            break
            
if __name__ == '__main__':
        bmi_cal()
