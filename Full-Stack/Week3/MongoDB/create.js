// Create operations

// To insert one
db.Employees.insertOne(
    { 
        name: "Faroo",
        Role: "Front-end"
    }
)

db.Employees.insertMany(
    [
        { 
            name: "Faroo",
            Role: "Front-end"
        },
        { 
            name: "Sah",
            Role: "Back-end"
        },
        { 
            name: "Safar",
            Role: "FullStack"
        },
        { 
            name: "Sa",
            Role: "Technician"
        }
    ]
)