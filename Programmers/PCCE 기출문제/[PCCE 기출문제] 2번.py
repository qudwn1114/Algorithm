#디버깅(Debugging)은 이미 완성된 코드에서 버그를 찾아 수정하는 문제 타입입니다.
#1줄만 수정하여 버그를 고치세요.
#2줄 이상 수정할 경우, 실행 결과에 에러 메시지가 표시됩니다.

a = int(input())
c = int(input())

b_square = c*c - a*a # 원본 b_square = c - a
print(b_square)