const express = require('express');
const app = express();
const path = require('path');

app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public'))); // used to access the public folder (the whole path will come here)
app.set('view engine', 'ejs'); //like html but can do calculations

app.get('/',function(req,res){
    res.render("index");
})

//username is considered as a variable here
app.get("/profile/:username",function(req,res){
    // req.params.username //this gets the username
    res.send(`Welcome, ${req.params.username}`);
    console.log(`Welcome, ${req.params.username}`)
})

app.get("/profile/:username/:age",function(req,res){
    res.send(`Welcome, ${req.params.username} of age ${req.params.age}`);
    console.log(`Welcome, ${req.params.username} of age ${req.params.age}`)
})

app.listen(3000,function(){
    console.log("The server is running");
})

