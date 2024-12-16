const express = require('express');
const app = express();
const userModel = require('./models/users')
const postModel = require('./models/post')

app.get('/', (req,res)=>{
    res.send("Assalamwalaikum");
});


// creating a user in the database
app.get('/create', async (req,res)=>{

    // creating a doc in the user database
    let user = await userModel.create({
        username: "Faroo",
        email: "faroo@mail.com",
        age: 22
    })

    res.send(user)
    console.log(user)
})

// connecting the user and the post model
app.get('/post/create', async (req,res)=>{

    // creating a doc in the post database
    let post = await postModel.create({
        postdata: "Love you!",
        user: "676049b9278976a6d76d76a9", // hard coded (taken from the database for learning purposes)
    })

    // finding the user with the same id
    let user = await userModel.findOne({_id: "676049b9278976a6d76d76a9"});
    // pushing the value of the post ('post' is the variable above) into the userModel's 'post' key
    user.posts.push(post._id);
    // need to manually save this
    await user.save();

    res.send({post, user})
    console.log(post,user)
})

app.listen(3000);