// //Node.js Basics
// // Intro to Node.js
// // working Node.js and npm
// // workding with modules
// // File systems operations
// // Understanding HTTP module

// // Node js is not a programming lang,framework or library
// // This is a js runtime enviroment
// // it is a wrapper around the V8 engine (Chrome engine)

// //npm init (type in terminal to create a package.json file (This contains all our priorities))

// // # modules -
// const fs = require('fs');

// // # writefile
// // Syntax fs.writeFile(file,data[,options],callback)

// fs.writeFile("Sfaroo.txt", "Assalamwalaikum Faroo",function(err){
//     if(err) console.log(err);
//     else console.log("done writeFile")
// })

// // # appendFile
// fs.appendFile("Sfaroo.txt","\nKaise ho?",function(err) {
//     if(err) console.log(err);
//     else console.log("done appendFile")
// })

// // # rename
// fs.rename("Sfaroo.txt","SFaroo.txt",function(err){
//     if(err) console.log(err)
//     else console.log("done rename")
// })

// // # copyFile
// fs.copyFile("Sfaroo.txt","copySFaroo.txt",function (err) {
//     if(err) console.log(err)
//     else console.log("Done copyFile")
// })

// // # unlink
// fs.unlink("Faroo.txt",function(err) {
//     if(err) console.log(err)
//         else console.log("Done unlink(removed)")
// })

// // # rmdir
// fs.rmdir("folder(toRemove)/tempFiles/tempFiles(studies)",{recursive:true},function(err) {
//     if(err) console.log(err.message)
//     else console.log("Done rmdir(removeDir)")
// })

// // # rm
// fs.rm("folder(toRemove)/tempFiles/tempFiles(studies)",function(err){
//     if(err) console.log(err.message)
//     else console.log("Done rm(removeDir even if it contains files)")
// })


// # http 

const http = require('http')

const server = http.createServer(function(req,res){
    res.end("Hello world")
})

server.listen(3000)