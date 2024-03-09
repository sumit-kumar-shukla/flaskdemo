import requests, json 
# sample request 
data = {'NWSC': {0: 19}, 'NCO': {0: 6}, 'RRK': {0: 12}, 'RPP': {0: 6}, 'FDP': {0: 5}, 'EMP': {0: 8},
 'FP': {0: 1}, 'PICES': {0: 1}, 'PSIESC': {0: 8}, 'SD': {0: 48}, 'SL': {0: 48}, 'SSV': {0: 9}, 'PF': {0: 4}} 
# Hitting the API with a POST request 
ot = requests.post(url='http://127.0.0.1:5000/get_prediction', json=json.dumps(data)) 
print(ot.json())# Response JSON