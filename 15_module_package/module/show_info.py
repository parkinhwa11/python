def show_name():
    print("홍길동")

def show_phone():
    print("010-1234-1234")

if __name__ =='__main__':
    print('자신의 모듈 show_info를 호출함')
    show_name()
    show_phone()
# 다른 파일에서 이 모듈 쓰면 이 부분은 호출이 안 됨.
# __name__ 내장변수는 다른 파일에서 호출 시, 메인이 아니죠.
# 실행하는 파일은 걔가 메인이 됨.
