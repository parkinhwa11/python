# 문자열의 모든 글자 뒤에 $ 붙이기
#print(char)하면 문자열 하나하나 다 가져와짐
# S="파이썬짱!"
# temp=''
# for char in S:
#     temp+=char+"$" # char+"$"+temp 하면 !$짱$썬$이$파$ 역순 출력
                   # "$"+char+temp 하면 $!짱$썬$이$파 출력
# print(temp)
    #print(char,end="$")
    # char+"$" 하면 하나의 문자열로 안 나옴.
    # 하나의 문자열로 이어야 함!

# 문자열 짝수번째 글자 #으로 변경
# 풀이1-요 뒤에 # 붙음
# S = "파이썬은재미있어요"
# temp=""
# for char in S[::2]:
#     temp+=char+"#"
# print(temp)

#풀이2-요 뒤에 # 안 붙음!
# S="파이썬은재미있어요"
# temp=""
# cnt=-1
# for ch in S:
#     print('cnt:',cnt)
#     if cnt%2==0:
#         ch='#'
#     else:
#         pass
#     temp+=ch
#     cnt+=1
# print(temp)

# 풀이3-삼항연산자, 인덱싱 사용
# text="파이썬은재미있어요"
# temp=""
# for i in range(len(text)):
#     ch='#' if i%2!=0 else text[i] #인덱스가 0,2,4,6,8은 text[i]
#     #그 외 홀수 인덱스(짝수번째 문자)는 #으로 대체 (i%2==1)
#     temp+=ch
# print(temp)

# 3. 입력 받는 문자열 거꾸로 출력
# char=input("문자열을 입력하세요 :")
# rev=char[::-1]
# print(rev)








