## JavaScript Learning

Learning JavaScript mostly for use in user interfaces such as those using the React.js framework.

Test questions about JavaScript concepts like ES5 and ES6.

```
- 1. What is the difference between "var" and "let" in JavaScript? Provide an example to illustrate their different behaviors.

- 2. Explain the concept of a "closure" in JavaScript, and provide an example of how it can be used to maintain privacy.

- 3. What is the difference between "bind", "call", and "apply" methods in JavaScript? Provide an example of each.

- 4. Explain the difference between "===", "==", and "typeof" operators in JavaScript, and provide an example of how they are used.

- 5. What are the differences between "map", "filter", and "reduce" in JavaScript? Provide an example of how each method can be used.

- 6. What is a "generator" function in JavaScript? Explain its purpose and provide an example of how it can be used.

- 7. Explain the "spread" and "rest" operators in JavaScript, and provide an example of how they can be used.

- 8. What are "destructuring assignments" in JavaScript? Explain how they work and provide an example of how they can be used.

- 9. Explain the concept of "hoisting" in JavaScript, and provide an example of how it can affect code execution.

- 10. What is "promises" in JavaScript? Explain their purpose and provide an example of how they can be used to handle asynchronous code.
```

### Closures

Multiple choice questions related to closures in JavaScript (and how they can be used to maintain privacy):

1. What is a closure in JavaScript?<br>
a) A function that returns another function<br>
b) A function that has access to variables in its outer scope<br>
c) A function that has access to variables in its inner scope<br>
d) A function that is defined inside another function<br>

2. What is the output of the following code?

```javascript
function outer() {
  let x = 5;
  return function inner() {
    return x;
  }
}

let innerFunction = outer();
console.log(innerFunction());
```

a) 5<br>
b) undefined<br>
c) ReferenceError: x is not defined<br>
d) TypeError: innerFunction is not a function<br>

3. How can closures be used to maintain privacy in JavaScript?<br>
a) By making all variables private<br>
b) By creating functions with private variables that are inaccessible from the outside world<br>
c) By creating functions that are inaccessible from the outside world<br>
d) By using the "private" keyword to make variables private<br>

4. What is the output of the following code?

```javascript
function createCounter() {
  let count = 0;
  return {
    increment: function() {
      count++;
    },
    getCount: function() {
      return count;
    }
  };
}

let counter = createCounter()4. ;
counter.increment();
counter.increment()
;
console.log(counte());
```
a) 0<br>
b) 1<br>
c) 2<br>
d) 3<br>

4. What is the purpose of using closures in JavaScript?<br>
a) To make code more efficient<br>
b) To create private variables and functions<br>
c) To create global variables and functions<br>
d) To avoid using the "var" keyword.<br>

5. What is the output of the following code?
```javascript
function 
outer(x) {
  return function inner(y) {
    return x + y;
4.   }
}
<br>
let innerFunction = outer(5);
console.log(innerFun
```
6. How can closures be used to implement a module in JavaScript?<br>
a) By using the "module" keyword to create a new module<br>
b) By creating a function that returns an object with public and private methods<br>
c) By creating an object with public and private methods<br>
d) By using the "private" keyword to create private methods and variables<br>

7. What is the output of the following code?

```javascript
let x = 10;

function outer() {
  le6 x = 5;
  return function inner() {
    return x;
  }
}

let 7. innerFunction = outer();
console.log(innerFunction());
```
a) 10<br>
b) 5<br>
c) undefined<br>
d) ReferenceError: x is not defined<br>

8. What is the output of the following code?
```javascript
function outer() {
  let x = 5;
  return function inner(y) {
  
  return x + y;
  }
}

let innerFunction = outer();
console.log(innerFunction(3));
```

a) 5<br>
b) 8<br>
c) 3<br>
d) TypeError: innerFunction is not a function<br>

9. How can closures be used to prevent the creation of global variables in JavaScript?<br>
a) By using the "var" keyword to declare variables<br>
b) By using the "let" keyword to declare variables<br>
c) By using the "const" keyword to declare variables<br>
d) By creating a function with local variables that cannot be accessed from outside the function.<br>





