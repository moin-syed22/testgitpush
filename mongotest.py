import pymongo
client = pymongo.MongoClient("mongodb+srv://moin_syed:gpPEfkOYg650F7ZT@clustermoin.kv5mxmg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "moin",
    "email" : "moinsyed@gmail.com",
    "surname" : "syed"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
