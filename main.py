import os
from flask import Flask, render_template, request

app = Flask(__name__)

# make upload photo directory
path = os.path.join("uploads/photo")
os.makedirs(path, exist_ok=True)

    
#check file format
allowed_format = {'txt','jpg','png'}
def check_file_format(fileName):
    return '.' in fileName and fileName.rsplit('.', 1)[1] in allowed_format

@app.route('/')
def index():
    return render_template('index.html') 


#Get Data from URL
@app.route('/result', methods=['POST'])
def show_result():
    email = request.form['email']
    password = request.form['password']
    return render_template('result.html', email=email, password=password)

# File upload
@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/upload_result', methods=['POST'])
def upload_result():
    file = request.files['file']
    if check_file_format(file.filename):
        try:
            file.save(os.path.join(path, file.filename))
            return 'Uploaded'
        except Exception as e:
            return f"the error is {e}"
    else:
        return "file format is not allowed..."

    