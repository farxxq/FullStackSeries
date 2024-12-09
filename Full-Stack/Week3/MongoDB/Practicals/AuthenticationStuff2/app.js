const express = require('express');
const app = express();
const userModel = require('./models/userModel')
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');
const path = require('path');

app.set('view engine', 'ejs');
app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req,res)=>{
    res.render("index");
});

app.post('/create', async(req,res)=>{
    let {username,email,password,age} = req.body
    bcrypt.genSalt(10, (err,salt)=>{
        bcrypt.hash(password, salt, async(err,hash)=>{
            await userModel.create({
                username,
                email,
                password: hash,
                age
            });
        });
    });
    let token = jwt.sign({email}, "love");
    res.cookie("token", token);
    console.log(token);
    res.send('The user is created');
})

app.listen(3000);