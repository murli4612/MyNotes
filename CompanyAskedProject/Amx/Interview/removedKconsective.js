function removeKconcestive(stringA, k){
    stack = []

    for (char of stringA){
        if(stack.length && stack[stack.length - 1][0]  === char ){
            stack[stack.length - 1][1]  = stack[stack.length - 1][1]  + 1
        }
        else{
            stack.push([char,1])
        }
         if (stack[stack.length - 1][1] === k) {
            stack.pop()
        }

        
    }
    return stack.map(([ch, n]) => ch.repeat(n)).join('')
}
stringA = 'deeedbbcccbdaa'
k = 3
console.log(removeKconcestive(stringA, k))

/**
 * Remove any k‑length run of the same character, repeatedly, until
 * the string is stable.
 *
 * @param {string} s  – input string
 * @param {number} k – run length to delete
 * @returns {string}  – cleaned string
 */
function removeKConsecutive(s, k) {
  const stack = [];            // [[char, count], …]

  for (const ch of s) {
    // If top of stack has the same char, bump its count
    if (stack.length && stack[stack.length - 1][0] === ch) {
      stack[stack.length - 1][1] += 1;
    } else {
      stack.push([ch, 1]);
    }

    // If we’ve reached k, drop that run
    if (stack[stack.length - 1][1] === k) {
      stack.pop();
    }
  }

  // Reconstruct the final string
  return stack
    .map(([ch, cnt]) => ch.repeat(cnt))
    .join('');
}

// Demo
const stringA = 'deeedbbcccbdaa';
const k = 3;
console.log(removeKConsecutive(stringA, k)); // "aa"
