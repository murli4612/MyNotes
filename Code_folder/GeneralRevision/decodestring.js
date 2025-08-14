function isDigit(str) {

    // This checks if a single character is a digit (0-9).
    // ^\d$ ensures it matches exactly one digit, not multiple
    return /^\d$/.test(str);
}

function decodeString(stringA) {
    let stack = [];

    for (let i = 0; i < stringA.length; i++) {
        if (stringA[i] !== ']') {
            stack.push(stringA[i]);
        } else {
            // Extract the substring inside the brackets
            let subStr = "";
            while (stack.length > 0 && stack[stack.length - 1] !== '[') {
                subStr = stack.pop() + subStr;
            }

            // Pop the '[' from the stack
            stack.pop();

            // Extract the number (k)
            let k = "";
            while (stack.length > 0 && isDigit(stack[stack.length - 1])) {
                k = stack.pop() + k;
            }

            // Repeat the substring and push back to stack
            stack.push(subStr.repeat(parseInt(k)));
        }
    }

    return stack.join('');
}

const input = "3[a]2[bc]";
console.log(decodeString(input));  // Output: "aaabcbc"
