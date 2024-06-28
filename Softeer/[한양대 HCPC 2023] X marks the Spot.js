var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = parseInt(input[0]);
let result = '';

for(let i=1; i<=n; i++){
    let a = input[i].split(' ')[0].trim();
    let b = input[i].split(' ')[1].trim();
    let idx = 0;
    for(let j=0; j<a.length; j++){
        if(a[j]=='x' || a[j] == 'X'){
            idx = j;
            break;
        }
    }
    result += b[idx].toUpperCase();
}

console.log(result);