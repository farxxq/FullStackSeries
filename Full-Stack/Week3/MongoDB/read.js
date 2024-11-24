// Read operations

db.Roles.find() // To find all the data
db.Roles.find({}) // To find all the data

// To find a particular data
db.Roles.find(
    {
    Role: "FullStack"
    }
) // To find a particular data

// Real all the docs with these 2 datas in the Role key
db.Roles.find(
    {
        Role: {$in: ["Front-end","Python"]}
    }
) 
// AND condition (don't need to mention (the commas work))
db.Roles.find(
    {
        name: "Faroo", Role: {$in: ["Front-end","Python"]}
    }
)

// OR condition (Need to mention and also have the Keys in {})
db.Roles.find(
    {
      $or: [{name: "Farooq"}, {Role: {$in: ["Front-end","Python"]}}]
    }
)