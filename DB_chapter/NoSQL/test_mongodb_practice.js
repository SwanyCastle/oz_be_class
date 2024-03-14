db.users.insertMany([
    { name: "Bob", age: 25, address: "456 Oak St" },
    { name: "Charlie", age: 35, address: "789 Pine St" }
])
db.users.insertOne({ name: "Alice", age: 30, address: "123 Maple St" })
db.users.find()
db.users.find({}, { name:1 })
db.users.find({}, { name:1, address:1 })
db.users.find({}, {address:"Maple "})
db.users.updateOne({ name:"Bob" }, { $set: { age:31 }})
db.users.updateMany({ name:"Bob" }, { $set : { age: 30 } })

db.users.deleteOne({ name:"Bob" })
db.users.deleteMany({ name:"Alice" })

db.users.aggregate([
    { $group: { _id: null, avgAge: { $avg: "$age" } } }
])