import os
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

# make upload photo directory
path = os.path.join("uploads/photo")
os.makedirs(path, exist_ok=True)

    
#check file format
allowed_format = {'txt','jpg','png'}
def check_file_format(fileName):
    return '.' in fileName and fileName.rsplit('.', 1)[1] in allowed_format

# check cookies set or not
@app.route('/')
def index():
   if request.cookies.get('user_email'):
       return f"hello {request.cookies.get('user_email')}"
   else:
       return render_template('index.html')


#Get Data from URL and set Cookies
@app.route('/result', methods=['POST'])
def show_result():
    email = request.form['email']
    password = request.form['password']

    try:
      response = make_response('sucssful ...')
      response.set_cookie('user_email', email)
      return response
    except Exception as e:
      return f"ooops error is  {e}"
    # return render_template('result.html', email=email, password=password)

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

# Error Page 
@app.errorhandler(404)
def show_error(error):
    return render_template('error_page.html'), 404