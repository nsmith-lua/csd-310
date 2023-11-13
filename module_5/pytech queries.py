from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority")
db = client.pytech
students = db.students
student_list = students.find({})
                     
                     
print("\n")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

Gandolf = students.find_one({"student_id": "1009"})

print("  Student ID: " + Gandolf["student_id"] + "\n  First Name: " + Gandolf["first_name"] + "\n  Last Name: " + Gandolf["last_name"] + "\n")

