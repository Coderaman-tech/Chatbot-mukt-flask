from flask import Flask,request,jsonify
from mukti_bot import  chatbot_main
import pickle
import numpy as np



app=Flask(__name__)


@app.route('/')

def home():
    return "Hello World"

@app.route('/predict',methods=['POST'])

def predict():
    message=request.form.get('message')
    result=chatbot_main(message)
    return jsonify({'response':result})

if __name__=='__main__':
    app.run(debug=True)