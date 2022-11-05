from flask import Flask, render_template, request
import warnings

warnings.filterwarnings('ignore')
import socket


name = socket.gethostname().split('.')[0]

app = Flask(__name__)


@app.route('/', methods=['GET'])
def app_home():
    
    return render_template("index.html", name=name)


@app.route('/submit/', methods=['POST'])
def result():    
    if request.method == 'POST':
        print(request.form.get('name'))
        print(request.form.get('email'))
        return render_template("submit.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4000,)