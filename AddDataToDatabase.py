import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':".................................................."
})

ref = db.reference('Students')

data = {

    "1126":
        {
                "name":"...................... ",
                "major":"...............",
                "starting_year":"..................",
                "total_attendance":".........",
                "standing":"...........",
                "year":.........,
                "last_attendance_time": "..................."

        },
    "1011":
        {
                "name":"................ ",
                "major":".........",
                "starting_year":"..........",
                "total_attendance":".......",
                "standing":"......",
                "year":.........,
                "last_attendance_time": "......................"

        }

}

for key,value in data.items():
    ref.child(key).set(value)
