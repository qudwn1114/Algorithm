var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

let answer = 0;

for(let i=0; i<5; i++){
    let temp = input[i].trim().split(' ');
    let start = temp[0].split(':');
    let end = temp[1].split(':');

    answer += (parseInt(end[0]) * 60 + parseInt(end[1])) - (parseInt(start[0]) * 60 + parseInt(start[1]));
}

console.log(answer);