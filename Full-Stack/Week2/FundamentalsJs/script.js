// Fundamentals of JS
// arrays and objects
// functions return
// async js
// forEach map filter find indexOf

var arr = [1, 2, 28, 7, 2004, 2003];
// # forEach:
arr.forEach(function (val) {
  console.log("<Love/> elems in array:" + val);
});

// # map:
var map = arr.map(function (val) {
  return val + 1;
});
console.log("The updated array using map: " + map);

// # filter
var filter = arr.filter(function (val) {
  if (val > 1000) return true;
});
console.log("The array using the filter: " + filter);

// # find
var find = arr.find(function (val) {
  if (val <= 100) return val;
});

console.log(
  "This is used to find the first elem that aligns with the condition: " + find
);

// # indexOf
var indexOf = arr.indexOf(5); //gives -1 as there is no 5th index in the arr
console.log("To find the elem index in the arr: " + indexOf);
var indexOf = arr.indexOf(2); //gives 1 as there is 2nd index in the arr
console.log("To find the elem index in the arr: " + indexOf);

// # objects - (key,value pairs)
var obj = {
  name: "Sah",
  age: 21,
} 

//to access the keys in the object
console.log(obj.name)
console.log(obj['name'])

//change the objects

obj.age = 22
console.log(obj.age + " Value changed")

//To not change the objects
Object.freeze(obj)
obj.age = 21 //won't update
console.log(obj.age + " Value can't be changed as it is freezed")

// # return

function hello(){
    return 12
}


console.log("Called using the function and learning return: "+ hello())

// # Async JS
async function sah() {
    var blob = await fetch(`https://randomuser.me/api/`)
    var ans = blob.json()
    return ans
}

console.log(sah())