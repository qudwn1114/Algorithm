var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

let a = parseInt(input[0]);
let b = parseInt(input[1]);
let d = parseInt(input[2]);

let move = 0;
let result = 0;
let touch = false;
let run = true;

while(move < d*2){
    // 터치 전
    if(!touch){
        //움질일때
        if(run){
            for(let i=0; i<a; i++){
                move += 1;
                result += 1;
                if(move == d){
                    touch = true;
                    break;
                }
            }
            if(touch){
                run = true;
            }
            else{
                run = false;
            }
        }
        else{
            for(let i=0; i<b; i++){
                result += 1;
            }
            run = true;
        }
    }
    else{
        if(run){
            for(let i=0; i<b; i++){
                move += 1;
                result += 1;
                if(move == d * 2){
                    break;
                }
            }
            run = false;
        }
        else{
            for(let i=0; i<a; i++){
                result += 1;
            }
            run = true
        }
    }
}

console.log(result);