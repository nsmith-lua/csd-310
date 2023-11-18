from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.oai9kyi.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
students = db["students"]


results = students.find({})
#students.find( {"_id": 1007})


for result in results:
    print(result)
