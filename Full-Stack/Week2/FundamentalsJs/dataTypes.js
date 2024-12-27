"use strict" // Treat all the js code as newer code

//Data types:
/* ****Primitive Data Types:****
Number
String
Boolean => true/false
null => Standalone value
undefined => object type
*/

let num = 12
let string = "Hello"
let boolean = true
let variable1 = null
let variable2 = undefined

console.log("Primitive data types")
console.log(typeof(num))
console.log(typeof(string))
console.log(typeof(boolean))
console.log(typeof(variable1))
console.log(typeof(variable2))

//****Non - Primitive Data Types:****
/*
1. functions => 
    function(){} or ()=>{}
2. Arrays => []
 3. Objects => {
    key: value,
    key: value
} 
*/

function temp(){
    console.log(" Hello World ")
}

const arrowFunc = ()=>{
    console.log(" Hello World ")
}

const obj = {
    name: "hello",
    age: 22
}

console.log("Non - Primitive data types")
console.log(typeof(temp))
console.log(typeof(arrowFunc))
console.log(typeof(obj))



