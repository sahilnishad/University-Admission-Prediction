from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        GRE_Score = int(request.form['GRE_Score'])
        TOEFL_Score = int(request.form['TOEFL_Score'])
        University_Rating = int(request.form['University_Rating'])
        SOP = float(request.form['SOP'])
        LOR = float(request.form['LOR'])
        CGPA = float(request.form['CGPA'])
        Research = int(request.form['Research'])

        input = pd.DataFrame([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]])
        
        output = model.predict(input)[0][0]
        output_ = round((output*100), 2)
    
    return render_template("index.html", result=output_)


if __name__ == "__main__":
    app.run(debug=True)