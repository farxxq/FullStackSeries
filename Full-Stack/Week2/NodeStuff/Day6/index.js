const express = require("express");
const app = express();
const path = require("path");
const fs = require("fs");
const { error } = require("console");

app.set("view engine", "ejs"); //like html but can do calculations
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public"))); // used to access the public folder (the whole path will come here)

app.get("/", function (req, res) {
  fs.readdir(`./files`, function (err, files) {
    console.log(files);
    res.render("index", { files: files });
  });
  console.log("The Files are read from the file folder");
});

app.get("/file/:filename", function (req, res) {
  fs.readFile(
    `./files/${req.params.filename}`,
    "utf-8",
    function (err, filedata) {
      res.render("show", { filename: req.params.filename, filedata: filedata });
    }
  );
  console.log("The files content is visible");
});

app.get("/edit/:filename", function (req, res) {
  res.render("edit", { filename: req.params.filename });
});

app.get("/delete/:filename", function (req, res) {
  res.render("delete", { filename: req.params.filename });
  console.log(req.params.filename)
});

app.post("/create", function (req, res) {
  fs.writeFile(
    `./files/${req.body.title.split(" ").join("")}.txt`,
    req.body.details,
    function (err) {
      // res.send(error)
      res.redirect("/");
    }
  );
});

app.post("/edit", function (req, res) {
  console.log(req.body);
  fs.rename(
    `./files/${req.body.previous}`,
    `./files/${req.body.new}`,
    function (err) {
      res.redirect("/");
    }
  );
});

app.post("/delete", function (req, res) {
    fs.rm(
      `./files/${req.body.filename}`,
      function (err) {
        res.redirect("/");
        console.log("the file is deleted")
      }
    );
    console.log(req.body.filename)
  });

app.get("/sahu", function (req, res) {
  // res.send("Meri jaan");
  res.send(`Welcome, Sahu meri noor`);
  console.log("the route sahu is working");
});

app.listen(3000, function () {
  console.log("The server is running");
});
