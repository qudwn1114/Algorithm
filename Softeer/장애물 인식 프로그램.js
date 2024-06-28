var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(input[0]);
let arr = [];
var cnt = 0;
let result = [];

// 지도 배열 초기화
for(let i=1; i<=N; i++){
    let temp = input[i].trim().split('');
    temp.map(Number);
    arr.push(temp);
}

for(let i=0; i<N; i++){
    for(let j=0; j<N; j++){
        if(arr[i][j] == 1){
            cnt = 0;
            countBlock(i, j);
            result.push(cnt);
        }
    }
}

result.sort(function(a,b){
    return a - b;
})

console.log(result.length);
for(let i=0; i<result.length; i++){
    console.log(result[i]);
}


function countBlock(x, y){
    arr[x][y] = 0;
    cnt += 1;
    //위 체크
    if(x-1 >=0){
        if(arr[x-1][y] == 1){
            countBlock(x-1, y);
        }
    }
    //아래 체크
    if(x+1 <= N-1){
        if(arr[x+1][y] == 1){
            countBlock(x+1, y);
        }
    }
    //왼쪽 체크
    if(y-1 >= 0){
        if(arr[x][y-1] == 1){
            countBlock(x, y-1);
        }
    }
    //오른쪽 체크
    if(y+1 <= N-1){
        if(arr[x][y+1] == 1){
            countBlock(x, y+1);
        }
    }
}
