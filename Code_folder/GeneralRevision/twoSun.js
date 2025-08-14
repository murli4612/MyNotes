function twoSum(nums, target) {
    const myMap = new  Map()

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (myMap.has(complement)) {
            return [myMap.get(complement), i];
        }

        myMap.set(nums[i], i);
    }

    return null; // if no pair found
}

const input = [2, 7, 11, 15];
const target = 17;
const output = twoSum(input, target);
console.log(output); // Output: [0, 3]


function twoSum1(nums, target) {
    const myMap = {};  // plain object

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        // if (myMap.hasOwnProperty(complement)) {
        //     console.log(myMap)
        //     return [myMap[complement], i];
        // }

        if (Object.hasOwn(myMap, complement)) {
            console.log(myMap)
            return [myMap[complement], i];
        }

        myMap[nums[i]] = i;  // set key-value
    }
    // console.log(myMap)
    return null;
}

const output1 = twoSum1(input, target);
console.log(output1); // Output: [0, 3]

