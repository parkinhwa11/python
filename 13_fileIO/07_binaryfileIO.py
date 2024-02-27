# binary file : 이진파일
# - 글자(text)가 아닌 bit 단위로 의미가 부여되는 파일
# - 텍스트파일을 제외한 파일 : 그림파일, 음악파일, 동영상파일, 엑셀, 실행exe
# - 텍스트파일과 이진파일 구분 : 메모장에서 파일열기 시 내용 보이면 텍스트, 이상하게 보이면 이진파일

inStr=''
path1='C:/Windows/notepad.exe' #절대경로
path2='data/notepad.exe'
inF=open(path1,'rb')
outF=open(path2,'wb')

while True:
    inStr=inF.read(1)
    if not inStr:
        break
    outF.write(inStr) #바이트 단위로 읽어서 그대로 쓰는 것

inF.close()
outF.close()

