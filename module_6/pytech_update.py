import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.oai9kyi.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

student_list = collection.find({})
for student in student_list:
   print(student)

result = collection.update_one({"_id": 1007}, {"$set": {"Last Name": "King of Gondor"}}) 

student_list = collection.find({})
for student in student_list:
   print(student)

