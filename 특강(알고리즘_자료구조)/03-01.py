# 함수 선언부



# 전역 변수부
katok=['다현','정연','쯔위','사나','지효']

# 메인 코드부
print(katok)

# 데이터 추가 (모모에게 카톡 1회)
katok.append(None)
katok[5]='모모'
print(katok)

# 1단계 : 빈 칸 추가
katok.append(None)
# 2단계 : 한칸씩 뒤로 이동
katok[6]=katok[5]  # 모모이동
katok[5]=None
katok[5]=katok[4] # 지효이동
katok[4]=None
katok[4]=katok[3] # 사나이동
katok[3]=None
katok[3]="미나"   # 미나삽입
print(katok)

# 데이터 삭제 ( 사나가 카톡 차단)
# 1단계 : 데이터 지우기
katok[4]=None
# 2단계 : 한칸씩 앞으로 : 5등부터 마지막까지
katok[4]=katok[5]
katok[5]=None
katok[5]=katok[6]
katok[6]=None
# 3단계 : 마지막 칸 제거
del(katok[6])
print(katok)



