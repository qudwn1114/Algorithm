var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const M = parseInt(input[0].split(' ')[0]);
const N = parseInt(input[0].split(' ')[1]);
const K = parseInt(input[0].split(' ')[2]);

let MList = input[1].trim().split(' ');
let MStr = '';
for(let i=0; i<M; i++){
    MStr += MList[i];
}

let NList = input[2].trim().split(' ');
let NStr = '';
for(let i=0; i<N; i++){
    NStr += NList[i];
}

if(NStr.includes(MStr)){
    console.log('secret');
}
else{
    console.log('normal');
}