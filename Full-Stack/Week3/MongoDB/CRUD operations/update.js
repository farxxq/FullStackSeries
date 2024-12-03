// Update operations

db.Roles.updateOne(
    {Role:"Back-end"},
    {
        $set: {Role:"Front-end"},
        $currentDate: {lastModified: true}
    },
    
)