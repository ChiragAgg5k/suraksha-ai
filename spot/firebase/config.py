import pyrebase
from os import environ

firebaseConfig = {
    "apiKey": environ.get("FIREBASE_API_KEY"),
    "authDomain": environ.get("FIREBASE_AUTH_DOMAIN"),
    "projectId": environ.get("FIREBASE_PROJECT_ID"),
    "storageBucket": environ.get("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": environ.get("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": environ.get("FIREBASE_APP_ID"),
    "databaseURL": environ.get("FIREBASE_DATABASE_URL"),
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
