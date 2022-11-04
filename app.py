from flask import Flask, render_template, request
import requests
import warnings

warnings.filterwarnings('ignore')


app = Flask(__name__)

@app.route('/', methods=['GET'])
def app_home():
    return render_template("index.html")


@app.route('/predict/', methods=['POST'])
def result():    
    if request.method == 'POST':
        return render_template("prediction.html",
                               date_=date,
                               value0=day_pred[0], 
                               value1=day_pred[1], 
                               value2=day_pred[2],
                              value3=day_pred[3])


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4000,)