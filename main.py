import pymongo
client = pymongo.MongoClient("mongodb+srv://mazumderrohan:Deepmind2022@cluster0.dytye.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name":"rohan", "email":"mazumderrohan1@gmail.com","surname":"mazumder"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)