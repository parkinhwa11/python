try:
    for i in range(1,7):
        result=7//i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다")
import random
answer=random.randint(1,10)
def guess_number(answer):
    try:
        guess=int(input("숫자를 넣어:"))
        if guess==guess:
            print("정답!")
        else:
            print("오답")
    except ValueError:
        print("숫자 아닙니다.")
guess_number(answer)

for i in range(3):
    try:
        print(i,3//i)
    except ZeroDivisionError:
        print("Not divided by 0")