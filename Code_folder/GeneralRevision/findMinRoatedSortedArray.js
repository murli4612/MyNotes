function findMinRSA(arrayA){
    let low = 0
    let high = arrayA.length - 1
    while (low < high){
         let mid = Math.floor((low + high) / 2);

        if (arrayA[mid] > arrayA[high]){
            low = mid + 1
        }
        else{
            high = mid
        }
    }
    return arrayA[low]
}

const Input = [4,6,1,2,3]
result = findMinRSA(Input)

console.log(result)

// ✅ Time & Space Complexity:
// Time: O(log n)

// Space: O(1)


function findMinWithDuplicates(arr) {
    let low = 0;
    let high = arr.length - 1;

    while (low < high) {
        let mid = Math.floor((low + high) / 2);

        if (arr[mid] > arr[high]) {
            low = mid + 1;
        } else if (arr[mid] < arr[high]) {
            high = mid;
        } else {
            // arr[mid] === arr[high], can't decide, shrink safely
            high--;
        }
    }

    return low; // index of minimum element
}

const input = [2, 2, 2, 0, 1, 2];
const index = findMinWithDuplicates(input);
console.log("Minimum with duplicates:", input[index]); // 0
console.log("Index:", index);                          // 3
