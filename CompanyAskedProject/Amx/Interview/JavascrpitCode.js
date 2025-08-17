// const map = new Map();

// // Setting key-value pairs
// map.set("name", "Alice");
// map.set("age", 30);
// map.set(42, "answer");
// map.set({ key: "obj" }, "object value");

// // Iterating
// for (const [key, value] of map) {
//   console.log(`${key}: ${value}`);
// }

// // Deleting
// map.delete("age");
// map.clear();  // Removes all entries

  
function removeCharFromStringCompareWithOther(stringA, removeString) {
    const removeDict = {};
    const result = [];
    
    for (const char of removeString.toLowerCase()) {
        removeDict[char] = (removeDict[char] || 0) + 1;
    }
    
    for (const char of stringA) {
        if (char in removeDict) {
            continue;
        } else {
            result.push(char);
        }
    }
    
    return result.join('');
}

console.log(removeCharFromStringCompareWithOther("careermonkc", "ec"));