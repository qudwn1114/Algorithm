var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

let x = parseInt(input[1].split(' ')[0])
let y = parseInt(input[1].split(' ')[1])

for(let i=1; i<=parseInt(input[0]); i++){
    let temp = input[i].split(' ')
    if(y > parseInt(temp[1])){
        x = parseInt(temp[0]);
        y = parseInt(temp[1]);
    }
}

console.log(x, y);