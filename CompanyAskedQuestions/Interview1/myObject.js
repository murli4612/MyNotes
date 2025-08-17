// 2️⃣  Create a concrete object that satisfies the User type
var myUser = {
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
console.log(myUser.fullName); // "Murli Manohar"
console.log(myUser.roles.includes("admin")); // true
