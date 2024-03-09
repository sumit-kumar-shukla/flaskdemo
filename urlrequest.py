from flask import Flask, request, jsonify
import json, pickle

app = Flask(__name__)

@app.route('/get_prediction',methods=['POST'])
def Get_Prediction():
    input_score =json.loads(request.get_json())
    print(input_score)
    print(input_score['NWSC'])
    model = pickle.load(open('lm_model.pkl','rb'))
    NWSC = int(input_score['NWSC']['0'])
    NCO = int(input_score['NCO']['0'])
    RRK = int(input_score['RRK']['0'])
    RPP = int(input_score['RPP']['0'])
    FDP = int(input_score['FDP']['0'])
    EMP = int(input_score['EMP']['0'])
    FP = int(input_score['FP']['0'])
    PSIESC = int(input_score['PSIESC']['0'])
    PICES = int(input_score['PICES']['0'])
    SD = int(input_score['SD']['0'])
    SL = int(input_score['SL']['0'])
    SSV = int(input_score['SSV']['0'])
    PF = int(input_score['PF']['0'])
    prediction = model.predict([[NWSC, NCO, RRK, RPP, FDP, EMP, FP, PSIESC, PICES, SD, SL, SSV, PF]])
    print(prediction)
    return jsonify({'Your Predicted Score is ':prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    host='study-major-mic.cdmr7t2fp3ky.ap-south-1.rds.amazonaws.com', port=3306)


