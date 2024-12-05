const express = require("express");
const app = express();
const path = require("path");
const fs = require("fs");

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  fs.readdir(`./files`, (err, files) => {
    res.render("index", { files: files });
  });
});

app.get("/files/:file", (req, res) => {
  fs.readFile(`./files/${req.params.file}`, 
    "utf-8", 
    (err, content) => {
    res.render("read", { file: req.params.file, data: content });
  });
  console.log(req.params.file)
});

app.get('/delete', (req,res)=>{
  const fileName = req.query.file;
  res.render("delete", {file : fileName})
  console.log("delete ejs file active")
})

app.post('/delete/:file', (req,res)=>{
  fs.rm(`./files/${req.params.file}`,(err)=>{
    res.redirect('/')
    console.log("File deleted:",req.params.file)
  })
})


app.post("/create", (req, res) => {
  console.log(req.body);
  fs.writeFile(
    `./files/${req.body.fileName.split(" ").join("")}.txt`,
    req.body.content,
    (err) => {
      res.redirect("/");
    }
  );
  console.log("Created file for id:", req.body.fileName);
});

app.listen(3000);
