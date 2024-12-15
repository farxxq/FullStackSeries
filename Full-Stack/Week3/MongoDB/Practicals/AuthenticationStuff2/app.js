const express = require("express");
const app = express();
const userModel = require("./models/userModel");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const cookieParser = require("cookie-parser");
const path = require("path");

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.render("index");
});

app.post("/create", async (req, res) => {
  let { username, email, password, age } = req.body;
  bcrypt.genSalt(10, (err, salt) => {
    bcrypt.hash(password, salt, async (err, hash) => {
      await userModel.create({
        username,
        email,
        password: hash,
        age,
      });
    });
  });
  let token = jwt.sign({ email }, "love"); //creates a token to be saved on the browser as cookie
  res.cookie("token", token);
  console.log(token);
  res.send("The user is created");
});

app.get("/login", (req, res) => {
  res.render("login");
});

app.post("/login", async (req, res) => {
  let user = await userModel.findOne({ email: req.body.email });
  console.log(user);
  if (!user) return res.send("Something went wrong");

  bcrypt.compare(req.body.password, user.password, (err, result) => {
    if (!result) {
      let token = jwt.sign({ email: user.email }, "love"); //creates a token to be saved on the browser as cookie
      res.cookie("token", token);
      console.log(token);
      res.send("User Authorized");
    } else {
      res.send("Something is wrongp");
    }
  });
});

app.get("/logout", (req, res) => {
  res.cookie("token", ""); // Emptied the token value
  res.redirect("/");
});

app.listen(3000);
