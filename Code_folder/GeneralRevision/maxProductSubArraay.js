function maxProductArray(numbers){
    let res = Math.max(...numbers);
    let currMax = 1
    let currMin = 1
    for (let num of numbers){
        if (num === 0){
            currMax = 1
            currMin = 1
            continue
        }
        let temp = num * currMax
        currMax = Math.max(num, num * currMax, num * currMin)
        currMin = Math.min(num, num *currMin, temp)
        res = Math.max(res, currMax)
    }
    return res
}

input = [-1,-2,-3,-4]
result = maxProductArray(input)

console.log(result)

// ✅ Time & Space Complexity:
// Time: O(n)

// Space: O(1)