'''
# 사진 앱 만들기
기능
1. 사진 찍기
2. 동영상 찍기
3. 사진 앨범 보기
4. 동영상 보기

# 이미지 붙이기
1. 원도우1 원본이미지, 원도우2: 흰바탕 이미지
2. 원본이미지를 마우스로 드래그하여 영역을 지정한 뒤 흰 바탕 이미지를 클릭하면 클릭한 위치에 원본이미지에서
드래그한 영역 이미지를 복사하여 붙임
'''
from tkinter import *
import selection


window = Tk()
window.title("Joe's Python Camera")
window.geometry('1600x800+100+50')


Button(window, font='bold 60', text="[ 카메라 ]", width=12, command=selection.camera).pack()
Button(window, font='bold 60', text="[ 스티커 ]", width=12, command=selection.sticker).pack()
Button(window, font='bold 60', text="[ 프로그램 종료 ]", width=12, command=window.destroy).pack()

window.mainloop()

