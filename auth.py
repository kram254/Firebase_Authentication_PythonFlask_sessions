import pyrebase

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

email = 'markorlando45@gmail.com'
password = 'pass1234'

### We do not need to run this again the user is already created
#user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email, password)

### These lines print the details/info of the user
# info  = auth.get_account_info(user["idToken"])
# print(info)

auth.send_email_verification(user['idToken'])

auth.send_password_reset_email(email)
