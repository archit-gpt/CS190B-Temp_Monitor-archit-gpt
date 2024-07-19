import pyrebase

config = {
  "apiKey": "AIzaSyBtW_20F2VotiOd0f8LYF9NmE5_O_jHnZI",
  "authDomain": "cs190b-final-project.firebaseapp.com",
  "databaseURL": "https://console.firebase.google.com/u/0/project/cs190b-final-project/firestore/data/~2Fpi~2Fdata",
  "storageBucket": "cs190b-final-project.appspot.com"
}

firebase = pyrebase.initialize_app(config)
