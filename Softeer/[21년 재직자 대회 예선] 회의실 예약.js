var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(input[0].split(' ')[0]);
const M = parseInt(input[0].split(' ')[1]);

let room = {};
let room_list = [];
for(let i=1; i<=N; i++){
    room_list.push(input[i]);
    room[input[i]] = [0, 0, 0, 0, 0, 0, 0, 0, 0];
}
room_list.sort();

for(let i=N+1; i<=N+M; i++){
    let room_name = input[i].split(' ')[0];
    let start = parseInt(input[i].split(' ')[1]);
    let end = parseInt(input[i].split(' ')[2]);
    for(let j=0; j<end-start; j++){
        room[room_name][start - 9 + j] = 1;
    }
}

for(let i=0; i<N; i++){
    console.log(`Room ${room_list[i]}:`);
    let arr = [];
    let idx = 0;
    let cnt = 0;
    
    for(let j=0; j<9; j++){
        if(room[room_list[i]][j] == 0){
            if(cnt == 0){
                idx = j;
            }
            cnt += 1;
        }
        else{
            if(cnt > 0){
                arr.push([idx, cnt]);
                idx = 0;
                cnt = 0;
            }
        }
    }
    if(cnt > 0){
        arr.push([idx, cnt]);
        idx = 0;
        cnt = 0;
    }

    if(arr.length == 0){
        console.log("Not available");
    }
    else{
        console.log(`${arr.length} available:`);
        for(let j=0; j<arr.length; j++){
            let start = arr[j][0] + 9;
            let end = start + arr[j][1];
            console.log(`${zeroFillStr(start)}-${zeroFillStr(end)}`);
        }
    }
    
    if(i != N-1){
        console.log("-----");
    }
}

function zeroFillStr(n){
    let str = n.toString();
    if(str.length == 1){
        str = '0' + str;
    }
    return str;
}
