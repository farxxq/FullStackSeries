const express = require('express')
const app = express();

const userModel = require('./usermodel')

app.get('/', (req,res)=>{
    res.send("Assalamwalaikum,Change the url to see the working of the commands")
})

// Create a user
app.get('/create',async (req,res)=>{
    let createduser = await userModel.create(
        {
            name: "Farooq",
            email: "faroo@gmail.com",
            username: "Faroo"
        }
    )
    res.send(createduser)
    console.log("User is created",createduser)
})

app.get('/create',async (req,res)=>{
    let createduser = await userModel.create(
        {
            name: "Love",
            email: "love@gmail.com",
            username: "Far"
        }
    )
    res.send(createduser)
    console.log("User is created",createduser)
})

// Read the documents or find the documents
app.get('/read',async (req,res)=>{
    let readuser = await userModel.find()
    res.send(readuser)
    console.log("Users are read",readuser)
})

// Read a specific document or find a specific document
app.get('/readUser',async (req, res)=>{
    let readOneUser = await userModel.find({name: "light"})
    res.send(readOneUser)
    console.log("Read one user:", readOneUser)
})

// Read the first occuring document
app.get('/readOne',async (req, res)=>{
    let readOneUser = await userModel.findOne({name: "Love"})
    res.send(readOneUser)
    console.log("Read one user:", readOneUser)
})

// Update the data of a user
app.get('/update',async (req,res)=>{
    let updateuser = await userModel.findOneAndUpdate(
        {
            username: "Faroo"
        },{
            name: "light"
        },{
            new: true
        }
    )
    res.send(updateuser)
    console.log("User is updated",updateuser)
})

// Delete the document
app.get('/delete', async (req,res) =>{
    let deleteUser = await userModel.findOneAndDelete({name: "Farooq"})
    res.send(deleteUser)
    console.log("The account is deleted:", deleteUser)
})

app.listen(3000)