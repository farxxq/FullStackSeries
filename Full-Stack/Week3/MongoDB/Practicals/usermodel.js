const mongoose = require('mongoose')

mongoose.connect(`mongodb://127.0.0.1:2707/mongoLove`)

const userSchema = mongoose.Schema({
    name: String,
    username: String,
    email: String
})

module.exports = mongoose.model('user',userSchema)