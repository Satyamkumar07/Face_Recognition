# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 18:11:11 2021

@author: Satyam
"""

from flask import Flask, request, render_template
import os
import json
from face_util import compare_faces, face_rec

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

                                          
@app.route('/face_rec', methods=['POST'])
def face_recognition():
    if request.method == 'POST':
        baseImage = request.form['baseImage']
        EmpID = request.form['EmpID']
        name = face_rec(baseImage,EmpID)
        resp_data = {'name': 'Login Successful for '+name }
        
        return json.dumps(resp_data['name'])           
    
# When debug = True, code is reloaded on the fly while saved
app.run(debug=True)