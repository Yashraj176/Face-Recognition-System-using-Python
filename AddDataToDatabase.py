import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendacerealtime-bf845-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

    "1126":
        {
                "name":"Yash Raj Singh ",
                "major":"MCA",
                "starting_year":"2021",
                "total_attendance":"4",
                "standing":"G",
                "year":2,
                "last_attendance_time": "2022-09-28 00:54:34"

        },
    "1011":
        {
                "name":"Sharad Gupta ",
                "major":"MCA",
                "starting_year":"2021",
                "total_attendance":"2",
                "standing":"G",
                "year":2,
                "last_attendance_time": "2022-02-18 00:54:34"

        }

}

for key,value in data.items():
    ref.child(key).set(value)