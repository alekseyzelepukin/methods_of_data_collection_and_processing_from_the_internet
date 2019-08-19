from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')
db = client['testdb']
testdb = db.testdb
testdb.insert_many([{'name':"test abc",
                   'size': 2000,
                   'author': "Mike Dowson"},

                    {'name':"Name space",
                   'size': 1500,
                   'author': "Peter Pan",
                     'age': 56}
                    ])
objects = testdb.update_many({'size': {'$gt':1000}},
                            {'$set': {'name':'smallsize'}})

objects = testdb.find().sort('size',)
for i in objects:
    print(i)
