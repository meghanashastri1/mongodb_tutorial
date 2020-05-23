import pymongo
import dns


#connect to mongodb cloud cluster
#client = pymongo.MongoClient("mongodb+srv://<root1>:<mongodb>@cluster0-sfquv.gcp.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["database"]

#create new collection called inventory
col = db["inventory"]


#added variables because I had errors saying that the keys item, qty, status, size, h, w, uom, and tags didnt exist
item = "item"
qty = "qty"
status = "status"
size = "size"
h = "h"
w = "w"
uom = "uom"
tags = "tags"


#list of documents to insert into inventory collection
list = [
   {item: "journal", qty: 25, status: "A", size: {h: 14, w: 21, uom: "cm"}, tags: ["blank", "red"]},
   {item: "notebook", qty: 50, status: "A", size: {h: 8.5, w: 11, uom: "in"}, tags: ["red", "blank"]},
   {item: "paper", qty: 10, status: "D", size: {h: 8.5, w: 11, uom: "in"}, tags: ["red", "blank", "plain"]},
   {item: "planner", qty: 0, status: "D", size: {h: 22.85, w: 30, uom: "cm"}, tags: ["blank", "red"]},
   {item: "postcard", qty: 45, status: "A", size: {h: 10, w: 15.25, uom: "cm"}, tags: ["blue"]}
]

#populate collection
x = col.insert_many(list)

print(x)

#return all documents
db.col.find({})

#format the result of returning documents
#db.col.find({}).pretty()

#return documents where status = D
db.col.find( { status: "D" } );

#return documents where qty = 0
db.col.find( { qty: 0 } );

#return documents where status = D and qty = 0
db.col.find( { qty: 0, status: "D" } );

#return documents where uom in size = in
db.col.find( { "size.uom": "in" } )

#return documents where size has fields h = 14, w = 21, uom = cm
db.col.find( { size: { h: 14, w: 21, uom: "cm" } } )

#return documents where tags array contains an element "red"
db.col.find( { tags: "red" } )

#return documents where tags array contains an element "red" in the sepcified order
db.col.find( { tags: [ "red", "blank" ] } )

#return _id, item, and status fields from col
db.col.find( { }, { item: 1, status: 1 } );

#exclude the _id field by setting it to 0
#db.col.find( {}, { _id: 0, item: 1, status: 1 } );
