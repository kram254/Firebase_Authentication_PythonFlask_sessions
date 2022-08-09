from flask import Flask, session, render_template, redirect, request
import pyrebase

app = Flask(__name__)

config = {    
  'apiKey': "AIzaSyBmEoZnRQLVHWaqWsf3--w88l0Ueovjyno",
  'authDomain': "python-authentication-cbdf4.firebaseapp.com",
  'projectId': "python-authentication-cbdf4",
  'storageBucket': "python-authentication-cbdf4.appspot.com",
  'messagingSenderId': "136200064542",
  'appId': "1:136200064542:web:6c45e0e08eaa823cda680f",
  'measurementId': "G-GJVKPRZXP4",
  'databaseURL': " "
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secretkey'

@app.route('/', methods= ['POST', 'GET'])
def index():
    if ('user' in session):
        return 'Hello, {}'.format(session['user'])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
        except:
            return "Failed to login."    
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
