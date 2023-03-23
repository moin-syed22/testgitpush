import pymongo
client = pymongo.MongoClient("mongodb+srv://moin:AZibKzndLCDsoTmU@cluster0.de0tvyf.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database['basicinfo']

#record = collection.find()
#for i in record:
#    print(i)

#data = collection.find({"companyName" : "iNeuron"})
data = collection.find({"courseOffered" : {"$gt" : "E"}})
for i in data:
    print(i)
