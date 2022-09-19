from crypt import methods
from enum import unique
import os
from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# make upload photo directory
path = os.path.join("uploads/photo")
os.makedirs(path, exist_ok=True)

# config database
file_dir = os.path.dirname(__file__)
db_dir = os.path.join(file_dir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_dir
db = SQLAlchemy(app)

# class ORM like django
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    
# FOR ONCE YOU CREATE THE DATABASE
# db.create_all()
    
#check file format
allowed_format = {'txt','jpg','png'}
def check_file_format(fileName):
    return '.' in fileName and fileName.rsplit('.', 1)[1] in allowed_format

# check cookies set or not
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)


#Get Data from URL and set Cookies
@app.route('/result', methods=['GET','POST'])
def show_result():
    try:
      username = request.form['username']
      email = request.form['eamil']
    #   password = request.form['password']
      user = User(username = username, email = email)
      db.session.add(user)
      db.session.commit()
      
      response = make_response('sucssful save to db...') #this line can set render_template
    #   response.set_cookie('user_email', email)
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


if __name__ == "__main__":
    app.run(debug=True)