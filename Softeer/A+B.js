var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = parseInt(input[0]);
for(let i=1; i<=n; i++){
    let temp = input[i].trim().split(' ');
    console.log(`Case #${i}: ${parseInt(temp[0]) + parseInt(temp[1])}`);
}