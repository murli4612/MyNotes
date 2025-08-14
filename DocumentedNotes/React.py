1. Creating a Simple Custom Hook
Let's create a custom hook useCounter to manage a counter.

import { useState } from "react";

function useCounter(initialValue = 0) {
    const [count, setCount] = useState(initialValue);

    const increment = () => setCount(count + 1);
    const decrement = () => setCount(count - 1);
    const reset = () => setCount(initialValue);

    return { count, increment, decrement, reset };
}

export default useCounter;

Using the Hook in a Component
import React from "react";
import useCounter from "./useCounter";

function CounterComponent() {
    const { count, increment, decrement, reset } = useCounter(10);

    return (
        <div>
            <h2>Count: {count}</h2>
            <button onClick={increment}>Increment</button>
            <button onClick={decrement}>Decrement</button>
            <button onClick={reset}>Reset</button>
        </div>
    );
}

export default CounterComponent;

2. Custom Hook for Fetching Data (useFetch)
A hook to fetch data from an API.
import { useState, useEffect } from "react";

function useFetch(url) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(url);
                if (!response.ok) throw new Error("Network response was not ok");
                const result = await response.json();
                setData(result);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [url]);

    return { data, loading, error };
}

export default useFetch;

Using useFetch in a Component
import React from "react";
import useFetch from "./useFetch";

function UsersList() {
    const { data, loading, error } = useFetch("https://jsonplaceholder.typicode.com/users");

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;

    return (
        <ul>
            {data.map((user) => (
                <li key={user.id}>{user.name}</li>
            ))}
        </ul>
    );
}

export default UsersList;

3. Custom Hook for Managing Local Storage (useLocalStorage)
This hook stores and retrieves values from local storage.

import { useState } from "react";

function useLocalStorage(key, initialValue) {
    const [value, setValue] = useState(() => {
        const storedValue = localStorage.getItem(key);
        return storedValue ? JSON.parse(storedValue) : initialValue;
    });

    const updateValue = (newValue) => {
        setValue(newValue);
        localStorage.setItem(key, JSON.stringify(newValue));
    };

    return [value, updateValue];
}

export default useLocalStorage;

Using useLocalStorage
import React from "react";
import useLocalStorage from "./useLocalStorage";

function NameStorage() {
    const [name, setName] = useLocalStorage("username", "Guest");

    return (
        <div>
            <h2>Name: {name}</h2>
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        </div>
    );
}

export default NameStorage;

Key Benefits of Custom Hooks
✅ Reusability – Use the same logic in multiple components.
✅ Separation of Concerns – Keeps components clean by moving logic into hooks.
✅ Better Code Organization – Makes code more modular and readable.



React Fiber: The Reconciliation Engine of React
What is React Fiber?
React Fiber is the reconciliation algorithm introduced in React 16 to improve rendering performance and responsiveness. 
It replaces the older stack-based reconciliation algorithm and allows React to work efficiently on large, complex UIs.

Key Features of React Fiber
1️⃣ Incremental Rendering (Time-Slicing)

Instead of blocking the UI, React Fiber splits rendering into chunks and works in a non-blocking manner.
This makes animations and interactions smoother.
2️⃣ Prioritization of Updates

React Fiber assigns different priority levels to UI updates (e.g., user interactions are more important than background data fetching).
This ensures a faster UI response.
3️⃣ Concurrency Mode

Allows React to pause, resume, and discard rendering work if needed.
Helps improve performance on slower devices.
4️⃣ Better Support for Suspense & Lazy Loading

React Suspense and React.lazy() work efficiently because of Fiber’s ability to manage rendering interruptions.
5️⃣ Improved Error Handling

React 16 introduced error boundaries, allowing components to catch errors without crashing the entire app.
How React Fiber Works?

React Fiber breaks rendering into two phases:

Render Phase (Work Preparation) - Can be Interrupted

React walks through the component tree and prepares changes.
If React finds a more urgent task (like a button click), it pauses and resumes later.
Commit Phase (UI Update) - Cannot Be Interrupted

The final changes are applied to the DOM.
This phase is fast and synchronous.

Why is React Fiber Important?
✅ Makes React faster and more efficient
✅ Improves user experience with smooth UI updates
✅ Handles animations, gestures, and transitions better
✅ Allows React to introduce features like Suspense and Concurrent Mode

🚀 React Fiber is the backbone of modern React applications, making them highly performant and responsive!


What are Error Boundaries?
Error Boundaries are React components that catch JavaScript errors in their child component tree, log the errors, and prevent the entire application from crashing.

🔹 Introduced in React 16
🔹 Works only for class components (functional components require useEffect with error handling)
🔹 Catches errors in rendering, lifecycle methods, and constructors of child components

How to Create an Error Boundary?
You create an error boundary by defining a class component with the special lifecycle method:


import React, { Component } from "react";

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state to show fallback UI
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Error caught by Error Boundary:", error, errorInfo);
    // You can log this error to an error tracking service
  }

  render() {
    if (this.state.hasError) {
      return <h2>Something went wrong.</h2>;
    }

    return this.props.children;
  }
}

export default ErrorBoundary;


How to Use an Error Boundary?

Wrap the components that might throw errors inside the <ErrorBoundary> component:

import ErrorBoundary from "./ErrorBoundary";
import MyComponent from "./MyComponent";

function App() {
  return (
    <ErrorBoundary>
      <MyComponent />
    </ErrorBoundary>
  );
}

export default App;


Where to Use Error Boundaries?
✅ At the top level of the app (to prevent the whole app from crashing)
✅ Around critical UI components (e.g., a dashboard, chat widget, or video player)
✅ Around third-party libraries (to catch external errors)

Limitations of Error Boundaries
🚫 Cannot catch errors in event handlers → Use try...catch inside event handlers
🚫 Does not work in functional components directly (but can use hooks like useErrorBoundary from third-party libraries)
🚫 Does not catch errors in asynchronous code (e.g., setTimeout, fetch)

Conclusion
Error Boundaries improve React app stability by preventing crashes and showing fallback UIs. They are essential for production-ready React applications. 🚀

Using Error Boundaries in Functional Components
🚀 Functional components do not support lifecycle methods like componentDidCatch.
📌 Instead, you have two options:

Use an existing Error Boundary (Class Component) and wrap your functional component.
Use React’s useEffect + try-catch for handling specific errors.
Use a third-party hook like use-error-boundary.


✅ Option 1: Using a Class-Based Error Boundary in Functional Components
Since React does not support error boundaries in functional components, the recommended way is to wrap functional components inside a class-based error boundary.

Step 1: Create an Error Boundary (Class Component)

import React, { Component } from "react";

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Error caught:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h2>Something went wrong.</h2>;
    }
    return this.props.children;
  }
}

export default ErrorBoundary;


Step 2: Wrap Functional Components in Error Boundary
import React from "react";
import ErrorBoundary from "./ErrorBoundary";

const MyComponent = () => {
  throw new Error("Oops! An error occurred."); // Simulating an error
  return <h1>Hello, World!</h1>;
};

const App = () => {
  return (
    <ErrorBoundary>
      <MyComponent />
    </ErrorBoundary>
  );
};

export default App;

🔹 If MyComponent throws an error, the Error Boundary catches it and prevents the whole app from crashing.

✅ Option 2: Handling Errors with useEffect in Functional Components
If you want to handle specific errors inside a functional component, you can use useEffect with a try-catch block:

import React, { useEffect, useState } from "react";

const MyComponent = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    try {
      // Simulating an error
      throw new Error("Data fetch failed!");
    } catch (err) {
      setError(err.message);
    }
  }, []);

  if (error) {
    return <h2>Error: {error}</h2>;
  }

  return <h1>Data: {data}</h1>;
};

export default MyComponent;


📌 Limitations:

This does not catch errors in rendering like an Error Boundary.
Only useful for fetching or side-effects inside useEffect.

✅ Option 3: Using a Third-Party Hook (use-error-boundary)
If you want Error Boundaries inside functional components, use use-error-boundary:

Step 1: Install the package
npm install use-error-boundary

Step 2: Use the useErrorBoundary Hook
import React from "react";
import { useErrorBoundary } from "use-error-boundary";

const MyComponent = () => {
  const { ErrorBoundary, didCatch, error } = useErrorBoundary();

  if (didCatch) {
    return <h2>Error: {error.message}</h2>;
  }

  return (
    <ErrorBoundary>
      <button onClick={() => { throw new Error("Oops!"); }}>Click to Error</button>
    </ErrorBoundary>
  );
};

export default MyComponent;


✅ This allows error boundary handling inside functional components.

📌 Conclusion
1️⃣ Best Practice: Use a class-based error boundary to wrap functional components.
2️⃣ For Side Effects (API Calls): Use try-catch inside useEffect.
3️⃣ For Native Functional Error Boundaries: Use a third-party hook like use-error-boundary.

🚀 Error Boundaries help make React applications more stable and production-ready!



3. Suspense and Lazy Loading
React Fiber introduces Suspense and Lazy Loading for improved code splitting and asynchronous data fetching.

Example:

import React, { Suspense, lazy } from "react";

const MyComponent = lazy(() => import("./MyComponent"));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <MyComponent />
    </Suspense>
  );
}


⏳ Suspense ensures the UI remains responsive while components load asynchronously.

React Suspense - Lazy Loading & Data Fetching
🚀 React Suspense allows you to delay rendering a component until some condition (like data fetching or code loading) is met. It improves performance and user experience.

1️⃣ Basic Example: Lazy Loading a Component
📌 Use Case: Load a component only when needed, reducing initial bundle size.

🔹 Example: Lazy Load a Component

import React, { Suspense, lazy } from "react";

// Lazy load the component
const MyComponent = lazy(() => import("./MyComponent"));

const App = () => {
  return (
    <Suspense fallback={<h2>Loading...</h2>}>
      <MyComponent />
    </Suspense>
  );
};

export default App;


✅ Explanation:

lazy(() => import("./MyComponent")) loads the component only when needed.
<Suspense fallback={<h2>Loading...</h2>}> shows Loading... while the component is being fetched.

2️⃣ Suspense with React Router (Lazy Loading Pages)
📌 Use Case: Improve performance by loading pages only when a user navigates to them.

🔹 Example: Lazy Loading Routes

import React, { Suspense, lazy } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));

const App = () => {
  return (
    <Router>
      <Suspense fallback={<h2>Loading page...</h2>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Suspense>
    </Router>
  );
};

export default App;

✅ Benefits:
✔ Reduces initial load time by loading only necessary pages.
✔ Makes the app feel faster when navigating between pages.

3️⃣ Suspense with Data Fetching (React 18+)
📌 Use Case: Suspend rendering until data is fetched (works with React Server Components).

🔹 Example: Suspense with Data Fetching

import React, { Suspense } from "react";
import { fetchData } from "./api"; // Simulated API call

const Resource = React.lazy(() => import("./Resource"));

const App = () => {
  return (
    <Suspense fallback={<h2>Fetching Data...</h2>}>
      <Resource />
    </Suspense>
  );
};

export default App;

✅ Why Use This?
✔ Prevents "loading" states cluttering the UI.
✔ Improves user experience by waiting until all data is ready before rendering.

📌 Key Takeaways
🔹 Lazy load components to reduce initial bundle size.
🔹 Use Suspense in React Router for efficient page transitions.
🔹 Combine Suspense with data fetching for smoother user experiences (React 18+).

🚀 React Suspense makes React apps more efficient, faster, and user-friendly!

React Router Explained 🚀
📌 React Router is a powerful library that enables client-side routing in React applications. 
It allows users to navigate between different pages without full page reloads, making apps faster and more interactive.

1️⃣ Installation
First, install react-router-dom using npm or yarn:

npm install react-router-dom

or

yarn add react-router-dom

2️⃣ Basic Routing Example
📌 Use Case: Define multiple pages and navigate between them.

import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

const Home = () => <h2>Home Page</h2>;
const About = () => <h2>About Page</h2>;
const Contact = () => <h2>Contact Page</h2>;

const App = () => {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link> | <Link to="/about">About</Link> | <Link to="/contact">Contact</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  );
};

export default App;

✅ How It Works:

<Router>: Wraps the app to enable routing.
<Routes>: Contains multiple <Route> components.
<Route path="/" element={<Home />}>: Defines the URL path and its corresponding component.
<Link to="/about">About</Link>: Provides navigation without reloading the page.

3️⃣ Route Parameters (Dynamic Routing)
📌 Use Case: Pass dynamic values in the URL (e.g., user profiles).

import React from "react";
import { BrowserRouter as Router, Route, Routes, Link, useParams } from "react-router-dom";

const UserProfile = () => {
  const { username } = useParams(); // Get dynamic parameter
  return <h2>Welcome, {username}!</h2>;
};

const App = () => {
  return (
    <Router>
      <nav>
        <Link to="/user/John">John's Profile</Link> | <Link to="/user/Alice">Alice's Profile</Link>
      </nav>

      <Routes>
        <Route path="/user/:username" element={<UserProfile />} />
      </Routes>
    </Router>
  );
};

export default App;

✅ How It Works:

path="/user/:username": :username is a dynamic parameter.
useParams() retrieves the value from the URL.


4️⃣ Nested Routes
📌 Use Case: Create a layout where child components are rendered inside a parent route.

import React from "react";
import { BrowserRouter as Router, Routes, Route, Outlet, Link } from "react-router-dom";

const Dashboard = () => (
  <div>
    <h2>Dashboard</h2>
    <nav>
      <Link to="stats">Stats</Link> | <Link to="settings">Settings</Link>
    </nav>
    <Outlet /> {/* Renders nested routes here */}
  </div>
);

const Stats = () => <h3>Stats Page</h3>;
const Settings = () => <h3>Settings Page</h3>;

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />}>
          <Route path="stats" element={<Stats />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </Router>
  );
};

export default App;


✅ How It Works:

Dashboard is the parent route with <Outlet /> to render child routes (Stats and Settings).
URLs: /dashboard/stats, /dashboard/settings.


5️⃣ Redirects & 404 Page Handling
📌 Use Case: Redirect users when they visit an unknown page.

import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

const Home = () => <h2>Home Page</h2>;
const NotFound = () => <h2>404 - Page Not Found</h2>;

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="*" element={<NotFound />} />  {/* Catch-all route */}
      </Routes>
    </Router>
  );
};

export default App;

✅ How It Works:

path="*" matches any unknown routes and redirects users to a 404 page.

6️⃣ Programmatic Navigation (useNavigate)
📌 Use Case: Redirect users after login or button clicks.

import React from "react";
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  return (
    <div>
      <h2>Home Page</h2>
      <button onClick={() => navigate("/about")}>Go to About</button>
    </div>
  );
};

const About = () => <h2>About Page</h2>;

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
};

export default App;


✅ How It Works:

useNavigate() lets you navigate without using <Link>.
Clicking "Go to About" programmatically redirects to /about.

7️⃣ Protected Routes (Authentication Example)
📌 Use Case: Restrict certain pages based on user authentication.

import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

const isAuthenticated = false; // Simulated authentication state

const ProtectedRoute = ({ children }) => {
  return isAuthenticated ? children : <Navigate to="/" />;
};

const Dashboard = () => <h2>Dashboard - Private Page</h2>;
const Home = () => <h2>Home Page</h2>;

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
};

export default App;

✅ How It Works:

If isAuthenticated === false, users are redirected to the home page (/).
Otherwise, they can access /dashboard.


🔹 Summary of Key Features
Feature	Description
BrowserRouter	Enables client-side routing.
Routes	Wraps all <Route> components.
Route	Defines a route with a path and element.
Link	Provides navigation without reloading.
useParams	Extracts dynamic route parameters.
useNavigate	Programmatic navigation.
Outlet	Used for nested routes.
Navigate	Redirects users to another page.

📌 Conclusion
🚀 React Router makes single-page applications (SPAs) more dynamic and user-friendly.
✔ Helps in navigating pages without refreshing.
✔ Supports dynamic routing, lazy loading, and protected routes.
✔ Provides better user experience and performance improvements.



1️⃣ Authentication Flow with React Router + Redux
📌 Use Case: Control access to protected pages based on user login state.

🛠 Tech Stack Used
React Router → Handles navigation.
Redux (with Redux Toolkit) → Manages authentication state.
Protected Routes → Restricts access for unauthenticated users.

🔹 Step 1: Install Dependencies
npm install react-router-dom @reduxjs/toolkit react-redux

yarn add react-router-dom @reduxjs/toolkit react-redux

🔹 Step 2: Set Up Redux for Authentication
👉 Create a Redux slice for authentication (authSlice.js).

import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  isAuthenticated: false, // Default: User is NOT logged in
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    login: (state) => {
      state.isAuthenticated = true;
    },
    logout: (state) => {
      state.isAuthenticated = false;
    },
  },
});

export const { login, logout } = authSlice.actions;
export default authSlice.reducer;


🔹 Step 3: Configure Redux Store
👉 Create store.js


import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./authSlice"; // Import auth slice

const store = configureStore({
  reducer: {
    auth: authReducer, // Add auth state to the store
  },
});

export default store;

🔹 Step 4: Create Protected Route Component
👉 Only allow authenticated users to access protected routes


import React from "react";
import { Navigate } from "react-router-dom";
import { useSelector } from "react-redux";

const ProtectedRoute = ({ children }) => {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  return isAuthenticated ? children : <Navigate to="/login" />;
};

export default ProtectedRoute;



🔹 Step 5: Create Login & Logout Components
👉 Login Page (Login.js)


🔹 Step 5: Create Login & Logout Components
👉 Login Page (Login.js)

import React from "react";
import { useDispatch } from "react-redux";
import { login } from "./authSlice";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogin = () => {
    dispatch(login());  // Dispatch login action
    navigate("/dashboard"); // Redirect to dashboard
  };

  return (
    <div>
      <h2>Login Page</h2>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;

👉 Logout Button (Inside Dashboard)
import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "./authSlice";
import { useNavigate } from "react-router-dom";

const Logout = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(logout()); // Dispatch logout action
    navigate("/"); // Redirect to home
  };

  return <button onClick={handleLogout}>Logout</button>;
};

export default Logout;


🔹 Step 6: Create Main App with Routes
👉 Define Routes in App.js

import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { Provider } from "react-redux";
import store from "./store";
import Login from "./Login";
import Dashboard from "./Dashboard";
import ProtectedRoute from "./ProtectedRoute";

const Home = () => <h2>Home Page</h2>;

const Dashboard = () => (
  <div>
    <h2>Dashboard - Private Page</h2>
    <Logout />
  </div>
);

const App = () => {
  return (
    <Provider store={store}>
      <Router>
        <nav>
          <Link to="/">Home</Link> | <Link to="/dashboard">Dashboard</Link> | <Link to="/login">Login</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
        </Routes>
      </Router>
    </Provider>
  );
};

export default App;


✅ How It Works
authSlice.js manages the login/logout state.
store.js creates a Redux store.
ProtectedRoute ensures only authenticated users can access protected pages.
Login page updates Redux state when a user logs in.
Logout button logs out the user and redirects them to home.
Dashboard is only accessible if the user is logged in.


2️⃣ Lazy Loading & Code Splitting with React Router
📌 Why?

Helps reduce initial load time.
Improves performance by loading components only when needed.
🔹 Step 1: Import lazy & Suspense
👉 Modify App.js

import React, { lazy, Suspense } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const Home = lazy(() => import("./Home"));
const Dashboard = lazy(() => import("./Dashboard"));
const Login = lazy(() => import("./Login"));

const App = () => {
  return (
    <Router>
      <Suspense fallback={<h2>Loading...</h2>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Suspense>
    </Router>
  );
};

export default App;



✅ How It Works?

lazy(() => import("./Component")) → Dynamically loads components.
<Suspense> → Displays fallback UI (like "Loading...") while the component loads.

3️⃣ Performance Optimizations
✅ Best Practices for Scaling React Router Applications

Optimization	Explanation
Lazy Loading	Load components only when needed (React.lazy())
Code Splitting	Use dynamic imports for large components
Redux for State Management	Avoid passing props deeply
Debounce Navigation Calls	Prevent unnecessary re-renders
Use Memoization	Optimize expensive re-renders (useMemo, useCallback)

📌 Final Thoughts
🚀 Now you know how to:
✔️ Secure routes using authentication & Redux
✔️ Implement lazy loading for performance
✔️ Use Protected Routes to restrict access
✔️ Improve React Router for large-scale apps


q)🔹 Steps to Implement Authentication with Context API
✅ We will:

Create an AuthContext to store authentication state.
Use useContext in components to access authentication state.
Implement a ProtectedRoute to restrict unauthorized access.

🛠 Step 1: Create an Authentication Context (AuthContext.js)
👉 This will manage user authentication state globally.

import React, { createContext, useState, useContext } from "react";

// Create Auth Context
const AuthContext = createContext();

// Custom Hook to access AuthContext
export const useAuth = () => useContext(AuthContext);

// Provider Component
export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Login Function
  const login = () => {
    setIsAuthenticated(true);
  };

  // Logout Function
  const logout = () => {
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

🔹 Step 2: Create Protected Route Component (ProtectedRoute.js)
👉 This component restricts access to authenticated users only.

import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();

  return isAuthenticated ? children : <Navigate to="/login" />;
};

export default ProtectedRoute;

🔹 Step 3: Create Login Component (Login.js)
👉 Users will click the login button to authenticate.

import React from "react";
import { useAuth } from "./AuthContext";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = () => {
    login();  // Call login function from AuthContext
    navigate("/dashboard");  // Redirect to dashboard
  };

  return (
    <div>
      <h2>Login Page</h2>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;


🔹 Step 4: Create Logout Component (Logout.js)
👉 Users can log out from the dashboard.

import React from "react";
import { useAuth } from "./AuthContext";
import { useNavigate } from "react-router-dom";

const Logout = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout(); // Call logout function from AuthContext
    navigate("/"); // Redirect to home page
  };

  return <button onClick={handleLogout}>Logout</button>;
};

export default Logout;



🔹 Step 5: Define Routes in App.js
👉 Wrap everything inside AuthProvider

import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { AuthProvider } from "./AuthContext";
import ProtectedRoute from "./ProtectedRoute";
import Login from "./Login";
import Logout from "./Logout";

const Home = () => <h2>Home Page</h2>;

const Dashboard = () => (
  <div>
    <h2>Dashboard - Private Page</h2>
    <Logout />
  </div>
);

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <nav>
          <Link to="/">Home</Link> | <Link to="/dashboard">Dashboard</Link> | <Link to="/login">Login</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;


🎯 How It Works
AuthProvider holds the global authentication state (isAuthenticated).
useAuth() provides access to login/logout functions.
ProtectedRoute ensures only logged-in users access restricted pages.
Login & Logout modify the authentication state.
React Router handles navigation.

🔹 Why Use Context API Over Redux?
Feature	Context API	Redux
Setup Complexity	Simple	More complex
Performance	Good for small apps	Better for large-scale apps
Global State	Yes	Yes
Middleware Support	No	Yes (Redux Thunk, Saga)
Debugging Tools	Limited	Excellent (Redux DevTools)

Use Context API if:
✔️ Your app is small/medium-sized.
✔️ You need global state without extra dependencies.
✔️ You prefer a simpler setup.

Use Redux if:
✔️ Your app is large with many global states.
✔️ You need advanced debugging & middleware.
✔️ You work with complex async operations (API calls, caching).


🔹 How Authentication Works with a Backend
User submits login credentials (email/password) to the server via an API request.
Server validates credentials using a database and generates a JWT (JSON Web Token) or session token.
Client stores the token in HTTP-only cookies (preferred) or local storage.
For each protected request, the client sends the token, and the server verifies it before responding.


🔹 Modify AuthProvider to Authenticate via Server
✅ Step 1: Modify login() to Send API Request

import React, { createContext, useState, useContext } from "react";

// Create Auth Context
const AuthContext = createContext();

// Custom Hook to access AuthContext
export const useAuth = () => useContext(AuthContext);

// Provider Component
export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Login Function - Authenticate with the server
  const login = async (email, password) => {
    try {
      const response = await fetch("https://your-api.com/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // Important for cookies
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        setIsAuthenticated(true);
      } else {
        console.error("Login failed");
      }
    } catch (error) {
      console.error("Error logging in:", error);
    }
  };

  // Logout Function - Tell server to invalidate session
  const logout = async () => {
    try {
      await fetch("https://your-api.com/logout", {
        method: "POST",
        credentials: "include", // Important for cookies
      });

      setIsAuthenticated(false);
    } catch (error) {
      console.error("Error logging out:", error);
    }
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};


🔹 Step 2: Login Component

import React, { useState } from "react";
import { useAuth } from "./AuthContext";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    await login(email, password);
    navigate("/dashboard"); // Redirect after login
  };

  return (
    <div>
      <h2>Login</h2>
      <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;


🔹 Step 3: Secure API with JWT (Django Example)
The backend (Django, FastAPI, Node.js, etc.) will handle authentication.

Django API (views.py)

from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["POST"])
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(email=email, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})
    return Response({"error": "Invalid credentials"}, status=401)


Django Middleware for Protected Routes

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "You are authenticated!"})

🔹 How Does It Work?
✅ The client sends login credentials → Server validates and returns JWT.
✅ The client stores the JWT securely (HTTP-only cookies).
✅ For protected routes, the client sends the token in the request.
✅ The server verifies the token before granting access.


🔹 Why Use Server-Based Authentication?
❌ Client-side Only (Bad)	✅ Server-side Authentication (Good)
Vulnerable to token theft (stored in local storage)	More secure (uses HTTP-only cookies)
Tokens can be easily modified	Server verifies JWT on every request
Logout requires manual token removal	Server invalidates session on logout

🎯 Conclusion
🔹 The frontend only manages login state, but authentication is handled by the backend.
🔹 Always store tokens in HTTP-only cookies to prevent XSS attacks.
🔹 For protected routes, the client sends the token on every request.



Q20. What are React Fragments?
Fragments allow grouping elements without adding extra nodes to the DOM.

<>
  <h1>Hello</h1>
  <p>World</p>
</>

🔹 What is a React Portal?
A React Portal allows you to render a component outside the main DOM hierarchy while keeping it inside the React component tree. It is useful for UI elements like modals,
 tooltips, dropdowns, and pop-ups that need to visually break out of the main component structure.
 
 Normally, React components render inside their parent DOM elements. However, sometimes we need to: 
 ✅ Prevent CSS overflow issues (e.g., modal appearing behind a div with overflow: hidden).
✅ Avoid z-index problems with nested elements.
✅ Keep a component logically inside React but outside in the DOM for better positioning.



🔹 How to Create a Portal?
✅ Step 1: Create a Target DOM Element
Add a div in your HTML file (index.html) where the portal will mount:

<body>
  <div id="root"></div>
  <div id="portal-root"></div>  <!-- Portal target -->
</body>


✅ Step 2: Use ReactDOM.createPortal()
The createPortal method takes two arguments: 1️⃣ What to render – The JSX you want to display
2️⃣ Where to render – The DOM node where it should be mounted


import React from "react";
import ReactDOM from "react-dom";

const Modal = ({ children }) => {
  return ReactDOM.createPortal(
    <div className="modal">
      {children}
    </div>,
    document.getElementById("portal-root") // Renders outside #root
  );
};

export default Modal;


✅ Step 3: Use the Modal Component
Now, you can use the <Modal> component anywhere, and it will render inside the #portal-root outside of #root.

import React, { useState } from "react";
import Modal from "./Modal";

const App = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div>
      <h1>Main App</h1>
      <button onClick={() => setIsOpen(true)}>Open Modal</button>

      {isOpen && (
        <Modal>
          <div className="modal-content">
            <h2>Portal Modal</h2>
            <button onClick={() => setIsOpen(false)}>Close</button>
          </div>
        </Modal>
      )}
    </div>
  );
};

export default App;


🔹 Benefits of Using Portals
✅ Escapes Parent Styles: The modal won’t be affected by overflow: hidden or z-index from parent components.
✅ Better Accessibility: Easily place modals at the end of <body> for better screen reader support.
✅ No Re-Renders of Parent: Since the modal is outside, updating it does not trigger re-renders of parent components.


🔹 When to Use Portals?
🔹 Modals, Pop-ups
🔹 Tooltips
🔹 Floating UI Elements (Dropdowns, Menus)
🔹 Toast Notifications



✅ 1. API Caching in React (Using SWR or React Query)
Instead of fetching data from the backend every time, use React Query or SWR to cache API responses.

🔹 Using SWR for Client-Side Caching
import useSWR from "swr";

const fetcher = (url) => fetch(url).then((res) => res.json());

function ProductList() {
  const { data, error } = useSWR("/api/products", fetcher);

  if (error) return <p>Error loading products...</p>;
  if (!data) return <p>Loading...</p>;

  return (
    <ul>
      {data.products.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}

✅ Now, API responses are cached and won’t refetch unless necessary.

✅ 2. JWT Authentication in React
On login, store the JWT token in localStorage or httpOnly cookies
Attach the token in every API request for authentication
🔹 Login & Store JWT Token

async function login(username, password) {
  const response = await fetch("/api/token/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  if (response.ok) {
    localStorage.setItem("access_token", data.access);
    localStorage.setItem("refresh_token", data.refresh);
  }
}

✅ 3. Sending Authenticated Requests
Attach the JWT token in API headers for authentication.

🔹 Fetch Data with JWT

async function fetchProtectedData() {
  const token = localStorage.getItem("access_token");

  const response = await fetch("/protected_view/", {
    headers: { Authorization: `Bearer ${token}` },
  });

  if (response.ok) {
    return await response.json();
  } else {
    throw new Error("Unauthorized");
  }
}

✅ Now, only authenticated users can access protected APIs.
✅ 4. Refresh JWT Token Automatically
If the JWT token expires, use the refresh token to get a new one.

🔹 Token Refresh Logic
async function refreshToken() {
  const refresh = localStorage.getItem("refresh_token");

  const response = await fetch("/api/token/refresh/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh }),
  });

  const data = await response.json();
  if (response.ok) {
    localStorage.setItem("access_token", data.access);
  }
}

✅ Now, expired tokens are refreshed automatically, preventing logout.


🚀 Summary
Feature	Django Backend	React Frontend
Caching	Redis (django-redis)	SWR or React Query
JWT Auth	rest_framework_simplejwt	Store token in localStorage
Auth Requests	DRF permissions (IsAuthenticated)	Attach JWT token in API headers
Token Refresh	/api/token/refresh/	Auto-refresh using fetch


What is the Virtual DOM?
The Virtual DOM (VDOM) is a lightweight, in-memory representation of the actual DOM (Document Object Model). 
It is a core concept in React that helps improve performance by minimizing direct manipulations of the real DOM.

Instead of updating the real DOM directly, React uses the Virtual DOM to track changes efficiently and update only the necessary parts of the UI.

How the Virtual DOM Works?
React follows these steps to update the UI efficiently:

Render: When a component’s state or props change, React creates a new Virtual DOM tree.
Diffing: React compares the new Virtual DOM with the previous one using a diffing algorithm to detect changes.
Reconciliation: React updates only the changed elements in the real DOM instead of re-rendering the entire page.
Efficient Updates: React batches updates to minimize expensive DOM operations.

How Does Virtual DOM Improve Performance?
The real DOM is slow because:

It involves recalculating styles, reflowing layouts, and repainting the screen every time an update occurs.
Updating the real DOM frequently can cause performance bottlenecks.
The Virtual DOM improves performance by:

Minimizing Direct DOM Manipulation

The real DOM is updated only when necessary, reducing the number of costly re-renders.
Batching Updates

React groups multiple changes together before applying them to the real DOM, making updates more efficient.
Efficient Re-rendering with Diffing Algorithm

React compares the old and new Virtual DOM trees and updates only the changed parts.
Component-Based Architecture

The UI is broken into smaller reusable components, reducing the scope of updates.


Example: Virtual DOM vs. Real DOM
Without Virtual DOM (Traditional Approach)

document.getElementById('button').addEventListener('click', () => {
  document.getElementById('counter').innerText = parseInt(document.getElementById('counter').innerText) + 1;
});


The browser modifies the real DOM directly, which triggers unnecessary recalculations.

With Virtual DOM (React Approach)

import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Counter: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};

export default Counter;


React updates the Virtual DOM first, then efficiently updates only the changed elements in the real DOM.


Conclusion
The Virtual DOM is one of React's key optimizations. It reduces unnecessary DOM updates, enhances performance, 
and provides a smooth user experience by applying changes efficiently.


Comparison: Controlled vs. Uncontrolled Components
Feature	Controlled Components	Uncontrolled Components
Data Handling	Controlled by React state	Controlled by the DOM
Updates	onChange updates state	Value accessed via ref
Predictability	More predictable	Less predictable
Performance	May cause re-renders on every input change	Better for performance in large forms
Validation	Easier to validate in real-time	Validation requires manual handling
Use Case	Forms, validation, controlled UI updates	Integrating with non-React libraries (e.g., third-party form handlers)
Which One Should You Use?
Use Controlled Components when you need:

Real-time validation
Controlled form behaviors (e.g., disabling submit until valid)
Centralized state management
Use Uncontrolled Components when:

Integrating with third-party libraries (e.g., jQuery plugins)
Managing very simple forms where React state is unnecessary
Optimizing performance by reducing re-renders



Summary: React Event Handling
Feature	React	Traditional DOM
Event Object	Uses SyntheticEvent	Uses native Event
Event Naming	onClick, onChange (camelCase)	onclick, onchange (lowercase)
Binding this	Required in class components	Not needed in plain JS
Prevent Default	event.preventDefault()	event.preventDefault()
Event Bubbling	Can be stopped with event.stopPropagation()	Same

Conclusion
React normalizes events across browsers using SyntheticEvent.
Events in React use camelCase syntax (onClick instead of onclick).
In class components, binding this is necessary unless using arrow functions.
Use event.preventDefault() to prevent default behaviors (e.g., form submission).
Use event.stopPropagation() to stop event bubbling.



Key Differences:
Feature	React	ReactDOM
Package Name	react	react-dom
Purpose	Defines React components, state, hooks, etc.	Renders components into the browser's DOM
Usage	Used in both React Web and React Native	Used only for web applications
Rendering	Does NOT handle rendering	Handles rendering components to the DOM (ReactDOM.createRoot().render())


1. useState – Manages State in Functional Components
Allows components to maintain state without using a class.
Returns an array with the state variable and a function to update it.

✅ Example: Counter using useState

import React, { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0); // Initialize state

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};

export default Counter;



2. useEffect – Handles Side Effects (e.g., API Calls, Subscriptions)
Runs after every render (by default).
Can be configured to run once (on mount) or when specific values change.
✅ Example: Fetching Data from an API

import React, { useState, useEffect } from "react";

const DataFetcher = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then(response => response.json())
      .then(json => setData(json));

  }, []); // Empty dependency array = run only on mount

  return (
    <ul>
      {data.slice(0, 5).map(item => <li key={item.id}>{item.title}</li>)}
    </ul>
  );
};

export default DataFetcher;

✅ Key Points:

Runs once when the component mounts (empty [] dependency array).
Used for API calls, event listeners, DOM updates, etc.

3. useContext – Access Global State Without Props Drilling
Allows components to consume values from React Context without passing props down manually.
✅ Example: Using Context for Theme Management

import React, { useContext } from "react";
import { ThemeContext } from "./ThemeContext";

const ThemedComponent = () => {
  const theme = useContext(ThemeContext); // Access global theme

  return <div style={{ background: theme }}>Themed Component</div>;
};


✅ Key Points:

Replaces the need for prop drilling in deeply nested components.
Works well with global themes, authentication, and settings.


4. useRef – Access DOM Elements or Persist Values Without Re-Renders
Creates a mutable reference (ref) that stays the same across renders.
Used for accessing DOM elements or storing values without causing re-renders.


✅ Example: Focusing an Input Field on Mount
import React, { useRef, useEffect } from "react";

const InputFocus = () => {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus(); // Focus input on mount
  }, []);

  return <input ref={inputRef} type="text" />;
};

export default InputFocus;



✅ Key Points:

useRef.current gives access to the element.
Doesn’t trigger re-renders when updated.

5. useReducer – Manages Complex State Logic (Alternative to useState)
Similar to Redux, but built-in.
Useful for managing complex state logic (e.g., form validation, multiple state updates).
✅ Example: Counter with useReducer

import React, { useReducer } from "react";

const reducer = (state, action) => {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    default:
      return state;
  }
};

const Counter = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
    </div>
  );
};

export default Counter;

✅ Key Points:

useReducer is great for state logic involving multiple actions.
Similar to Redux’s reducer pattern.


Other Useful Hooks
Hook	Purpose
useMemo	Optimizes performance by memoizing computed values.
useCallback	Optimizes performance by memoizing functions to prevent unnecessary re-renders.
useLayoutEffect	Similar to useEffect, but fires synchronously after DOM updates.
useImperativeHandle	Customizes ref handling for forwarded refs.

1️⃣ useMemo – Memoizing Computed Values
Scenario: Avoid recalculating expensive operations unless dependencies change.

import React, { useState, useMemo } from "react";

const ExpensiveCalculation = ({ num }) => {
  const computeFactorial = (n) => {
    console.log("Computing factorial...");
    return n <= 1 ? 1 : n * computeFactorial(n - 1);
  };

  const factorial = useMemo(() => computeFactorial(num), [num]); // Memoize result

  return <p>Factorial of {num}: {factorial}</p>;
};

const App = () => {
  const [count, setCount] = useState(5);
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Increment {count}</button>
      <ExpensiveCalculation num={count} />
    </div>
  );
};

export default App;

🔹 Benefit: Prevents recalculating the factorial unless num changes.


2️⃣ useCallback – Memoizing Functions
Scenario: Prevent unnecessary re-renders when passing functions as props.

import React, { useState, useCallback } from "react";

const ChildComponent = ({ onClick }) => {
  console.log("Child rendered!");
  return <button onClick={onClick}>Click Me</button>;
};

const MemoizedChild = React.memo(ChildComponent); // Prevents unnecessary re-renders

const App = () => {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log("Button Clicked!");
  }, []); // Memoize function so it does not re-create every render

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <MemoizedChild onClick={handleClick} />
    </div>
  );
};

export default App;

🔹 Benefit: useCallback prevents unnecessary re-rendering of ChildComponent.

3️⃣ useLayoutEffect – Synchronous DOM Updates
Scenario: Runs before the browser paints the screen, useful for DOM measurements.


import React, { useState, useEffect, useLayoutEffect, useRef } from "react";

const App = () => {
  const [count, setCount] = useState(0);
  const countRef = useRef();

  useLayoutEffect(() => {
    console.log("useLayoutEffect: Updating color before render");
    countRef.current.style.color = "red";
  }, [count]);

  useEffect(() => {
    console.log("useEffect: DOM updated");
  }, [count]);

  return (
    <div>
      <h1 ref={countRef}>{count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};

export default App;


🔹 Difference from useEffect:

useLayoutEffect runs before the browser renders.
useEffect runs after the render.

4️⃣ useImperativeHandle – Custom Ref Handling
Scenario: Customize ref behavior when using forwardRef


4️⃣ useImperativeHandle – Custom Ref Handling
Scenario: Customize ref behavior when using forwardRef.

import React, { useRef, useImperativeHandle, forwardRef } from "react";

const CustomInput = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    clear: () => (inputRef.current.value = ""),
  }));

  return <input ref={inputRef} type="text" placeholder="Enter text..." />;
});

const App = () => {
  const inputRef = useRef();

  return (
    <div>
      <CustomInput ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
      <button onClick={() => inputRef.current.clear()}>Clear</button>
    </div>
  );
};

export default App;


🔹 Benefit: Allows parent components to control child components via ref.
Recap & When to Use Each Hook
Hook	Purpose
useMemo	Optimize expensive calculations by memoizing values.
useCallback	Optimize function references to prevent unnecessary re-renders.
useLayoutEffect	Execute effects before browser paints the screen.
useImperativeHandle	Customize ref behavior in forwarded components.


1️⃣ ref (Regular Refs in React)
What is ref?
A ref (reference) in React provides a way to directly interact with a DOM element or a React component without using state.

How to Use ref?
Example: Accessing a DOM Element

import React, { useRef } from "react";

const InputFocus = () => {
  const inputRef = useRef(null); // Create a ref

  const handleFocus = () => {
    inputRef.current.focus(); // Directly focusing the input field
  };

  return (
    <div>
      <input ref={inputRef} type="text" placeholder="Click button to focus" />
      <button onClick={handleFocus}>Focus Input</button>
    </div>
  );
};

export default InputFocus;


How it Works?
useRef(null) creates a reference.
<input ref={inputRef} /> attaches the ref to the input.
Calling inputRef.current.focus() focuses the input field when the button is clicked.

📌 Key Points:

ref.current gives access to the underlying DOM element.
Unlike state, updating ref.current does not trigger a re-render.

2️⃣ forwardRef (Passing Refs to Child Components)
What is forwardRef?
Normally, refs don’t work with functional components (only with DOM elements).
👉 forwardRef allows refs to be passed to child functional components.

Example Without forwardRef (❌ Doesn’t Work)


const CustomInput = ({ placeholder }) => {
  return <input type="text" placeholder={placeholder} />;
};

const ParentComponent = () => {
  const inputRef = useRef(null);
  return <CustomInput ref={inputRef} placeholder="Type here" />;
};


⚠️ This will not work because ref is not passed down to <input>.

Example Using forwardRef (✅ Works)
import React, { useRef, forwardRef } from "react";

// Forwarding the ref from Parent to Input
const CustomInput = forwardRef((props, ref) => {
  return <input ref={ref} type="text" {...props} />;
});

const ParentComponent = () => {
  const inputRef = useRef(null);

  const handleFocus = () => {
    inputRef.current.focus(); // Now it works!
  };

  return (
    <div>
      <CustomInput ref={inputRef} placeholder="Type here" />
      <button onClick={handleFocus}>Focus Input</button>
    </div>
  );
};

export default ParentComponent;


How it Works?
forwardRef wraps the CustomInput component, allowing it to receive a ref from the parent.
The ref is attached to the <input> inside CustomInput, so calling inputRef.current.focus() works.
📌 Key Points:

Use forwardRef to pass refs to child components.
It allows direct manipulation of child component elements without breaking encapsulation.


3️⃣ useImperativeHandle (Customizing Ref Behavior)
Extending forwardRef with useImperativeHandle
If you want to control what gets exposed via ref, use useImperativeHandle.

Example: Customizing Exposed Methods

import React, { useRef, forwardRef, useImperativeHandle } from "react";

const CustomInput = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    clear: () => (inputRef.current.value = ""),
  }));

  return <input ref={inputRef} type="text" {...props} />;
});

const ParentComponent = () => {
  const inputRef = useRef(null);

  return (
    <div>
      <CustomInput ref={inputRef} placeholder="Type here" />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
      <button onClick={() => inputRef.current.clear()}>Clear</button>
    </div>
  );
};

export default ParentComponent;


How it Works?
useImperativeHandle(ref, () => { ... }) exposes custom functions (focus, clear).
The parent can now call inputRef.current.focus() and inputRef.current.clear().
📌 Key Points:

Use useImperativeHandle with forwardRef to control what gets exposed from a child component.

Summary Table
Feature	ref	forwardRef	useImperativeHandle
Used For	Directly accessing DOM elements.	Passing refs to child components.	Customizing ref behavior.
Works With	Native elements (input, div, etc.).	Custom functional components.	Custom functional components.
Needs useRef?	✅ Yes	✅ Yes	✅ Yes
Triggers Re-render?	❌ No	❌ No	❌ No
Use Case	Accessing focus, scrolling, animations.	Allowing parent to control child component.	Exposing controlled methods like focus() and clear().

🚀 When to Use What?
✅ Use ref when you need to directly manipulate a DOM element (e.g., focus an input).
✅ Use forwardRef when you need to pass a ref to a functional component.
✅ Use useImperativeHandle when you need custom methods exposed from a child component.


Let's go deeper into ref, forwardRef, and useImperativeHandle with real-world use cases and optimizations.


1️⃣ ref - Direct DOM Access
📌 Use ref when you need to directly manipulate a DOM element (e.g., focusing an input field, scrolling to an element, etc.).

Example: Auto-focus Input Field on Mount

import React, { useRef, useEffect } from "react";

const AutoFocusInput = () => {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus(); // Automatically focuses input on mount
  }, []);

  return <input ref={inputRef} type="text" placeholder="Type something..." />;
};

export default AutoFocusInput;


🔥 Optimization Tip
useRef does not cause re-renders like useState.
Use it only when you need direct access to a DOM element.


2️⃣ forwardRef - Passing Refs to Child Components
📌 Use forwardRef when you need to pass a ref from a parent to a child functional component.

Example: Parent Controlling Child Input

import React, { useRef, forwardRef } from "react";

// Child Component (Input Box)
const CustomInput = forwardRef((props, ref) => {
  return <input ref={ref} type="text" {...props} />;
});

// Parent Component
const ParentComponent = () => {
  const inputRef = useRef(null);

  const handleFocus = () => {
    inputRef.current.focus(); // Focuses the input field in the child component
  };

  return (
    <div>
      <CustomInput ref={inputRef} placeholder="Click button to focus" />
      <button onClick={handleFocus}>Focus Input</button>
    </div>
  );
};

export default ParentComponent;



🔥 Optimization Tip
If CustomInput did not use forwardRef, the ref would not work on <input>.
Best practice: Use forwardRef when building reusable input components.

3️⃣ useImperativeHandle - Controlling What Parent Can Access

📌 Use useImperativeHandle to expose specific methods instead of the entire ref object.
🔴 Prevents exposing internal child component implementation details to the paren
Example: Exposing Only focus and clear Methods

import React, { useRef, forwardRef, useImperativeHandle } from "react";

// Child Component (Controlled Input)
const CustomInput = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    clear: () => (inputRef.current.value = ""),
  }));

  return <input ref={inputRef} type="text" {...props} />;
});

// Parent Component
const ParentComponent = () => {
  const inputRef = useRef(null);

  return (
    <div>
      <CustomInput ref={inputRef} placeholder="Type here" />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
      <button onClick={() => inputRef.current.clear()}>Clear</button>
    </div>
  );
};

export default ParentComponent;


🔥 Optimization Tip
Without useImperativeHandle, the parent would have access to all input properties.
With it, the parent only gets focus() and clear() methods.

4️⃣ Real-World Use Case: Modal Dialog Using forwardRef and useImperativeHandle


📌 Use forwardRef and useImperativeHandle to control modals/dialogs from a parent component.

Example: Parent Controlling a Modal

import React, { useRef, forwardRef, useImperativeHandle, useState } from "react";

// Child Component (Modal)
const Modal = forwardRef((_, ref) => {
  const [isOpen, setIsOpen] = useState(false);

  useImperativeHandle(ref, () => ({
    open: () => setIsOpen(true),
    close: () => setIsOpen(false),
  }));

  if (!isOpen) return null;

  return (
    <div style={{ position: "fixed", top: "30%", left: "40%", background: "white", padding: "20px", border: "1px solid black" }}>
      <p>This is a modal!</p>
      <button onClick={() => setIsOpen(false)}>Close</button>
    </div>
  );
});

// Parent Component
const ParentComponent = () => {
  const modalRef = useRef(null);

  return (
    <div>
      <button onClick={() => modalRef.current.open()}>Open Modal</button>
      <Modal ref={modalRef} />
    </div>
  );
};

export default ParentComponent;

How it Works?
The parent opens/closes the modal using modalRef.current.open() and modalRef.current.close().
The child does not expose unnecessary state—just the two methods.

🔥 Optimization Tip
This approach makes modals reusable and does not trigger unnecessary re-renders.


🚀 Final Summary Table
Feature	ref (Direct DOM)	forwardRef (Pass Refs)	useImperativeHandle (Expose Methods)
Used For	Directly accessing DOM elements.	Passing refs to child components.	Controlling what is exposed to parent.
Triggers Re-renders?	❌ No	❌ No	❌ No
Use Case	Focus input, animations, scroll.	Allowing parent to control child component.	Exposing only certain functions (focus(), clear()).
Works With	Native elements (input, div).	Functional components.	Functional components.

Using Typescrpit:


4️⃣ Real-World Use Case: Modal with forwardRef & useImperativeHandle
📌 Use useImperativeHandle to control a modal from the parent.

Example: Parent Controls Opening/Closing Modal

import React, { useRef, forwardRef, useImperativeHandle, useState } from "react";

// Define exposed methods
interface ModalRef {
  open: () => void;
  close: () => void;
}

// Child Component (Modal)
const Modal = forwardRef<ModalRef>((_, ref) => {
  const [isOpen, setIsOpen] = useState(false);

  useImperativeHandle(ref, () => ({
    open: () => setIsOpen(true),
    close: () => setIsOpen(false),
  }));

  if (!isOpen) return null;

  return (
    <div style={{ position: "fixed", top: "30%", left: "40%", background: "white", padding: "20px", border: "1px solid black" }}>
      <p>This is a modal!</p>
      <button onClick={() => setIsOpen(false)}>Close</button>
    </div>
  );
});

// Parent Component
const ParentComponent: React.FC = () => {
  const modalRef = useRef<ModalRef>(null);

  return (
    <div>
      <button onClick={() => modalRef.current?.open()}>Open Modal</button>
      <Modal ref={modalRef} />
    </div>
  );
};

export default ParentComponent;

TypeScript Notes
interface ModalRef { open: () => void; close: () => void; } restricts what the parent can access.
Parent cannot access useState directly—only open() and close().



q)
useEffect Cleanup on Unmount (Component Will Unmount in Functional Components)
In React, the cleanup function inside useEffect is executed when a component unmounts or before the effect runs again (when dependencies change).

Why Is Cleanup Needed?
When a component unmounts, any subscriptions, event listeners, or timers inside useEffect should be cleaned up to prevent:

Memory Leaks – Unnecessary resource consumption.
Unexpected Behaviors – Stale references to unmounted components.


How to Perform Cleanup in useEffect
If a function is returned inside useEffect, it runs when the component unmounts or before re-running the effect.
✅ Example: Cleaning Up an Event Listener on Unmount

import React, { useEffect, useState } from "react";

const WindowResize = () => {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", handleResize);

    return () => {
      console.log("Component unmounted, removing event listener");
      window.removeEventListener("resize", handleResize);
    };
  }, []); // Empty dependency array = runs only once on mount/unmount

  return <h1>Window Width: {width}</h1>;
};

export default WindowResize;


Explanation:
window.addEventListener("resize", handleResize) → Adds a listener when the component mounts.
The cleanup function (return () => {...}) → Removes the event listener when the component unmounts.


Unmount Example: Cleaning Up an API Polling Interval
✅ Example: Stopping an Interval When the Component Unmounts


import React, { useEffect, useState } from "react";

const Timer = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCount(prevCount => prevCount + 1);
    }, 1000);

    return () => {
      console.log("Component unmounted, clearing interval");
      clearInterval(interval);
    };
  }, []);

  return <h1>Count: {count}</h1>;
};

export default Timer;


Explanation:
setInterval() starts a timer when the component mounts.
clearInterval(interval) ensures the timer stops when the component unmounts.


When Does Cleanup Happen?
Scenario	When Cleanup Runs
Component Unmounts	useEffect cleanup runs before removal.
Dependency Changes	Cleanup runs before the effect runs again.
Re-renders	No cleanup unless dependencies change.


Common Mistakes
❌ Forgetting Cleanup (Leads to Memory Leaks)

useEffect(() => {
  window.addEventListener("resize", () => console.log(window.innerWidth));
}, []); // No cleanup = Listener stays even after unmounting!


✅ Fix: Add Cleanup
useEffect(() => {
  const handleResize = () => console.log(window.innerWidth);
  window.addEventListener("resize", handleResize);

  return () => window.removeEventListener("resize", handleResize);
}, []);


Conclusion
Always clean up side effects (event listeners, intervals, subscriptions).
Return a function inside useEffect to handle cleanup when unmounting.
Reduces memory leaks & prevents unexpected behaviors.


1. Difference Between useEffect with Different Dependency Arrays
The behavior of useEffect depends on its dependency array ([]):

(a) useEffect(() => {...}, []) → Runs Once (On Mount)
The effect runs only once when the component mounts.
The cleanup function runs on unmount (if provided).
Best for: Fetching data, setting up event listeners, or subscribing to services.
✅ Example: API Call on Mount

useEffect(() => {
  console.log("Component Mounted");
  fetchData();

  return () => console.log("Cleanup on Unmount"); 
}, []); // Runs only once


(b) useEffect(() => {...}) (No Dependency Array) → Runs After Every Render
The effect runs after every render.
Risk: Can cause unnecessary re-renders if state changes inside the effect.
❌ Example: Bad Practice (Infinite Loop)

useEffect(() => {
  setCount(count + 1); // Triggers re-render → useEffect runs again → Infinite loop!
});

✅ Fix: Use Dependencies ([count])
useEffect(() => {
  console.log("Count changed:", count);
}, [count]); // Runs only when `count` changes


(c) useEffect(() => {...}, [dependency]) → Runs When Dependency Changes
The effect runs when the dependency updates.
Best for: Reacting to state/prop changes (e.g., updating data based on user input).
✅ Example: Fetch Data When id Changes

useEffect(() => {
  fetch(`https://api.example.com/user/${id}`)
    .then(res => res.json())
    .then(data => setUser(data));
}, [id]); // Runs only when `id` changes


Summary Table
Dependency Array	When It Runs	Use Case
[] (Empty)	Once on mount	Fetching data, event listeners
No dependency array	Every render	Rarely useful, may cause performance issues
[dependencies]	When dependencies change	Updating state, reacting to prop changes

2. How to Optimize Performance in React Applications?

✅ Best Practices for React Performance Optimization
Optimization Technique	Description
Use useMemo	Caches computed values to prevent unnecessary recalculations.
Use useCallback	Caches functions to avoid unnecessary re-renders in child components.
Use React.memo	Prevents re-renders if props haven't changed.
Lazy Loading (React.lazy())	Loads components only when needed (e.g., for route-based loading).
Code Splitting (React Suspense)	Splits JavaScript into smaller chunks to improve loading speed.
Virtualization (react-window)	Renders only visible items in a long list to improve efficiency.
Optimize Reconciliation (Keys in Lists)	Use unique key props to help React track elements efficiently.
Avoid Unnecessary State Updates	Keep the state minimal and avoid redundant re-renders.


3. Higher-Order Components (HOCs) in React
What Are HOCs?
Higher-Order Components (HOCs) are functions that take a component and return a new enhanced component.
They are used for code reuse, logic sharing, and wrapping components with additional behavior.
🔹 Syntax:

const EnhancedComponent = HOC(WrappedComponent);


✅ Example: HOC for Authentication
Use Case: Protect a page by checking if the user is authenticated.

✅ Step 1: Create an HOC (withAuth)


const withAuth = (Component) => {
  return (props) => {
    const isAuthenticated = localStorage.getItem("token"); // Fake auth check

    return isAuthenticated ? <Component {...props} /> : <h2>Please log in</h2>;
  };
};


✅ Step 2: Use the HOC to Protect a Page

const Dashboard = () => <h1>Welcome to the Dashboard</h1>;
const ProtectedDashboard = withAuth(Dashboard);

const App = () => <ProtectedDashboard />;

🔹 What Happens?

If the user is authenticated, Dashboard is shown.
Otherwise, "Please log in" is displayed

When to Use HOCs?
✅ Best for:

Authentication (withAuth)
Logging (withLogging)
Theme management (withTheme)
Performance optimizations (withMemoization)

HOCs vs. Hooks
Feature	HOCs	Hooks
Syntax	Wraps a component	Used inside components
Use Case	Code reuse via component wrapping	Code reuse via function calls
Complexity	Can get complex with multiple HOCs	Easier to manage


Final Takeaways
useEffect Behavior

[] → Runs once (on mount)
No array → Runs on every render
[dependencies] → Runs when dependencies change
React Performance Optimization

Use useMemo, useCallback, and React.memo
Optimize rendering with virtualization (react-window)
Implement lazy loading (React.lazy)
Higher-Order Components (HOCs)

Wrap components to share logic (e.g., authentication, logging)
Example: withAuth(Component) → EnhancedComponent



1. React Context API: What It Is & How It Works
What is React Context API?
The React Context API allows data to be shared across components without manually passing props at every level (prop drilling).
 It is used for global state management (e.g., themes, authentication, language settings).
 
 
 How React Context Works
It consists of three main parts:

createContext() – Creates a context object.
Provider – Wraps components and provides the data.
Consumer / useContext() – Allows components to access the data.


✅ Example: Using React Context for Theme Management
Step 1: Create Context & Provider (ThemeContext.js)

import React, { createContext, useState } from "react";

const ThemeContext = createContext(); // Create Context

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState("light");

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export default ThemeContext;


Step 2: Use Context in Components (App.js)

import React, { useContext } from "react";
import ThemeContext from "./ThemeContext";

const ThemeButton = () => {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
      Toggle Theme (Current: {theme})
    </button>
  );
};

export default ThemeButton;


🚀 When to Use React Context?

✅ Best for:

Global state (theme, authentication, language settings)
Avoiding prop drilling in deeply nested components


❌ Not Best for:

Large-scale state management → Use Redux instead


2. React Router & Dynamic Routing
What is React Router?
React Router enables navigation between different views in a React app. It allows:

Declarative Routing – Define routes inside components.
Dynamic Routing – Match URL parameters to render different content dynamically.


How to Implement React Router?
✅ Step 1: Install React Router

npm install react-router-dom



✅ Step 2: Set Up Routes (App.js)

import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./Home";
import Profile from "./Profile";

const App = () => (
  <Router>
    <nav>
      <Link to="/">Home</Link>
      <Link to="/profile/123">Profile</Link>
    </nav>

    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/profile/:id" element={<Profile />} />
    </Routes>
  </Router>
);

export default App;


✅ Step 3: Implement Dynamic Routing (Profile.js)

import React from "react";
import { useParams } from "react-router-dom";

const Profile = () => {
  const { id } = useParams(); // Extracts `id` from URL

  return <h1>Profile Page of User {id}</h1>;
};

export default Profile;



🚀 Key Features of React Router
Feature	Description
BrowserRouter	Enables routing in the browser.
Routes	Groups multiple Route components.
Route	Defines a specific path and component.
useParams()	Retrieves URL parameters for dynamic routing.
Link	Used for client-side navigation.



3. Redux: What It Is & How It Works with React
What is Redux?
Redux is a state management library that helps manage global state in large React applications.


How Redux Works
It follows a unidirectional data flow:

Store → Holds global state.
Actions → Define what to do (e.g., "increase counter").
Reducers → Decide how state changes based on actions.
Dispatch → Sends actions to reducers to update the store.

✅ Example: Using Redux in React
Step 1: Install Redux & React-Redux

npm install redux react-redux



Step 2: Create Redux Store (store.js)

import { createStore } from "redux";

// Reducer: Handles state changes
const counterReducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + 1 };
    case "DECREMENT":
      return { count: state.count - 1 };
    default:
      return state;
  }
};

// Create Store
const store = createStore(counterReducer);
export default store;


Step 3: Connect Redux to React (index.js)

import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import store from "./store";
import Counter from "./Counter";

ReactDOM.render(
  <Provider store={store}>
    <Counter />
  </Provider>,
  document.getElementById("root")
);


Step 4: Use Redux State & Dispatch Actions (Counter.js)

import React from "react";
import { useSelector, useDispatch } from "react-redux";

const Counter = () => {
  const count = useSelector(state => state.count); // Get count from store
  const dispatch = useDispatch(); // Dispatch actions

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => dispatch({ type: "INCREMENT" })}>+</button>
      <button onClick={() => dispatch({ type: "DECREMENT" })}>-</button>
    </div>
  );
};

export default Counter;


🚀 When to Use Redux?
✅ Best for:

Large applications with complex state management
Sharing state across multiple components
❌ Not Ideal for:

Small apps → Use Context API instead


1. Server-Side Rendering (SSR) vs. Client-Side Rendering (CSR) in React
What is Server-Side Rendering (SSR)?
SSR (Server-Side Rendering) is a technique where the React application is rendered on the server and sent as a fully-formed HTML page to the browser.
 The browser then hydrates the page with React to make it interactive.
 
 
 
 How SSR Works:
User requests a page → Server processes the request.
Server renders the React components to an HTML string.
HTML is sent to the browser → Fast initial page load.
React hydrates the page → Adds interactivity.


What is Client-Side Rendering (CSR)?
CSR (Client-Side Rendering) is the default in React. 
The browser first downloads a blank HTML page and a JavaScript bundle, then React renders the components on the client.


What is Client-Side Rendering (CSR)?
CSR (Client-Side Rendering) is the default in React. The browser first downloads a blank HTML page and a JavaScript bundle, then React renders the components on the client.

How CSR Works:
User requests a page → Server sends a minimal HTML shell.
Browser downloads the JavaScript bundle and executes it.
React renders the UI dynamically on the client.

SSR vs. CSR: Comparison
Feature	Server-Side Rendering (SSR)	Client-Side Rendering (CSR)
Performance	Faster initial load, but may increase server load	Slower initial load due to JavaScript parsing
SEO	Better SEO (HTML is pre-rendered)	Poor SEO (initially no content for crawlers)
Time to First Paint	Faster (pre-rendered HTML)	Slower (JavaScript must run first)
Interactivity	Requires hydration (slight delay)	Fully interactive once loaded
Best For	SEO-heavy websites, blogs, e-commerce	SPAs (Single Page Applications), dashboards



React is primarily a Client-Side library, meaning it runs in the browser to update the UI dynamically without requiring full-page reloads. However, React can also be used for Server-Side Rendering (SSR) with frameworks like Next.js.

React as a Client-Side Library (CSR - Client-Side Rendering)
React renders components in the browser using JavaScript.
The initial HTML is almost empty and React dynamically updates the UI.
It is great for interactive applications like dashboards and SPAs (Single Page Applications).
🔹 Example of Client-Side React:


import React, { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>Clicked {count} times</button>
  );
};

export default Counter;


📌 Problem with CSR: Poor SEO and slower initial load time.


React Can Be Used for Server-Side Rendering (SSR)
With Next.js, React components can be pre-rendered on the server before being sent to the client.
This improves SEO and initial load speed.
🔹 Example of Server-Side React with Next.js:

import { GetServerSideProps } from "next";

const Page = ({ message }: { message: string }) => {
  return <h1>{message}</h1>;
};

// This function runs on the server before sending HTML to the client
export const getServerSideProps: GetServerSideProps = async () => {
  return { props: { message: "This page is server-side rendered!" } };
};

export default Page;


📌 Benefit of SSR: Faster initial rendering and better SEO.
Final Answer
React alone is a Client-Side library.
With Next.js, React can do Server-Side Rendering (SSR).
React can also support Static Site Generation (SSG) & Hybrid approaches.



✅ Example: Using SSR with Next.js
React doesn’t have built-in SSR, but Next.js makes it easy:

// pages/index.js
export async function getServerSideProps() {
  const data = await fetch("https://api.example.com/posts").then(res => res.json());
  return { props: { data } };
}

const Home = ({ data }) => {
  return (
    <div>
      <h1>Server-Side Rendered Page</h1>
      <ul>
        {data.map(post => <li key={post.id}>{post.title}</li>)}
      </ul>
    </div>
  );
};

export default Home;


2. React Suspense and Concurrent Mode
What is React Suspense?


React Suspense is a feature that lets components "wait" for data before rendering. 
Instead of showing a blank screen, it displays a fallback UI until the data is loaded.

✅ Example: Suspense with Lazy Loading

import React, { Suspense, lazy } from "react";

const LazyComponent = lazy(() => import("./LazyComponent"));

const App = () => (
  <Suspense fallback={<h1>Loading...</h1>}>
    <LazyComponent />
  </Suspense>
);

export default App;


Here, <LazyComponent /> is loaded only when needed, improving performance.

What is Concurrent Mode?
Concurrent Mode improves rendering by allowing React to work in the background without blocking the UI.

Key Features of Concurrent Mode:

Automatic Interruptions: React can pause rendering and resume later.
Better User Experience: Keeps UI responsive while processing large updates.
useTransition() Hook: Controls rendering priority.

✅ Example: Using useTransition() for Smooth UI

import React, { useState, useTransition } from "react";

const App = () => {
  const [input, setInput] = useState("");
  const [isPending, startTransition] = useTransition();

  const handleChange = (e) => {
    setInput(e.target.value);

    // Run heavy computation in background
    startTransition(() => {
      // Simulate filtering large dataset
      console.log("Filtering data...");
    });
  };

  return (
    <div>
      <input type="text" value={input} onChange={handleChange} />
      {isPending && <p>Loading...</p>}
    </div>
  );
};

export default App;

Here, startTransition() ensures React prioritizes input updates over filtering, keeping the UI responsive


3. React Fiber: The New Reconciliation Algorithm
What is React Fiber?
React Fiber is a complete rewrite of React’s rendering engine (introduced in React 16) that improves performance by:

Breaking rendering into small tasks → Allows React to pause & resume rendering.
Prioritizing updates → Important updates (e.g., user input) render faster.
Concurrency support → Enables features like Suspense & Concurrent Mode.


How React Fiber Works?
Instead of processing the entire React tree at once, Fiber splits it into units of work and processes them asynchronously.

Key Benefits of React Fiber: ✅ Time-slicing – Avoids UI freezes by breaking rendering into small chunks.
✅ Interruptible Rendering – Can pause rendering to prioritize user interactions.
✅ Concurrency Support – Enables features like Suspense and Concurrent Mode.


✅ Example: How React Fiber Optimizes Rendering
Before Fiber (React 15) – Blocking Updates
React would synchronously render the entire tree.
Large updates blocked UI, causing lag.
With Fiber (React 16+) – Non-blocking Updates
React pauses rendering for high-priority updates (e.g., button clicks).
Background tasks continue without freezing the UI.


🚀 Summary
Feature	React Fiber (React 16+)	Old Reconciliation (React 15)
Rendering	Asynchronous (interruptible)	Synchronous (blocking)
Performance	Faster UI updates	Slower rendering
User Experience	Prioritizes interactivity	UI can freeze
Concurrency	Supports Suspense & Concurrent Mode	No concurrency



🚀 Final Takeaways
SSR (Server-Side Rendering) vs. CSR (Client-Side Rendering):

SSR is better for SEO and faster initial loads.
CSR is better for rich, interactive SPAs.
React Suspense & Concurrent Mode:

Suspense delays rendering until data is ready.
Concurrent Mode keeps UI responsive by scheduling updates efficiently.
React Fiber (React 16+):

Allows non-blocking rendering, making React apps faster & smoother.


2. useReducer vs. useState – When to Use Each?
Feature	useState	useReducer
Complexity	Simple state logic	Complex state logic
Data Management	One or few state variables	Multiple state values
State Updates	Direct state updates	Uses a reducer function
Best For	Simple forms, toggles, counters	Forms, authentication, state logic with multiple actions


🔹 useState – Simple State Management
Best for basic states like toggles, counters, or form inputs.

✅ Example: Using useState

import React, { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}



🔹 useReducer – Complex State Management
Best for complex states with multiple related variables.

✅ Example: Using useReducer


import React, { useReducer } from "react";

// Reducer function
const reducer = (state, action) => {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    case "reset":
      return { count: 0 };
    default:
      return state;
  }
};

export default function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
      <h2>Count: {state.count}</h2>
      <button onClick={() => dispatch({ type: "increment" })}>Increment</button>
      <button onClick={() => dispatch({ type: "decrement" })}>Decrement</button>
      <button onClick={() => dispatch({ type: "reset" })}>Reset</button>
    </div>
  );
}


🔹 Why useReducer?

Works better when state transitions depend on previous state.
More readable & maintainable for complex state logic.



1. Creating a Custom Hook (useCounter)
Let's create a custom hook to manage a counter.

Custom Hook: useCounter.js

import { useState } from "react";

function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);

  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);
  const reset = () => setCount(initialValue);

  return { count, increment, decrement, reset };
}

export default useCounter;


Using the Custom Hook in a Component

import React from "react";
import useCounter from "./useCounter";

function CounterComponent() {
  const { count, increment, decrement, reset } = useCounter(5); // Start at 5

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}

export default CounterComponent;



✅ Reusability: The hook can be used in multiple components.
✅ Encapsulated Logic: The state management logic is inside useCounter.

2. Custom Hook for Fetching API Data (useFetch)
A custom hook to fetch data from an API.

Custom Hook: useFetch.js


import { useState, useEffect } from "react";

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Failed to fetch data");
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error };
}

export default useFetch;


Using the Custom Hook in a Component
import React from "react";
import useFetch from "./useFetch";

function Posts() {
  const { data, loading, error } = useFetch("https://jsonplaceholder.typicode.com/posts");

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {data.slice(0, 5).map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}

export default Posts;


✅ Encapsulates API fetching logic
✅ Reusable for any API endpoint

3. Custom Hook for Managing Local Storage (useLocalStorage)
This custom hook stores and retrieves data from localStorage.



Custom Hook: useLocalStorage.js
import { useState, useEffect } from "react";

function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(storedValue));
  }, [key, storedValue]);

  return [storedValue, setStoredValue];
}

export default useLocalStorage;



Using the Custom Hook in a Component
import React from "react";
import useLocalStorage from "./useLocalStorage";

function ThemeSwitcher() {
  const [theme, setTheme] = useLocalStorage("theme", "light");

  return (
    <div>
      <p>Current Theme: {theme}</p>
      <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
        Toggle Theme
      </button>
    </div>
  );
}

export default ThemeSwitcher;


✅ Persists state even after page reloads
✅ Can be used for saving user preferences

4. Custom Hook for Debouncing Input (useDebounce)
This custom hook delays updating a value until after a certain period.

Custom Hook: useDebounce.js
import { useState, useEffect } from "react";

function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
}

export default useDebounce;


Using the Custom Hook in a Search Component

import React, { useState } from "react";
import useDebounce from "./useDebounce";

function SearchBar() {
  const [searchTerm, setSearchTerm] = useState("");
  const debouncedSearchTerm = useDebounce(searchTerm, 500);

  return (
    <div>
      <input
        type="text"
        placeholder="Search..."
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <p>Searching for: {debouncedSearchTerm}</p>
    </div>
  );
}

export default SearchBar;



✅ Prevents excessive API calls while typing

5. Custom Hook for Window Size (useWindowSize)

Tracks the window size dynamically.

Custom Hook: useWindowSize.js
import { useState, useEffect } from "react";

function useWindowSize() {
  const [size, setSize] = useState({ width: window.innerWidth, height: window.innerHeight });

  useEffect(() => {
    const handleResize = () => {
      setSize({ width: window.innerWidth, height: window.innerHeight });
    };

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return size;
}

export default useWindowSize;



Using the Custom Hook in a Component
import React from "react";
import useWindowSize from "./useWindowSize";

function WindowTracker() {
  const { width, height } = useWindowSize();

  return (
    <p>Window Size: {width} x {height}</p>
  );
}

export default WindowTracker;


You need to display the thumbnail as an image rather than just printing its URL as text.
 Modify the <td>{products.thumbnail}</td> part by wrapping the URL in an <img> tag. Here's the corrected code:
 
 import React, { useEffect, useState } from 'react';
import './style.css';

export default function App() {
  const [data1, setData] = useState([]);

  useEffect(() => {
    fetch('https://dummyjson.com/products')
      .then((res) => res.json())
      .then((data) => {
        console.log(data.products, '---->22');
        setData(data.products);
      });
  }, []);

  console.log(data1, '---->');
  return (
    <div>
      <table border="1">
        <thead>
          <tr>
            <th>Brand</th>
            <th>Title</th>
            <th>Price</th>
            <th>Thumbnail</th>
          </tr>
        </thead>
        <tbody>
          {data1 &&
            data1.map((product) => (
              <tr key={product.id}>
                <td>{product.brand}</td>
                <td>{product.title}</td>
                <td>${product.price}</td>
                <td>
                  <img
                    src={product.thumbnail}
                    alt={product.title}
                    width="50"
                    height="50"
                  />
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}

Fixes & Improvements:
Added a key prop: React requires a unique key when rendering lists (key={product.id}).
Displayed the thumbnail properly: Used <img> with src={product.thumbnail}.
Set image dimensions: Used width="50" and height="50" for better display.
Defaulted useState to an empty array ([]): Prevents map from running on undefined

























