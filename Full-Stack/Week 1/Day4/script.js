// Day 4 - JS

/*
###Variables
1. let - works as in blocked scope
->mutable (can be modified later)
eg:
    let a = 10;
    console.log(a);
    a = 15;
    let a = 15; // syntax error as the same variable name can't be declared more then once using the let or var
    console.log(a); //updates the value of a
2. var - works as in global scope
eg:
    var h = 10;
    console.log(h);
    a = 15;
    var h = 15; // no error occurs
    console.log(h);  //updates the value of a

3. const - works in blocked scope
->immutable (cannot be modified later)
eg:
    const a = 10;
    console.log(a);
    a = 15; //immutable so can't be modified

    const a = [1,23,4,5,6];
    console.log(a);
    a.push(6,7,8,9); 
    console.log(a); //const prevents reassignment of the variable itself, but it does not prevent modifications to the data or elements within the object or array.
        
Variables working in Scope explanation:
eg:
function scope(){
    let a = 10;
    let b = 10
        if(a === b){
            console.log("A is equal to B");
            var c = 10;
            var d = 20;
            let e = 30;
            if(d < e){
                console.log(e);
                }
        }
        console.log(c);
        console.log(d);
        console.log(e); //throws an UncaughtReferenceError as variable is declared using the let(blocked scope) and called outside the block.
        }
    
        scope();
    UncaughtReferenceError - when a variable is called without declaration or initialization using the "let" keyword.
        eg:
                console.log(a);
                let a = 10;
    
    when we call the variable before declaring the variable using the "var" keyword we don't get the error but undefined as the output.
        eg:
            console.log(a);
            var a = 10;
                
###Operators:
1. Arithmetic operators:
    a. +
    b. -
    c. *
    d. /
    e. %
2. Logical operators. (boolean output)
    a. AND (&&)
        eg:
            let a = 5;
            let b = 5;
            let c = 10;
            console.log(a &&b &&c);  Output: false (all the values must be same)
            
    b. OR (||)
        eg:
            let a = 5;
            let b = 6;
            let c = 6;
            console.log(a ||b ||c);  Output: true (any one of the value must be same)
    c. NOT (!)
        eg:
            let a = false;
            console.log(!a);   Output: true (gives the opposite of the desired result)
3. Bitwise operators.(mostly not used)
4. Assignment operators:
    a. = 
    b. +=
        Eg:-
            let a = 15;
            a += 15;
    c. *=
    d. -=
    e. /=
    f. %=
    g.Equality operator:
        a. (Loose operators)== - checks the values alone
            eg:
                let a = 5;
                let b = "5";
                console.log (a==b);     Output: true
        b. (strict operators)=== - checls the values and also data types
            eg:
                let a = 5; //integer
                let b = "5"; //String
                console.log (a===b);     Output: false
        c. !=
            eg:
                let a = 5; //integer
                let b = "5"; //String
                console.log (a!=b);     Output: true (gives output in opposite to the actual result)
        d. !== 
            eg:
                let a = 5; //integer
                let b = 5; //integer
                console.log (a!==b);     Output: false (gives output in opposite to the actual result)
                
5. Special operators.
    a. (?:) - short cut of if/else.
    b. , - to allow multiple expressions
    c. delete - deletes a property from object
    d. in - checks if object has the given property
    e. instanceof - checks if the object is an instanceof
    f. new - creates an instance
    g. typeof - checks the type of object
    h. void - descards the expression's return value.
    i. yield - checks what is returned in the generatory
6. Ternary operators.
    a. ?:
        eg:
            let a = 5;
            let b = 6;

            let result = (a>b)? console.log("a is greater than b") : console.log("a is lesser than b");    #Output: a is lesser than b

7. Relational operators. (boolean output)
    a. <
    b. >
    c. <=
    d. >=
    e. !=
    f. ==

### Conditional Statements:
1. if statement
2. else statement.
3. else if statement.
4. switch statement.


### Loops:
1. for loop
    eg:
        for(let i=0; i<10; i++){
            console.log(i," Love you");
        }
2. while loop
    eg:
        let i = 0;
        while(i<10){
            console.log(i," Love you");
            i++;
        }
3. do while loop
    eg:
        let i = 0;
        do{
            console.log(i," Love you")
            i++;
        }while(i<10); //prints 11 times
4. for in loop
    eg:
        let obj = {
            name: "Faroo",
            age: 22
        }

        for (let i in obj){
            console.log(i,obj[i]); //prints the obj
        }
*/

// ### Quick test 1:
console.log("###Quick test 1###");

// Assigning of var
let a = 10;
let b = 20;

// Arithmetic operator
console.log("Addition", a+b);
console.log("Addition", a-b);
console.log("Addition", a*b);
console.log("Addition", a/b);
console.log("Addition", a%b);

// Usage of ternary operator and also comparision operator
let greater = (a>b)? console.log ("A is greater than B") : console.log("A is lesser than B");
let lesser = (a<b)? console.log ("A is Lesser than B") : console.log("B is greater than A");
let notEqual = (a!=b)? console.log ("A is not equal to B") : console.log("A is equal to B");

let c = 10; //for the OR operator

console.log(a&&b);
console.log(a||b||c);
console.log (a!=b!=c);

const e = [1,23,4,5,6];
console.log(e);
e.push(6,7,8,9); // it modifies the constant variable
console.log(e);
console.log(e);


//### Quick test 2:
console.log("###Quick Test 2###");

/*
1. Create a js program that determines the type of triangle based on the lengths of its sides.
The program should have the following:
    a. Declare 3 vars for lenght of triangle.
    b. use nested if-else to check if the triangle is valid(sum of any 2 must be greater than 3rd side)
    c. use if-else-if statement to determine the type of the triangle.
    d. Equilateral: All three sides are equal.
    e. Isosceles: 2 sides are equal.
*/





/*
2. Pattern of stars in the shape of pyramid.Display the pyramid on the web page.
    a. nested loops to generate pyramid.
    b. while loop to calc and log the total number of stars used in the pyramid.
*/
