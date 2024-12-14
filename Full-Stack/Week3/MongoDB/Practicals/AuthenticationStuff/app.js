const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');
const bcrypt = require('bcrypt'); // It is used to encrypt and decrypt
const jwt = require('jsonwebtoken');

// To read the cookies
app.use(cookieParser());

//cookies being set
app.get('/', (req,res)=>{
    res.cookie("name", "Sa");
    res.send("Cookie added");
})

//cookies being read
app.get('/read', (req,res)=>{
    console.log(req.cookies)
    res.send("Read Page")
})

//bcrypt - encrypt the password (Use the genSalt)
app.get('/bcrypt', (req,res)=>{
    bcrypt.genSalt(10, (err,salt)=>{
        bcrypt.hash('Safar', salt, (err, hash)=>{
            console.log("hash:",hash)
        });
    });
    res.send("Check the console for the hash value")
})

//bcrypt - decrypt the password (Use the compare)
app.get('/decrypt',(req,res)=>{
    bcrypt.compare("Safar", "$2b$10$suXEj.GGz5fe9oN0nIq/duHHg2JO98ImIqcd9VaavqJevh6xXpO.u", (err,result)=>{
        console.log(result) // used to check whether both the password and the hash value is same or not
    })
    res.send('The decrypt is correct or not? Check the console')
})

// JWT
app.get('/jwt', (req,res)=>{
    let token = jwt.sign({email: "Sah@mail.com"}, "love") // to hash send a unique string with the 3 types
    console.log(token)
    res.cookie("token", token)
    res.send("Check the console")
});

// JWT read
app.get('/jwtRead',(req,res)=>{
    console.log(req.cookies.token)
    let data = jwt.verify(req.cookies.token, "love") // to read the data 
    console.log(data)
    res.send("Check the console for the verification")
})


app.listen(3000)