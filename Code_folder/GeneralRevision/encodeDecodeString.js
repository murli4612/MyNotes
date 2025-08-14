
function encodeString(strings) {
    let res = "";
    for (let i = 0; i < strings.length; i++) {
        res += strings[i].length + "#" + strings[i];
    }
    return res;
}

function decodeString(string){

    const stack = []
    let i = 0
    while (i < string.length){
        let k = ""
        while (i < string.length && string[i] != '#' ){
            k = k + string[i]
            i ++
        }
        i +=1
        const length = parseInt(k)
        // const word = string.slice(i, i + length);
        // stack.push(word);
        stack.push(string.slice(i, i + length))
        i +=length
    }
    return stack
}


// function decodeString(string) {
//     const stack = [];
//     let i = 0;

//     while (i < string.length) {
//         let k = "";
//         // Read number (length of the string)
//         while (i < string.length && string[i] !== '#') {
//             k += string[i];
//             i++;
//         }

//         i++; // Skip the '#'

//         const length = parseInt(k);
//         const word = string.slice(i, i + length);
//         stack.push(word);
//         i += length;
//     }

//     return stack.join('');
// }

const input = ["lint", "code", "love", "you"];
const output = encodeString(input);
console.log(output);  // Output: 4#lint4#code4#love3#you

const decoded = decodeString(output);
console.log("Decoded:", decoded);  // Output: "lintcodeloveyou"
