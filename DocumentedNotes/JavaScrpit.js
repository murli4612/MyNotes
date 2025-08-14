Event-Driven Programming in JavaScript
Event-driven programming is a programming paradigm where the flow of execution is determined by events such as 
user actions (clicks, keystrokes), sensor outputs, or messages from other programs.

How Event-Driven Programming Works in JavaScript?
JavaScript uses an event loop to handle asynchronous operations efficiently. The core components of event-driven programming in JavaScript are:

Event Listeners – Functions that wait for an event to occur.
Event Handlers – Functions that execute when an event is triggered.
Event Queue & Event Loop – Manages and processes events asynchronously.


1. Event Listeners in JavaScript
Event listeners wait for an event to occur and trigger a callback function.

Example:

document.getElementById("btn").addEventListener("click", function() {
    alert("Button clicked!");
});


✅ The "click" event is listened to and the function executes when the button is clicked.


2. Event Bubbling & Capturing (Event Propagation)
When an event occurs, it propagates through the DOM tree in two phases:

Capturing Phase: Event travels from the root to the target element.
Bubbling Phase: Event bubbles up from the target element to the root.

2. Event Bubbling & Capturing (Event Propagation)
When an event occurs, it propagates through the DOM tree in two phases:

Capturing Phase: Event travels from the root to the target element.
Bubbling Phase: Event bubbles up from the target element to the root.

✅ Setting the third parameter to true makes the listener fire during capturing.

3. Asynchronous Event Handling & Event Loop
JavaScript uses the event loop to handle asynchronous events.

setTimeout(), setInterval() – Delayed execution.
Promises & Async/Await – Handle asynchronous code.
Web APIs (like fetch()) – Non-blocking requests.

console.log("Start");

setTimeout(() => {
    console.log("Inside setTimeout");
}, 0);

console.log("End");

✅ Output:
Start  
End  
Inside setTimeout  

✅ Even though setTimeout has 0ms, it executes after synchronous code due to the event loop.

4. Custom Events in JavaScript
JavaScript allows creating and dispatching custom events.

Example

const event = new Event("customEvent");

document.addEventListener("customEvent", () => {
    console.log("Custom event triggered!");
});

document.dispatchEvent(event);

✅ The "customEvent" is manually triggered using dispatchEvent().

5. Real-Life Use Cases of Event-Driven JavaScript
Handling User Interactions (Clicks, Keypress, Hover, etc.)
Processing Server Responses (AJAX, WebSockets, APIs)
Game Development (Handling Player Inputs, Physics Updates)
Real-Time Applications (Chat Apps, Stock Market Feeds)


Conclusion
✅ JavaScript is event-driven by design, meaning most actions trigger events.
✅ Event listeners handle user interactions dynamically.
✅ Event loop ensures non-blocking execution.
✅ Custom events allow defining application-specific triggers.


Deep Copy vs. Shallow Copy in JavaScript
When copying objects in JavaScript, there are two types of copies:

Shallow Copy – Copies references for nested objects.
Deep Copy – Recursively creates new copies of all nested objects.


1. Shallow Copy
A shallow copy creates a new object, but nested objects (objects inside objects) are still referenced (not copied).


Example of Shallow Copy

let obj1 = { name: "Alice", address: { city: "New York" } };
let obj2 = { ...obj1 };  // Shallow copy using spread operator

obj2.name = "Bob";  // Changes only obj2's name
obj2.address.city = "Los Angeles";  // Also modifies obj1.address.city

console.log(obj1); // { name: "Alice", address: { city: "Los Angeles" } }
console.log(obj2); // { name: "Bob", address: { city: "Los Angeles" } }

✅ Issue: The address object is shared between obj1 and obj2, so modifying one affects the other.

Ways to Create a Shallow Copy

Method	Example
Object.assign()	let obj2 = Object.assign({}, obj1);
Spread Operator	let obj2 = { ...obj1 };
✅ Works well only if there are no nested objects.


2. Deep Copy
A deep copy recursively copies all properties, including nested objects, so changes in the copied object don’t affect the original.

Example of Deep Copy

let obj1 = { name: "Alice", address: { city: "New York" } };

// Deep copy using JSON methods
let obj2 = JSON.parse(JSON.stringify(obj1));

obj2.address.city = "Los Angeles";  // Changes only obj2

console.log(obj1); // { name: "Alice", address: { city: "New York" } }
console.log(obj2); // { name: "Alice", address: { city: "Los Angeles" } }


✅ No shared references!
Ways to Create a Deep Copy

Method	                                          Example	                                                   Pros          	Cons
JSON.parse(JSON.stringify(obj))	        let deepCopy = JSON.parse(JSON.stringify(obj));                  	Simple, fast	Loses functions & special objects (e.g., Date, RegExp)
Lodash _.cloneDeep()	                   let deepCopy = _.cloneDeep(obj);                  	Best for complex objects	Requires Lodash library
Manual Recursion	                          (See below)	                                          Full control	        Complex, slow


function deepCopy(obj) {
    if (typeof obj !== "object" || obj === null) {
        return obj; // Return primitive values as is
    }

    let copy = Array.isArray(obj) ? [] : {}; // Create array or object

    for (let key in obj) {
        copy[key] = deepCopy(obj[key]); // Recursively copy
    }

    return copy;
}

let obj1 = { name: "Alice", address: { city: "New York" } };
let obj2 = deepCopy(obj1);
obj2.address.city = "Los Angeles";

console.log(obj1.address.city); // "New York"
console.log(obj2.address.city); // "Los Angeles"


✅ Handles nested objects & arrays without external libraries.

Key Differences Between Shallow Copy & Deep Copy

Feature	Shallow Copy	Deep Copy
Copy Level	Only top-level properties	Copies entire object recursively
Nested Objects	Shared references	Independent copies
Performance	Fast	Slower (recursive copying)
Methods	Object.assign(), Spread { ...obj }	JSON.parse(JSON.stringify()), Recursion, Lodash _.cloneDeep()

When to Use Which?
✔ Use shallow copy if the object has only primitive values (no nested structures).
✔ Use deep copy if the object contains nested objects/arrays to avoid unintended mutations.


The Event Loop in JavaScript is a fundamental concept that enables asynchronous programming. 
It ensures that JavaScript remains non-blocking, allowing it to handle multiple operations efficiently.

How the Event Loop Works
JavaScript has a single-threaded execution model, meaning it can execute only one task at a time in the Call Stack. However, 
it can manage asynchronous operations like fetching data, timers, and user interactions using the Event Loop.

Main Components of the Event Loop
Call Stack

This is where synchronous code gets executed.
Functions are pushed onto the stack when called and popped when they return.
Web APIs (or Node APIs)

Asynchronous functions like setTimeout, fetch, and DOM events are handled by the browser's Web APIs.
Callback Queue (Task Queue & Microtask Queue)

The Task Queue (Macro-task queue) contains callbacks from setTimeout, setInterval, setImmediate (Node.js), and I/O.
The Microtask Queue contains promises (.then, async/await) and process.nextTick (Node.js).
Event Loop

The Event Loop continuously checks if the Call Stack is empty.
If empty, it first processes the Microtask Queue, then moves to the Task Queue.
Execution Order of Tasks
The Call Stack executes all synchronous code.
If an asynchronous operation occurs (like setTimeout), it is handled by the Web APIs.
Once the asynchronous operation completes, its callback is pushed into the appropriate queue.
The Event Loop first checks the Microtask Queue and executes all microtasks before moving to the Task Queue.
The Event Loop repeats this process.
Example


console.log("Start");

setTimeout(() => {
  console.log("setTimeout Callback");
}, 0);

Promise.resolve().then(() => {
  console.log("Promise Callback");
});

console.log("End");



Execution Order
"Start" → Call Stack → Printed
setTimeout → Moved to Web APIs
Promise.resolve().then(...) → Moved to Microtask Queue
"End" → Call Stack → Printed
Microtasks (Promise Callback) execute → Printed
Task Queue (setTimeout Callback) executes → Printed

out:
Start
End
Promise Callback
setTimeout Callback

Key Takeaways
The Event Loop ensures JavaScript remains non-blocking.
Microtasks (Promises, process.nextTick) execute before Macrotasks (setTimeout, I/O).
The Call Stack executes synchronous code first before handling asynchronous operations.


How Promise Handles Asynchronous Operations in JavaScript
A Promise in JavaScript is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

States of a Promise
A Promise has three possible states:

Pending – The initial state, before the operation completes.
Fulfilled (Resolved) – The operation completed successfully.
Rejected – The operation failed.

Creating a Promise
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    let success = true; // Simulating success/failure
    if (success) {
      resolve("Operation Successful!");
    } else {
      reject("Operation Failed!");
    }
  }, 2000);
});


Handling Promises
1. .then() and .catch()

myPromise
  .then((result) => {
    console.log("Success:", result);
  })
  .catch((error) => {
    console.error("Error:", error);
  })
  .finally(() => {
    console.log("Promise Completed");
  });

Execution Flow
If resolved → .then() executes.
If rejected → .catch() executes.
.finally() executes regardless of success or failure.


2. Using async/await
async function handlePromise() {
  try {
    let result = await myPromise;
    console.log("Success:", result);
  } catch (error) {
    console.error("Error:", error);
  } finally {
    console.log("Promise Completed");
  }
}

handlePromise();

How async/await Works
await pauses the function execution until the Promise resolves.
If rejected, the control moves to the catch block


Chaining Promises
If multiple asynchronous tasks depend on each other:

If multiple asynchronous tasks depend on each other:

function firstTask() {
  return new Promise((resolve) => {
    setTimeout(() => resolve("First Task Done"), 1000);
  });
}

function secondTask(prevResult) {
  return new Promise((resolve) => {
    setTimeout(() => resolve(prevResult + " → Second Task Done"), 1000);
  });
}

firstTask()
  .then(secondTask)
  .then((finalResult) => console.log(finalResult));

output:

First Task Done → Second Task Done

Error Handling in Promises
If a .catch() is missing, an unhandled rejection occurs:

new Promise((_, reject) => reject("Error occurred!"))
  .then((data) => console.log("Data:", data)); // No .catch() → Unhandled Rejection

👉 Best practice: Always handle errors using .catch() or try...catch.

Would you like a deeper explanation or a real-world example? 🚀


💡 Problem: Since there's no .catch(), the rejection is not handled, which might crash the application.

🔹 Best Practices for Error Handling
✅ 1. Using .catch() to Handle Errors


new Promise((_, reject) => reject("Something went wrong!"))
  .then((data) => console.log("Data:", data))
  .catch((error) => console.error("Caught Error:", error));

✅ The .catch() method captures and handles the error, preventing an unhandled rejection.


✅ 2. Using try...catch with async/await
When working with async/await, we use try...catch for proper error handling.

const fetchData = async () => {
  try {
    let response = await fetch("https://api.example.com/data"); // Example API
    let data = await response.json();
    console.log("Data:", data);
  } catch (error) {
    console.error("Fetch Error:", error);
  }
};

fetchData();

✅ Advantages:

Easier to read than .then().catch()
More structured error handling inside try...catch

✅ 3. Using .catch() Globally
If an unhandled rejection occurs, you can use:
process.on("unhandledRejection", (error) => {
  console.error("Unhandled Rejection Detected:", error);
});

💡 Useful in Node.js applications to prevent app crashes due to unhandled promise rejections.


🔹 Real-World Example
Imagine an API call that fails due to network issues:

const fetchUser = async (userId) => {
  try {
    let response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    let data = await response.json();
    console.log("User Data:", data);
  } catch (error) {
    console.error("Error fetching user:", error);
  }
};

// Call function with an invalid user ID
fetchUser(99999); // Likely to fail


✅ Here, we:

Check if the response is OK (response.ok)
Throw a custom error if not
Catch the error and log it properly

🔹 Summary
🔹 Always handle errors using .catch() or try...catch
🔹 Use .catch() for standard Promises and try...catch for async/await
🔹 Handle unhandled rejections in Node.js using process.on("unhandledRejection")
🔹 Check API response status (response.ok) before parsing JSON


🔹 Retrying Failed Promises in JavaScript 🚀
When dealing with unreliable APIs or flaky network connections, we may need to retry failed requests before giving up.
 Let's explore different strategies to retry failed Promises efficiently.
 
 ✅ 1. Simple Retry Mechanism (Recursive Approach)
We retry the request a fixed number of times before throwing an error.


const fetchWithRetry = async (url, retries = 3, delay = 1000) => {
  try {
    let response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }

    return await response.json(); // Return data if successful
  } catch (error) {
    if (retries > 0) {
      console.warn(`Retrying... Attempts left: ${retries}`);
      await new Promise(res => setTimeout(res, delay)); // Wait before retrying
      return fetchWithRetry(url, retries - 1, delay);  // Recursive call
    }
    throw error; // No retries left, throw error
  }
};

// Example usage
fetchWithRetry("https://jsonplaceholder.typicode.com/posts/1")
  .then(data => console.log("Fetched Data:", data))
  .catch(err => console.error("Final Error:", err));


✅ How it works?

Fetches the data from the API.
If an error occurs, it waits (setTimeout) before retrying.
Retries up to retries times before throwing an error.
💡 Use Case: Useful when API servers are temporarily down.


✅ 2. Using Exponential Backoff (Smarter Retry Strategy)
Instead of retrying with a fixed delay, we use an exponential backoff strategy (increase delay exponentially).
const fetchWithExponentialBackoff = async (url, retries = 3, delay = 1000) => {
  try {
    let response = await fetch(url);
    
    if (!response.ok) {
      throw new Error(`HTTP Error! Status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    if (retries > 0) {
      let nextDelay = delay * 2; // Double the delay each retry
      console.warn(`Retrying in ${nextDelay}ms... Attempts left: ${retries}`);
      await new Promise(res => setTimeout(res, nextDelay));
      return fetchWithExponentialBackoff(url, retries - 1, nextDelay);
    }
    throw error;
  }
};

// Example usage
fetchWithExponentialBackoff("https://jsonplaceholder.typicode.com/posts/1")
  .then(data => console.log("Fetched Data:", data))
  .catch(err => console.error("Final Error:", err));



✅ How it works?

The delay doubles after each failed attempt (1000ms → 2000ms → 4000ms).
It reduces the load on the API by preventing frequent retries.
💡 Use Case: Helps prevent API throttling when rate limits exist.



✅ 3. Retrying Using Third-Party Libraries (axios-retry)
Instead of writing our own retry logic, we can use axios-retry, which provides built-in retry handling.

🔹 Step 1: Install axios-retry

npm install axios axios-retry

🔹 Step 2: Use axios-retry

import axios from "axios";
import axiosRetry from "axios-retry";

// Configure retry mechanism
axiosRetry(axios, {
  retries: 3, // Number of retries
  retryDelay: (retryCount) => retryCount * 1000, // 1s, 2s, 3s...
  retryCondition: (error) => error.response?.status >= 500, // Only retry on 5xx errors
});

const fetchData = async () => {
  try {
    const response = await axios.get("https://jsonplaceholder.typicode.com/posts/1");
    console.log("Fetched Data:", response.data);
  } catch (error) {
    console.error("Final Error:", error);
  }
};

fetchData();


✅ How it works?

Automatically retries requests up to 3 times.
Uses increasing delays between retries (1s → 2s → 3s).
Only retries if the error is server-related (5xx status codes).
💡 Use Case: Works well for APIs with built-in rate limits.

🔹 Summary: Which Strategy to Use?
Strategy	Best For	Pros	Cons
🔹 Simple Retry	Temporary failures	Easy to implement	Fixed delay
🔹 Exponential Backoff	API Rate Limits, Network issues	Reduces load, smart retries	Longer wait time
🔹 axios-retry	Handling API calls	Automatic retry, easy setup	Requires axios


Handling Rate-Limited APIs (Twitter API Example) 🚀
Many APIs, like Twitter, GitHub, and OpenAI, enforce rate limits to prevent abuse. If too many requests are sent within a short time, the API responds with HTTP 429 (Too Many Requests) or rate-limit headers.

✅ 1. Understanding Rate Limits
HTTP 429 Response → API rejects requests when limits are exceeded.
Rate Limit Headers → Some APIs return headers like:
X-RateLimit-Limit (Max allowed requests)
X-RateLimit-Remaining (Requests left before limit resets)
X-RateLimit-Reset (Time when limit resets)
Example: GitHub API returns:

HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1672540800

✅ 2. Implementing Rate-Limit Handling (Twitter API Example)
We'll use axios to handle retries only when a rate limit occurs (429 error).

🔹 Step 1: Install Required Libraries

npm install axios axios-retry

🔹 Step 2: Implement API Handling with Exponential Backoff
import axios from "axios";
import axiosRetry from "axios-retry";

// Configure axios-retry
axiosRetry(axios, {
  retries: 5, // Max retries
  retryDelay: (retryCount, error) => {
    // If the error is a 429 (rate limit), wait for the reset time
    if (error.response?.status === 429) {
      const retryAfter = error.response.headers["retry-after"] || 2; // Default: 2s
      console.warn(`Rate limit hit! Retrying after ${retryAfter} seconds...`);
      return retryAfter * 1000;
    }
    // Exponential backoff (2s, 4s, 8s...)
    return Math.pow(2, retryCount) * 1000;
  },
  retryCondition: (error) => {
    return error.response?.status === 429 || error.response?.status >= 500;
  },
});

// Function to fetch Twitter data
const fetchTwitterData = async () => {
  try {
    const response = await axios.get("https://api.twitter.com/2/tweets?ids=1453489038376132611", {
      headers: { Authorization: `Bearer YOUR_ACCESS_TOKEN` },
    });
    console.log("Fetched Data:", response.data);
  } catch (error) {
    console.error("Final Error:", error.message);
  }
};

// Call function
fetchTwitterData();

✅ 3. How This Works?
If an API request hits the rate limit (429 Too Many Requests), the script reads the "retry-after" header and waits before retrying.
If no "retry-after" header is present, exponential backoff (2s → 4s → 8s → ...) is used.
Retries up to 5 times before throwing an error.

✅ 4. Alternative: Using p-retry (More Control)
If you need more custom control over retries, use the p-retry library.

🔹 Install p-retry
npm install p-retry


🔹 Implement with p-retry
import axios from "axios";
import pRetry from "p-retry";

const fetchTwitterData = async () => {
  return axios.get("https://api.twitter.com/2/tweets?ids=1453489038376132611", {
    headers: { Authorization: `Bearer YOUR_ACCESS_TOKEN` },
  });
};

const runWithRetry = async () => {
  try {
    const response = await pRetry(fetchTwitterData, {
      retries: 5,
      onFailedAttempt: (error) => {
        console.warn(`Attempt ${error.attemptNumber} failed. Retrying in ${error.retriesLeft} tries...`);
      },
    });
    console.log("Fetched Data:", response.data);
  } catch (error) {
    console.error("Final Error:", error.message);
  }
};

runWithRetry();

✅ 5. Summary: Best Strategies
Method	Best For	Pros	Cons
🔹 Axios Retry	Basic API handling	Simple, easy to use	Limited flexibility
🔹 Custom Retry Logic	Exponential backoff	Fine-tuned retries	More code needed
🔹 p-retry	More control over retries	Handles errors gracefully	Requires p-retry package


🔐 Secure API Key Handling & Distributed Rate Limiting with Redis in Django
When working with APIs in Django, securing API keys and implementing rate limits efficiently is crucial. Here's how to do both using Django Rest Framework (DRF) and Redis.

✅ 1. Secure API Key Handling in Django

Never expose API keys directly in your Django code. Instead, store them securely in environment variables or Django settings.

🔹 Step 1: Store API Keys in .env
First, install django-environ to manage environment variables.

pip install django-environ

Create a .env file in your project root:
TWITTER_API_KEY=your_secret_key

🔹 Step 2: Load .env in settings.py
Modify settings.py:

import environ
import os

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

TWITTER_API_KEY = env("TWITTER_API_KEY")

🔹 Step 3: Use API Key Securely in Django Views
Instead of exposing the API key in the frontend, call it from Django:

import requests
from django.http import JsonResponse
from django.conf import settings

def fetch_twitter_data(request):
    url = "https://api.twitter.com/2/tweets"
    headers = {"Authorization": f"Bearer {settings.TWITTER_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to fetch data"}, status=500)



🔹 Step 4: Call API Securely in Frontend
Now, instead of calling the Twitter API directly, the frontend calls Django’s endpoint:


fetch("/api/twitter-data")
  .then((res) => res.json())
  .then((data) => console.log(data));


✅ 2. Distributed Rate Limiting in Django with Redis
If multiple users make API requests, rate-limiting per user/IP is needed. Redis helps handle this efficiently.

🛠️ Tech Used:
Redis: Stores request count per user/IP
Django Ratelimit: Blocks excessive requests
Celery (Optional): For background cleanup
🔹 Step 1: Install Dependencies

pip install django-ratelimit django-redis

🔹 Step 2: Configure Redis in settings.py

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

🔹 Step 3: Apply Rate Limiting in Django Views

from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit

@ratelimit(key="ip", rate="5/m", method="GET", block=True)
def my_api_view(request):
    return JsonResponse({"message": "API response"})

✅ This limits each IP to 5 requests per minute. If exceeded, requests are blocked.


✅ 3. User-Based Rate Limiting (JWT + Redis)
If users are authenticated via JWT, you can limit API usage per user instead of per IP.

🔹 Example
@ratelimit(key=lambda r: r.user.id if r.user.is_authenticated else 'ip', rate="5/m", method="GET", block=True)
def user_based_view(request):
    return JsonResponse({"message": "User API response"})

✅ This limits each user to 5 requests per minute.

🚀 Summary
Method	Use Case	Best For
Env Variables (.env)	Secure API Keys	Backend storage
Django Proxy (views.py)	Hide API Keys	Prevent direct frontend exposure
Redis Rate Limiting	Handle high traffic	API abuse prevention
JWT-based Rate Limit	Per-user limit	Multi-user apps

Note: 🔹 Use Environment Variables (.env File)
Never store API keys directly in the frontend. Instead, use a backend proxy or environment variables.

What is Hoisting?
Hoisting is JavaScript's default behavior of moving variable and function declarations to the top of their containing scope before execution. 
This means you can use variables and functions before they are declared.

1. Hoisting with var

console.log(a);  // Output: undefined
var a = 10;
console.log(a);  // Output: 10


Explanation:

The declaration var a; is hoisted to the top, but not its initialization (a = 10).
So, when console.log(a); runs before initialization, it prints undefined.

Internally, JavaScript treats it like this:
var a;  // Hoisted declaration
console.log(a);  // undefined
a = 10;
console.log(a);  // 10


2. Hoisting with let and const (Not Hoisted the Same Way)
console.log(b);  // ReferenceError: Cannot access 'b' before initialization
let b = 20;

let and const declarations are hoisted, but they are in a Temporal Dead Zone (TDZ) until the execution reaches their initialization.
Accessing them before declaration causes a ReferenceError.

3. Hoisting with Functions
Function Declarations (Hoisted)

greet();  // Output: "Hello!"
function greet() {
    console.log("Hello!");
}

Function declarations are fully hoisted.
You can call greet() before it is defined.

Function Expressions (Not Hoisted)
sayHello();  // TypeError: sayHello is not a function
var sayHello = function() {
    console.log("Hello!");
};


Only the variable declaration (var sayHello;) is hoisted, not the function assignment.
So sayHello is undefined when called.

4. Best Practices
✅ Use let and const to avoid unexpected behavior.
✅ Declare functions before using them for better readability.
✅ Avoid using var because of its function-scoped hoisting behavio

Difference Between var, let, and const in JavaScript
Feature	var	let	const
Scope	Function-scoped	Block-scoped	Block-scoped
Hoisting	Hoisted (initialized as undefined)	Hoisted (in Temporal Dead Zone)	Hoisted (in Temporal Dead Zone)
Reassignment	✅ Yes	✅ Yes	❌ No (constant value)
Redeclaration	✅ Yes	❌ No	❌ No
Mutable	✅ Yes	✅ Yes	✅ Yes (for objects & arrays, but not reassignable)

1. var (Function-Scoped, Hoisted)
✅ Can be redeclared and reassigned
⚠️ Hoisted with undefined, leading to unexpected behavior
⚠️ Function-scoped, so it ignores block-level scope


console.log(x); // undefined (Hoisted but not initialized)
var x = 10;
console.log(x); // 10

if (true) {
    var y = 20; // Available outside the block
}
console.log(y); // 20 (not block-scoped)


2. let (Block-Scoped, No Redeclaration)
✅ Can be reassigned
⚠️ Hoisted but in a Temporal Dead Zone (TDZ)
❌ Cannot be redeclared in the same scope

console.log(a); // ReferenceError: Cannot access 'a' before initialization
let a = 10;
console.log(a); // 10

if (true) {
    let b = 20;
    console.log(b); // 20 (inside block)
}
console.log(b); // ReferenceError: b is not defined (block-scoped)


3. const (Block-Scoped, Immutable Reference)
✅ Must be initialized at the time of declaration
❌ Cannot be reassigned
✅ Mutable for objects/arrays (but reference remains constant)

const PI = 3.14;
PI = 3.1415; // TypeError: Assignment to constant variable

const person = { name: "Alice" };
person.name = "Bob"; // ✅ Allowed (object properties are mutable)
console.log(person.name); // "Bob"

person = {}; // ❌ TypeError (Reference cannot change)


4. When to Use What?
Use Case	Preferred Choice
Variable that changes	let
Constant value	const
Old (Avoid using)	var





