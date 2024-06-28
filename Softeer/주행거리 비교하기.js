var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

let a = parseInt(input[0]);
let b = parseInt(input[1]);
if(a > b){
    console.log('A');
}
else if (a < b){
    console.log('B');
}
else{
    console.log('same');
}