// Express is a npm package
// Express is a framework (gives a flow and we have to follow that. But we can take any way to complete that flow)
// React JS is a library (Tools are given and we can use to perform something)

// This Express js manages everything from receiving the request and giving the response

const express = require("express");
const app = express();

// # Middleware
app.use(function(req, res, next) {
    console.log("Middleware working")
    next()
});

app.use(function(req, res, next) {
    console.log("Middleware working twice")
    next()
});

//now we can create the routes....... (google.com/route_name)

app.get("/", function (req, res) {
  res.send("Assalawalaikum");
});

app.get("/love", function (req, res) {
  res.send("Mere noor!");
});

app.get("/willYouBe\?", function (req, res,next) {
    return next(new Error("May be not now"))
  });

app.use(function(err, req, res, next){
    console.error(err.stack)
    res.status(500).send('Something is missing')
})

app.listen(3000);

//nodemon is used to have the server restarting on its own
