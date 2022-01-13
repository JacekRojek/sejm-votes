import pandas as pd

deputies = pd.read_csv('mps.csv')

deputy = deputies[(deputies['first_name'] == 'Andrzej') & (deputies['last_name'] == 'Adamczyk')]
print('deputy')
print(deputy)