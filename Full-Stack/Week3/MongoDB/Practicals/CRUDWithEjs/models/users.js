const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/mongoStudy");

const userSchema = mongoose.Schema({
  image: String,
  email: String,
  name: String,
});

module.exports = mongoose.model("user", userSchema);
