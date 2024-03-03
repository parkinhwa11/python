# 큐

# 함수

# 변수
SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=-1


# 메인
#! enQueue()
rear+=1
queue[rear]="화사"
rear+=1
queue[rear]="솔라"
rear+=1
queue[rear]="문별"
print('출구<--',queue,'<--입구')

#! deQueue()
front+=1
data=queue[front]
queue[front]=None
print('식사 손님 : ',data)

front+=1
data=queue[front]
queue[front]=None
print('식사 손님 : ',data)

front+=1
data=queue[front]
queue[front]=None
print('식사 손님 : ',data)

print('출구<--',queue,'<--입구')


## 자료구조 ##
# . 선형
# 	- 리스트
# 		. 선형 리스트 : 배열
# 		. 단순 연결 리스트 : 노드(Data+Link)
# 		. 원형 연결 리스트 : 마지막 노드? Link == Head
# 	- 스택 : 한쪽 막힌 파이프. FILO
# 	- 큐
# 		. 순차 큐 : 양쪽 뚫리 파이프. FIFO]
# 		. 원형 큐 : %SIZE
# . 비선형
# 	- 트리 --> 이진 트리
# 	- 그래프 : 방향/무방향
#
# ## 알고리즘 ##
# . 정렬
# 	- 선택 정렬 (메모리 2개, 메모리 1개)  --> 버블정렬, 퀵정렬(+재귀)
#
# . 검색
# 	- 순차 검색
# 	- 이진 검색
#
# . 재귀 : 다양한 사례