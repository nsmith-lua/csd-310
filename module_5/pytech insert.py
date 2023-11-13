import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.oai9kyi.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]
#
#post = {"_id":1007, "First Name": "Strider", "Last Name": "NA"}
#post = {"_id":1008, "First Name": "Frodo", "Last Name": "Baggins"}
post = {"_id": 1009, "First Name": "Gandolf", "Last Name": "Wizard"}
#
collection.insert_one(post)
#pyth