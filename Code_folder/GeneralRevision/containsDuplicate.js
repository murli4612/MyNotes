function duplicateContains(numbers){
   let  mySet = new Set()

    for(let num of numbers){
        if (mySet.has(num)) {
            return [true ,num]
        }
        else{
            mySet.add(num)
        }
    }
    return false
}

Input = [1,2,3,3,9]
console.log(duplicateContains(Input))