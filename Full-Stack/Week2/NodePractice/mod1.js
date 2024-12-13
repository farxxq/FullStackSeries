// -------- http ---------
// Importing the http server from the node modules
const http = require("http");
// Importing the eventEmitter from the node modules
const EventEmitter = require("events");
const myEmitter = new EventEmitter();
// url module
const url = require('url');

// // To create a http server using the node:
// const server = http.createServer((req,res)=>{
//     res.end("Assalamwalaikum") // Sends the response to the via server
// });

// // Using different types of logs:
// const server = http.createServer((req,res)=>{
//     res.end("Assalamwalaikum"); // Sends the response to the via server
//     console.log("Server is running") // Prints the output in the console
//     console.error("Error occured") // Prints if some error occurs in red line
//     console.warn("This is a warning") // Prints the message in yellow indicating a warning
//     console.table(users) // Prints the output in a table format
// });

// const users = [
//     {name: "Farooq", age: 22},
//     {name: "Faroo", age: 21}

// ]
// This listens the server response
// server.listen(3000);

// ----- Event Emitter --------
// // First listener
// myEmitter.on("event", function firstListener() {
//   console.log("Helloooo! first listener");
// });
// // Second listener
// myEmitter.on("event", function secondListener(arg1, arg2) {
//   console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
// });
// // Third listener
// myEmitter.on("event", function thirdListener(...args) {
//   const parameters = args.join(", ");
//   console.log(`event with parameters ${parameters} in third listener`);
// });

// myEmitter.emit("event", 1, 2, 3, 4, 5);

// // Counts the events
// console.log("This is the number of events active:",myEmitter.listenerCount("event"))
// // Lists the events
// console.log("This is the list of events active:",myEmitter.listeners("event"))

// ----File system----
// const fs = require('fs')

// fs.writeFile('Temp.txt', "This is the temp file made for studying",()=>{
//     console.log("Created a file")
// })

// fs.readFile("Temp.txt", "utf-8" ,(err,data)=>{
//     if(err) throw err;
//     console.log("The file is read and the info is:", data);
// })



