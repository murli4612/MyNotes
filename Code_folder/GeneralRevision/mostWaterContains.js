function mostWaterContains(arrayA){
    let res = 0

    let l =0
    let r = arrayA.length -1
    while (l < r){
        let area =  (r -l) * Math.min(arrayA[l], arrayA[r])
        res = Math.max(res, area)
        if (arrayA[l] < arrayA[r]){
            l++
        }
        else{
            r--
        }
    }
    return res
}

const height = [1,8,6,2,5,4,8,3,7]
console.log(mostWaterContains(height))