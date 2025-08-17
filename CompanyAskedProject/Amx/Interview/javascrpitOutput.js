// console.log('Start');

// setTimeout(() => {
//   console.log('Timeout (100ms)');
// }, 100);

// new Promise((resolve) => {
//   setTimeout(() => {
//     console.log('Promise Timeout (200ms)');
//     resolve();
//   }, 200);
// }).then(() => {
//   console.log('Promise Resolved');
// });

// console.log('End');







// console.log('Script Start');

// setTimeout(() => {
//   console.log('Timeout 1 (50ms)');
//   Promise.resolve().then(() => console.log('Microtask in Timeout 1'));
// }, 50);

// new Promise((resolve) => {
//   setTimeout(() => {
//     console.log('Promise Timeout (150ms)');
//     resolve('Resolved');
//   }, 150);
// }).then((msg) => {
//   console.log('Promise.then:', msg);
// });

// setTimeout(() => {
//   console.log('Timeout 2 (100ms)');
//   Promise.resolve().then(() => console.log('Microtask in Timeout 2'));
// }, 100);

// console.log('Script End');
// let name = "Murli";
// function outer() {
// //   let name = "Murli";

//   function inner() {
//     console.log("Hello " + name);
//   }

//   inner(); // 👈 Called immediately inside `outer()`
// }

// outer();


// let name = "Murli";

// function outer() {
//   let name = "Dynamic Murli"; // Added a local name
//   inner(); // Call inner from here
// }

// function inner() {
//   console.log("Hello " + name); // Under dynamic scoping, this would use caller's name
// }

// outer(); // What would this output?


// let name ="MMM"
// function createGreeter() {
// //   let name = "Murli"; // Local variable
//   return function() {
//     console.log("Hello " + name); // ← This creates a closure
//   };
// }
// const greet = createGreeter();
// greet(); // "Hello Murli"



// console.log(foo);   // 👉 prints the function body

// var foo = 42;

// function foo() {
//   return "I’m the function!";
// }

// console.log(foo);   // 👉 42


// // ─── 1. outer‑scope variable ───
// var name = "Global Name";

// // ─── 2. object with its own name ───
// const person = {
//   name: "Murli",

//   // (A) regular method: has its own dynamic `this`
//   getNameNormal: function () {
//     return this.name;           // ← `this` resolves to `person`
//   },

//   // (B) arrow “method”: inherits `this` from outer scope
//   getNameArrow: () => {
//     return this.name;           // ← `this` is NOT `person`; it’s `window`
//   }
// };

// // ─── 3. calls ───
// console.log(person.getNameNormal()); // 👉 "Murli"
// console.log(person.getNameArrow());  // 👉 "Global Name" (or undefined in strict‑mode modules)
const person = {
  name: "Bob",
  greet() {
    console.log("Hi, " + this.name);
  }
};

person.greet();  // Output: Hi, Bob
console.log(person,"person")

console.log(Object.keys(person));