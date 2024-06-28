var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(input[0].trim().split(' ')[0]);
const M = parseInt(input[0].trim().split(' ')[1]);

let limit = [];
let test = [];
let result = 0;

//배열 초기화
for(let i=1; i<=N; i++){
    let temp = input[i].trim().split(' ');
    for(let j=0; j<parseInt(temp[0]); j++){
        limit.push(parseInt(temp[1]));
    }
}


for(let i=N+1; i<=N+M; i++){
    let temp = input[i].trim().split(' ');
    for(let j=0; j<parseInt(temp[0]); j++){
        test.push(parseInt(temp[1]));
    }
}

for(let i=0; i<100; i++){
    let diff = test[i] - limit[i];
    if(diff > result){
        result = diff;
    }
}
console.log(result);