function threeSum(nums) {
    let res = [];
    nums.sort((a, b) => a - b);  // Sort the array

    const length = nums.length;

    for (let i = 0; i < length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;  // Skip duplicate values for i
        }

        let l = i + 1;
        let r = length - 1;

        while (l < r) {
            const total = nums[i] + nums[l] + nums[r];

            if (total < 0) {
                l++;
            } else if (total > 0) {
                r--;
            } else {
                res.push([nums[i], nums[l], nums[r]]);

                // Skip duplicates for l and r
                while (l < r && nums[l] === nums[l + 1]) l++;
                while (l < r && nums[r] === nums[r - 1]) r--;

                l++;
                r--;
            }
        }
    }

    return res;
}


const input = [-1, 0, 1, 2, -1, -4];
console.log(threeSum(input));
// Output: [[-1, -1, 2], [-1, 0, 1]]
