// 1️⃣  Define the User object type
type User = {
  id: number;              // unique identifier
  username: string;        // login name
  fullName: string;
  email: string;
  isActive: boolean;
  roles: string[];         // e.g., ["admin", "editor"]
  // Optional nested object
  address?: {
    street: string;
    city: string;
    postalCode: string;
  };
};

// 2️⃣  Create a concrete object that satisfies the User type
const myUser: User = {
  id: 1,
  username: "murli.m",
  fullName: "Murli Manohar",
  email: "murli@example.com",
  isActive: true,
  roles: ["admin", "developer"],
  address: {
    street: "221B Baker Street",
    city: "London",
    postalCode: "NW1 6XE",
  },
};

// 3️⃣  (Optional) Example usage
console.log(myUser.fullName);          // "Murli Manohar"
console.log(myUser.roles.includes("admin")); // true
