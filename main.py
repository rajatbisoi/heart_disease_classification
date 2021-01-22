
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

application = Flask(__name__) 
app=application
@app.route('/',methods=['GET']) 
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            
            age = float(request.form['age'])
            cp = float(request.form['cp'])
            trestbps = float(request.form['trestbps'])
            chol = float(request.form['chol'])
            fbs = float(request.form['fbs'])
            restecg = float(request.form['restecg'])
            thalach = float(request.form['thalach'])
            is_research = request.form['sex']
            exang = float(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = float(request.form['slope'])
            ca = float(request.form['ca'])
            thal = float(request.form['thal'])
            if(is_research==1):
                sex=1
            else:
                sex=0
            filename = 'finalized_model.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) 
          
            prediction=loaded_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
            print('prediction is', prediction)
      
            return render_template('results.html',prediction)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
   
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    application.run(debug=True) 
