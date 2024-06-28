var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

let K = BigInt(input[0]);
let P = BigInt(input[1]);
let N = BigInt(input[2]);

for(let i=0; i<N; i++){
    K *= P;
    K = K % BigInt(1000000007)
}

console.log(parseInt(K));