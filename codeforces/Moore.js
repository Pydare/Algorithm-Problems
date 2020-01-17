function findSmallestNumber(arr) {
    let max = 0;
    let maxTwo = 0;
    for (let i = 0; i < max.length; i++) {
        max = Math.max(max, arr[i]);
    }

    for (let i = 0; i < max.length; i++) {
        if (arr[i] === max) continue;
        maxTwo = Math.max(max, arr[i]);
    }

    return maxTwo
}

const testCaseOne = [1,2,3,4,5,6,7]

console.log(findSmallestNumber(testCaseOne))