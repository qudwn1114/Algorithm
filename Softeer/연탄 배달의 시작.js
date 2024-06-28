var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');
let n = parseInt(input[0])
let arr = input[1].split(' ');

let min = 0;
let result = [];

for(let i=0; i<n-1; i++){
    if(result.length == 0){
        min = parseInt(arr[i+1]) - parseInt(arr[i]);
        result.push([arr[i], arr[i+1]]);
    }
    else{
        let temp = parseInt(arr[i+1]) - parseInt(arr[i])
        if(temp < min){
            min = temp;
            result = [[arr[i], arr[i+1]]];
        }
        else if (temp == min){
            result.push([arr[i], arr[i+1]]);
        }        
    }
}

console.log(result.length);