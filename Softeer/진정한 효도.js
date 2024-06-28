var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

let arr = [];
let result = 2;

for(let i=0; i<3; i++){
    let temp = input[i].trim().split(' ');
    temp.map(Number);
    arr.push(temp);
}

for(let i=0; i<3; i++){
    //가로체크
    let a = arr[i][0];
    let b = arr[i][1];
    let c = arr[i][2];
    if(a == b && b == c){
        result = 0;
        break;
    }
    if(result == 2){
        if(a==b){
            if(Math.abs(b-c) < result){
                result = 1;
            }
        }
        if(b==c){
            if(Math.abs(c-a) < result){
                result = 1;
            }
        }
        if(c==a){
            if(Math.abs(a-b) < result){
                result = 1;
            }
        }
    }
    //세로체크
    a = arr[0][i];
    b = arr[1][i];
    c = arr[2][i];
    if(a == b && b == c){
        result = 0;
        break;
    }
    if(result == 2){
        if(a==b){
            if(Math.abs(b-c) < result){
                result = 1;
            }
        }
        if(b==c){
            if(Math.abs(c-a) < result){
                result = 1;
            }
        }
        if(c==a){
            if(Math.abs(a-b) < result){
                result = 1;
            }
        }
    }
}

console.log(result);