var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const light = [
    [1, 1, 0, 1, 1, 1, 1], 
    [0, 1, 0, 1, 0, 0, 0], 
    [1, 1, 1, 0, 1, 1, 0], 
    [1, 1, 1, 1, 1, 0, 0], 
    [0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
];

const T = parseInt(input[0]);

for(let i=1; i<=T; i++){
    let a = input[i].split(' ')[0];
    let b = input[i].split(' ')[1];
    a = ' '.repeat(5 - a.length) + a;
    b = ' '.repeat(5 - b.length) + b;
    let result = 0;
    for(let j=0; j<5; j++){
        if(a[j] != b[j]){
            if(a[j] == ' '){
                result += countBtn(parseInt(b[j]));
            }
            else if(b[j]==' '){
                result += countBtn(parseInt(a[j]));
            }
            else{
                result += compareBtn(parseInt(a[j]), parseInt(b[j]));
            }
        }
    }    
    console.log(result);
}

function compareBtn(a, b){
    let cnt = 0;
    for(let i=0; i<7; i++){
        if(light[a][i] != light[b][i]){
            cnt += 1;
        }
    }
    return cnt;
}

function countBtn(x){
    let cnt = 0;
    for(let i=0; i<7; i++){
        if(light[x][i] == 1){
            cnt += 1;
        }
    }
    return cnt;
}