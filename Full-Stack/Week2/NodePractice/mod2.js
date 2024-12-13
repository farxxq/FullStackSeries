// ------url module------
const url = require('url')

const my_url = 'http://localhost:3000/index.htm?year=2020&month=May';
//Parsing the adress:
const que = url.parse(my_url, true);
//The parsing method has created an object that can be accessed using its property names.
console.log("Host: "+ que.host);
console.log("PathName: "+que.pathname);
console.log("Search Query: "+que.search);
console.log("Protocol: "+que.protocol);
console.log("Href: "+que.href);
//You can find about the month inside the query by storing it inside a variable and later accessing its properties.
var que_info = que.query;
console.log("Year: "+ que_info.year);