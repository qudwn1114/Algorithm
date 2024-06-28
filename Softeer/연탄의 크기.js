var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0]);
let arr = input[1].trim().split(' ');
arr.map(Number);
arr.sort(function(a,b){
    return a-b;
});

let max_cnt = 1;
let r = 2;
while(true){
    if(r > arr[n-1]){
        break;
    }
    let cnt = 0;
    for(let i =0; i<n; i++){
        if(arr[i] % r == 0){
            cnt+=1;
        }
    }
    if(max_cnt < cnt){
        max_cnt = cnt;
    }
    if(max_cnt == n){
        break;
    }
    r+=1;
}

console.log(max_cnt);