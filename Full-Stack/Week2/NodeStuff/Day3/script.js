// Express is a npm package 
// Express is a framework (gives a flow and we have to follow that. But we can take any way to complete that flow)
// React JS is a library (Tools are given and we can use to perform something)

// This Express js manages everything from receiving the request and giving the response

 const express = require("express")
 const app = express()

 //no we can create the routes....... (google.com/route_name)

 app.get('/',function(req, res) {
    res.send("Hello world")
 })

 app.listen(3000)