var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

let W = parseInt(input[0].trim().split(' ')[0]);
let N = parseInt(input[0].trim().split(' ')[1]);

let result = 0;
let bag = W;

arr = [];
for(let i=1; i<=N; i++){
    let temp = input[i].trim().split(' ');
    temp.map(Number)
    arr.push(temp);
}
arr.sort(function(a, b){
    return b[1] - a[1];
})

for(let i=0; i<N; i++){
    if(bag >= arr[i][0]){
        bag -= arr[i][0];
        result += arr[i][0] * arr[i][1];
    }
    else{
        result += bag * arr[i][1];
        break;
    }
}
console.log(result);