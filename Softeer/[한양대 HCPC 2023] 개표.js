var fs = require('fs'); 
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(input[0]);
let arr = [];
for(let i=1; i<=T; i++){
    arr.push(parseInt(input[i]));
}

for(let i=0; i<arr.length; i++){
    let str = ''
    str += '++++ '.repeat(parseInt(arr[i] / 5));
    str += '|'.repeat(arr[i] % 5);
    console.log(str.trim());
}