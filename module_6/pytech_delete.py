import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.oai9kyi.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]



   
post4 = {"_id": 1010, "First Name": "Golem", "Last Name": "Smegel"}

collection.insert_one(post4)

print("\nList of students:")
student_list = collection.find({})
for student in student_list:
   print(student)


find = collection.find_one({"_id": 1010}) 

print("\nDo you really want to delete this file: y/n?")
print(find)

delete = collection.delete_one({"_id": 1010}) 
print("\nShowing deleted student:")
print(delete)
