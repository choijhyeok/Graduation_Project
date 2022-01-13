# 필요한 패키지 import 하는것 
from flask import Flask, render_template
import flask
from flask import Flask, request, render_template

import Recognize
import Capture_Image
import Train_Image
# 여기서 flask 로컬호스트를 여는 부분
import numpy as np
app = Flask(__name__)
import os

# 웹 시작했을때 첫화면에 나오는 html 정의한것
@app.route("/")


@app.route("/gnu.html")
def gnu():
    return render_template('gnu.html')

# 웹 상에서 iframe을 통해서 띄울 목록들을 flask가 인식하도록 하는것
@app.route("/register.html", methods=['POST','GET'])
def register():
    global gnu_id,name
    if request.method == 'POST':
        gnu_id = request.form.get('Gnu_id')
        name = request.form.get('name')
        gnu_id = str(gnu_id)
        name = str(name)
        Capture_Image.takeImages(gnu_id,name)
        Train_Image.TrainImages()
    return render_template('register.html')

@app.route("/professor_register.html")
def professor_register():
    return render_template('professor_register.html')

@app.route("/professor_page.html")
def professor_page():
    return render_template('professor_page.html')

@app.route("/student_page.html", methods=['POST','GET'])
def student_page():
    Recognize.recognize_attendence()
    return render_template('student_page.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/professor_login_form.html")
def professor_login_form():
    return render_template('professor_login_form.html')
    
# flask 실행 자동화 하는 부분
if __name__ == '__main__':
    app.run(debug=True)
