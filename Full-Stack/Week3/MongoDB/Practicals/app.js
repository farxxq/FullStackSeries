const express = require('express')
const app = express();

const userModel = require('./usermodel')

app.get('/', (req,res)=>{
    res.send("hey")
})

app.get('/create',async (req,res)=>{
    let createduser = await userModel.create(
        {
            name: "Farooq",
            email: "faroo@gmail.com",
            username: "Faroo"
        }
    )
    res.send(createduser)
    console.log("User is created")
})

app.listen(3000)