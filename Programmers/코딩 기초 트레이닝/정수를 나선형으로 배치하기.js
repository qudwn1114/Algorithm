function solution(n) {
    var answer = [];
    for(let i=0; i<n; i ++){
        let temp = [];
        for(let j=0; j<n; j++){
            temp.push(0);
        }
        answer.push(temp);
    }
    
    let x = 0;
    let y = 0;
    
    let max_x = n-1;
    let max_y = n-1;
    let min_x = 0;
    let min_y = 1;
    
    let d = 0; //0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
    
    for(let i=1; i<=n*n; i++){
        answer[y][x] = i;
        if(i != n*n){
            //오른쪽 으로 갈때
            if(d == 0){
                if(max_x == x){
                    max_x -= 1;
                    y += 1
                    d = 1;
                }
                else{
                    x += 1
                } 
            }
            else if (d == 1){
                if(max_y == y){
                    max_y -= 1;
                    x -= 1;
                    d = 2
                }
                else{
                    y += 1
                }
            }
            else if (d == 2){
                if(min_x == x){
                    min_x += 1;
                    y -= 1;
                    d = 3
                }
                else{
                    x -= 1
                }
            }
            else if (d == 3){
                if(min_y == y){
                    min_y += 1;
                    x += 1;
                    d = 0
                }
                else{
                    y -= 1
                }
            }
        }
    }
    
    
    return answer;
}