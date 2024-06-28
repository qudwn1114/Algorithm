var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

let arr = input.map(Number);

let result = 'mixed';
if(arr[0] == 1 && arr[7] == 8){
    result = 'ascending';
    for(let i=0; i<7; i++){
        if(arr[i+1] - arr[i] != 1){
            result = 'mixed';
            break;
        }
    }
}
else if(arr[0] == 8 && arr[7] == 1){
    result = 'descending';
    for(let i=0; i<7; i++){
        if(arr[i] - arr[i+1] != 1){
            result = 'mixed';
            break;
        }
    }
}

console.log(result);