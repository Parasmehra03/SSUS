from pymongo import MongoClient

try:
    MONGO_URI = "mongodb+srv://parasmehra0303_db_user:Panjara%40123@cluster0.jx6gghp.mongodb.net/?appName=Cluster0"

    client = MongoClient(MONGO_URI)

    client.admin.command("ping")

    db = client["ssus"]

    student_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]

    print("MongoDB Connected Successfully")

except Exception as e:
    print("MongoDB error:", e)   


    

    
