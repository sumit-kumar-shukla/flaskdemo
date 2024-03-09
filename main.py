from flask import Flask, render_template, request, redirect, url_for
import pickle
from flask.helpers import url_for

from werkzeug.utils import redirect
app = Flask(__name__)

@app.route('/', methods= ['GET',"POST"])
def home():
    prediction=[0]
    print(request.method)
    if request.method == "POST":
        model = pickle.load(open('lm_model.pkl','rb'))
        RTI = int(request.form.get('RTI'))
        RTS = int(request.form.get('RTS'))
        RTE = int(request.form.get('RTE'))
        NNCOP = int(request.form.get('NNCOP'))
        NICOP = int(request.form.get('NICOP'))
        NPPFSC = int(request.form.get('NPPFSC'))
        NPPFRR = int(request.form.get('NPPFRR'))
        FDP = int(request.form.get('FDP'))
        RPPS = int(request.form.get('RPPS'))
        RPPF = int(request.form.get('RPPF'))
        NSDPEGI = int(request.form.get('NSDPEGI'))
        NSDPEPI = int(request.form.get('NSDPEPI'))
        FPG = request.form.get('FPG')
        print(FPG)

        if FPG=='Yes':
            FPG = 1
        elif FPG =='No':
            FPG = 0
        
        print(type(FPG))

        FPP = request.form.get('FPP')
        print(FPP)

        if FPP=='Yes':
            FPP = 1
        elif FPP =='No':
            FPP = 0
        
        print(type(FPP))

        PICES = request.form.get('PICES')
        print(PICES)

        if PICES=='Yes':
            PICES = 1
        elif PICES =='No':
            PICES = 0

        PSIESC = int(request.form.get('NPIESC'))
        NSD = int(request.form.get('NSD'))
        NSL = int(request.form.get('NSL'))
        NSSI = int(request.form.get('NSSI'))
        NPF = int(request.form.get('NPF'))

        # MERGING COLLECTED DATA TO DF2
        NWSC   = RTI + RTS + RTE
        NCO    = NNCOP + NICOP
        RRK    = NPPFRR + NPPFSC
        RPP    = RPPF + RPPS
        FDP    = FDP
        EMP    = NSDPEGI + NSDPEPI
        FP     = FPG + FPP
        PSIESC = PSIESC
        PICES  = PICES
        SD     = NSD
        SL     = NSL
        SSV    = NSSI
        PF     = NPF
        print(NWSC, NCO, RRK, EMP, RPP, FDP, FP, PSIESC, PICES, SD, SL, SSV, PF)
        #print(user_input, type(user_input))
        #user_input = float(user_input)
        prediction = model.predict([[NWSC, NCO, RRK, EMP, RPP, FDP, FP, PSIESC, PICES, SD, SL, SSV, PF]])
        #print(prediction)
    return render_template('newfile.html', prediction=prediction[0])
    #return redirect(url_for('prediction',prediction=prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/get_prediction')
def Pred(prediction):
    return ('Predicted Score is', prediction)
    #http://52.66.214.162:5000/