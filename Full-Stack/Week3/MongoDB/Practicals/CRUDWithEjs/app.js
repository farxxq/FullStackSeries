const express = require("express");
const app = express();
const path = require("path");
const userModel = require("./models/users");

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {

  // Home page
  res.render("index");
});

app.get("/read", async (req, res) => {

  // to display the users using the read.ejs file
  let allUsers = await userModel.find();
  console.log("The read is initiated")
  res.render("read", {user: allUsers});
});

app.get("/edit/:userid", async (req, res) => {

  //find's one and displays it in edit.ejs file
  let user = await userModel.findOneAndUpdate({});
  res.render("edit", {user});
  console.log("The user:", user.name);
});

app.post("/update/:userid", async (req, res) => {
  let {name,email,image} = req.body;
  // find's one and then updates the value
  let user = await userModel.findOneAndUpdate(
    {_id:  req.params.userid },
    {name, email, image},
    {new: true} // this needs to be true to update
  );
  res.redirect("/read");
  console.log("The updated user:", user)
});

app.get("/delete/:id", async (req, res) => {

  // To delete a particular document
  let deleteUser = await userModel.findOneAndDelete({_id: req.params.id});
  console.log("The read is initiated", deleteUser)
  res.redirect("/read");
});

app.post("/create", async (req, res) => {

  // To create a document
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
