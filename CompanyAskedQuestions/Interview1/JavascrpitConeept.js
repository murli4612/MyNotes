let nums = [1, 2, 3 ];
// let doubled = nums.map(x => x * 2);
// console.log(doubled); // [2, 4, 6]

// let even = nums.filter(x => x % 2 === 0);
// console.log(even); // [2]

// let sum = nums.reduce((total, current) => total + current, 0);
// console.log(sum); // 6

// let found = nums.find(x => x > 1);
// console.log(found); // 2

// console.log(nums.includes(2)); // true

// let name = "Murli";
// let user = { name }; // same as { name: name }

// let user1 = { name : name }; 
// console.log(user1)

// function double(n) {
//     return new Promise((resolve) => {
//       setTimeout(() => resolve(n * 2), 1000);
//     });
//   }
  
//   double(2)
//     .then(result => {
//       console.log(result,"1+"); // 4
//       return double(result);
//     })
//     .then(result => {
//       console.log(result ,"2+"); // 8
//       return double(result);
//     })
//     .then(result => console.log(result,"3+")); // 16
  


//     Promise.all([
//         double(2),
//         double(4),
//         double(6)
//       ]).then(results => console.log(results ,"all")); // [4, 8, 12]
      
//       Promise.race([
//         double(2),
//         double(4),
//         double(6)
//       ]).then(result => console.log(result,"race")); // likely 4
      


// const user = {
//     name: "Murli",
//     greet: () => {
//       console.log("Hi " + this.name); // ❌ undefined
//     }
//   };
  
//   user.greet();

//   const user1 = {
//     name: "Murli",
//     greet: function () {
//       const inner = () => {
//         console.log("Hi " + this.name); // ✅ uses lexical `this`
//       };
//       inner();
//     }
//   };

//   user1.greet(); // Hi Murli


function introduce(age, city) {
    console.log(`${this.name}, Age: ${age}, City: ${city}`);
  }
  
//   introduce.call({ name: "Murli" }, 30, "Mumbai");

introduce.apply({ name: "Murli" }, [30, "Mumbai"]);


// What kind of security do you think should be in place in terms of api and sdks
  