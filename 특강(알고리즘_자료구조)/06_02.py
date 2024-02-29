# 함수
def isQueueFull():
    global SIZE, queue, front, rear
    # Case1:뒤에 여유있음(가장 행복)
    if rear!=SIZE-1:
        return False
    # Case2: 진짜 꽉참
    elif rear==SIZE-1 and front==-1:
        return True
    # Case3: 뒤는 마지막, 앞에 여유(고민)
    elif rear==SIZE-1 and front!=-1: #else
        for i in range(front+1,SIZE):
            queue[i-1]=queue[i]
            queue[i]=None
        front-=1
        rear-=1
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
    rear+=1
    queue[rear]=data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("빔")
        return None
    front+=1
    pop=queue[front]
    queue[front]=None
    return pop

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("큐 빔")
        return None
    return queue[front+1]

# 변수

SIZE=5
queue=[None for _ in range(SIZE)]
front=rear=-1

# 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')



retData=deQueue()
print("손님 이리로-->",retData)
print("준비하세요==>",peek())

retData=deQueue()
print("손님 이리로-->",retData)
enQueue("재남")
# retData=deQueue()
# print("손님 이리로-->",retData)

print(queue)

