const express = require('express');
const app = express();

app.get('/', (req,res)=>{
    res.send("Assalamwalaikum")
})

app.get('/love', (req,res)=>{
    res.send("I love you yaar, Sa")
    console.log("I love you meri noor")
})

app.listen(3000,()=>{
    console.log("Server is running");
});