const express = require("express");
const app = express();
const bcrypt = require("bcrypt"); // Importing the bcrypt (For hashing)
const jwt = require("jsonwebtoken");
const userModel = require("./models/user"); // Importing the data base
const postModel = require("./models/post"); // Importing the data base
const cookieParser = require("cookie-parser"); // Importing the cookie parser to read the data from the cookie in the console

app.set("view engine", "ejs"); // Setting up the ejs
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser()); // To print cookie value in console

app.get("/", (req, res) => {
  // res.send("Assalamwalaikum");
  res.render("index");
});

app.get("/login", (req, res) => {
  // res.send("Assalamwalaikum login ke liye hei");
  res.render("login");
});

app.get("/logout", (req, res) => {
    // res.send("Assalamwalaikum login ke liye hei");
    res.cookie("token", "");
    res.redirect('/login')
  });

app.get("/profile", isLoggedIn, (req, res) => {
  console.log(req.user);
  res.send("Profile");
});

app.post("/register", async (req, res) => {
  let { email, password, username, name, age } = req.body;
  let user = await userModel.findOne({ email });
  if (user) return res.status(500).send("User already registered");

  bcrypt.genSalt(10, (err, salt) => {
    bcrypt.hash(password, salt, async (err, hash) => {
      userModel.create({
        username,
        name,
        email,
        age,
        password: hash,
      });

      let token = jwt.sign({ email: email }, "love");
      res.cookie("token", token);
      console.log(token);
      res.send("Registered");
    });
  });
});

app.post("/login", async (req, res) => {
  let { email, password } = req.body;

  let user = await userModel.findOne({ email });
  if (!user) return res.status(500).send("Something went wrong");

  bcrypt.compare(password, user.password, (err, result) => {
    if (result) {
      console.log(result);
      let token = jwt.sign({ email: email }, "love");
      res.cookie("token", token);
      console.log(token);
      res.status(200).send("You can login");
    } else {
      res.redirect("/login");
      console.log("wrong password");
    }
  });
});

function isLoggedIn(req, res, next) {
  if (req.cookies.token === "") res.send("You need to be loggedIn");
  else {
    let data = jwt.verify(req.cookies.token, "love");
    req.user = data;
  }
  next();
}

app.listen(3000);
