var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString();

const N = parseInt(input);

console.log((2**N + 1) ** 2)