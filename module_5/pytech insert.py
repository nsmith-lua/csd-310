import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.oai9kyi.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

post1 = {"_id": 1007, "First Name": "Aragorn", "Last Name": "son of Arathorn"}
post2 = {"_id": 1008, "First Name": "Frodo", "Last Name": "Baggins"}
post3 = {"_id": 1009, "First Name": "Gandolf", "Last Name": "The Grey"}

collection.insert_many([post1, post2, post3])
