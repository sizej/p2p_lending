import pandas as pd 
import numpy as np 

if __name__ == '__main__':
    data = pd.read_csv('data/Master_Loan_Summary.csv')
    grade_dict = {}
    for g in data['grade'].unique():
        m0 = data['grade'] == g
        m1 = data['loan_status_description'] != 'CURRENT'
        loans = data[m0 & m1].shape[0]
        m2 = data['loan_status_description'] == 'CHARGEOFF'
        chargeoffs = data[m0 & m2].shape[0]
        m3 = data['loan_status_description'] == 'DEFAULTED'
        defaults = data[m0 & m3].shape[0]
        grade_dict[g] = {'Chargeoff': chargeoffs/loans, 'Default': defaults/loans}
    grade = pd.DataFrame(grade_dict)
    print(grade)