var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n  = parseInt(input[0]);
let arr = input[1].trim().split(' '); // 입력값 끝에 공백제거 안해서 삽질 !!!!!!!!!!!!!!!!
arr = arr.map(Number);

arr.sort(function(a, b){
    return a - b;
})

console.log(Math.max(arr[0] * arr[1], arr[n-2] * arr[n-1]))