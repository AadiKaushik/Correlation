import csv 
import numpy as np 

def setup():
    dataPath = 'C:/Users/aadi_/Desktop/coding/python/dataVisulation/Student Marks vs Days Present.csv'

    data = getData(dataPath)

    findCorrelation(data)

def getData(dataPath):
    marks_in_percentage = []
    days_Present = []
    
    with open(dataPath) as f :
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            marks_in_percentage.append(float(row['Marks In Percentage']))
            days_Present.append(float(row['Days Present']))

    return {'x' : marks_in_percentage,'y' : days_Present}        

def findCorrelation(data):
    correlation = np.corrcoef(data['x'],data['y'])
    print(correlation[0,1])

setup()    
