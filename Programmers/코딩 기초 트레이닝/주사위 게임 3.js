function solution(a, b, c, d) {
    var answer = 0;
    let arr = [a, b, c, d];
    arr.sort(function(a,b){
        return a - b;
    })
    
    let n = countElem(arr, arr[0])
    
    if(n == 4){
        answer = arr[0] * 1111;
    }
    else if(n == 3){
        let p = arr[0];
        let q = 0;
        for(let i =0; i<arr.length; i++){
            if(arr[i] != p){
                q = arr[i];
                break;
            }
        }
        answer = (10 * p + q) ** 2;
    }
    else if(n == 2){
        let p = arr[0];
        let temp = [];
        for(let i=0; i<arr.length; i++){
            if(arr[i] != p){
                temp.push(arr[i]);
            }
        }
        if(temp[0] == temp[1]){
            answer = (temp[0] + p) * (Math.abs(p - temp[0]));
        }
        else{
            answer = temp[0] * temp[1];
        }
    }
    else if(n == 1){
        let n1 = countElem(arr, arr[1]);
        if(n1 == 3){
            answer = (10 * arr[1] + arr[0]) ** 2;
        }
        else if(n1 == 2){
            for(let i=0; i<arr.length; i++){
                if(arr[i] != arr[0] && arr[i] != arr[1]){
                    answer = arr[0] * arr[i];
                    break;
                }
            }
            
        }
        else if(n1 == 1){
            if(countElem(arr, arr[2]) == 1){
                answer = arr[0];
            }
            else{
                answer = arr[0] * arr[1];
            }
        }
    }
    
    
    return answer;
}

function countElem(arr, x){
    let n = 0;
    for(let i=0; i<arr.length; i++){
        if(arr[i] == x){
            n+=1
        }
    }
    return n;
}