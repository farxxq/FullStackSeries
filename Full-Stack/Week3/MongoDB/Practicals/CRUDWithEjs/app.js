const express = require("express");
const app = express();
const path = require("path");
const userModel = require("./models/users");

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.render("index");
});

app.get("/read", async (req, res) => {
  let allUsers = await userModel.find();
  console.log("The read is initiated", allUsers)
  res.render("read", {user: allUsers});
});

app.post("/create", async (req, res) => {
  let { name, email, image } = req.body;
  let createdUser = await userModel.create({
    name,
    email,
    image,
  });
  res.redirect("read");
  console.log(createdUser, "the user is created")
});

app.listen(3000);
