# 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1)%SIZE==front:
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front==rear:
        return True
    else:
        return False
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print("꽉 참")
        return
    rear=(rear+1)%SIZE
    queue[rear]=data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("빔")
        return None
    front=(front+1)%SIZE
    pop=queue[front]
    queue[front]=None
    return pop

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("큐 빔")
        return None
    return queue[(front+1)%SIZE]

# 변수

SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=0

# 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
# enQueue('선미')



retData=deQueue()
print("손님 이리로-->",retData)
print("준비하세요==>",peek())

retData=deQueue()
print("손님 이리로-->",retData)
# enQueue("재남")
# retData=deQueue()
# print("손님 이리로-->",retData)

print(queue)

