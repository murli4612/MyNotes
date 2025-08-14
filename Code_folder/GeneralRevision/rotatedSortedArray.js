// function rotatedSortedArraySearch(arrayA, target){

//     let low = 0
//     let high = arrayA.length - 1

//     while (low <= high){
//         let mid = Math.floor((low + high) / 2);

//         if (arrayA[mid]=== target){
//             return mid
//         }
//         // left sorted part
//         if (arrayA[low] <= arrayA[mid]){

//             if(target >= arrayA[low] && target < arrayA[mid]){
//                 high = mid - 1

//             }
//             else{
//                 low = mid + 1
//             }

//         }
//         // right sorted part
//         else
//         {
//            if (target > arrayA[mid] &&  target <= arrayA[high]){
//             low = mid + 1
//            }
//            else{
//             high = mid - 1
//            }
//         }
//     }
//     return -1



// }

// // input  = [4, 5, 6,7,1,2,3]

// // console.log(roatedSortedArraySearch(input,4))

// let input = [4, 5, 6, 7, 1, 2, 3];
// console.log(rotatedSortedArraySearch(input, 4));  // Output: 0
// console.log(rotatedSortedArraySearch(input, 2));  // Output: 5
// console.log(rotatedSortedArraySearch(input, 9));  // Output: -1





function rotatedSortedArraySearchD(arrayA, target) {
    let low = 0;
    let high = arrayA.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);

        // ✅ Found target
        if (arrayA[mid] === target) return true;

        // ⚠ Handle duplicates — skip them
        if (arrayA[low] === arrayA[mid] && arrayA[mid] === arrayA[high]) {
            low++;
            high--;
        }
        // \U0001f50d Left side is sorted
        else if (arrayA[low] <= arrayA[mid]) {
            if (arrayA[low] <= target && target < arrayA[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        // \U0001f50d Right side is sorted
        else {
            if (arrayA[mid] < target && target <= arrayA[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }

    return false;
}

// input  = [4, 5, 6,7,1,2,3]

// console.log(roatedSortedArraySearch(input,4))

let input = [4, 5, 6, 7,7, 1, 2, 3];
console.log(rotatedSortedArraySearchD(input, 7));  // Output: 0
console.log(rotatedSortedArraySearchD(input, 2));  // Output: 5
console.log(rotatedSortedArraySearchD(input, 9));  // Output: -1
