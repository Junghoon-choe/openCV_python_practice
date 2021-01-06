import tkinter as tk
import cv2
from PIL import Image  # tkinter에서 이미지를 넣으려면 꼭 사용해야 한다.
from PIL import ImageTk


class AppWindow(tk.Frame):  # frame 클래스를 상속 받음.
    def __init__(self, master=None, size=None, path=None):
        super().__init__(master)
        self.master = master  # tk() 객체. 윈도우
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()  # opencv frame

        self.sub_fr = None  # frame
        self.src = None  # tk의 label 에 출력할 영상
        self.frame = None  # tk의 영상을 출력할 레이블

        self.create_widgets(path)

    def make_img(self, path):  # path 경로의 이미지를 레이블에 출력,
        src = cv2.imread(path)  # path 이미지를 읽어서 src에 저장
        src = cv2.resize(src, (640, 400))
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 이미지 color space를 rgb로 변경
        img = Image.fromarray(img)  # 넘파이 배열을 이미지로 변환
        self.src = ImageTk.PhotoImage(image=img)  # tkinter 에서 인식할 수 있는 이미지로 생성

    def create_widgets(self, path):  # 프레임에 위젯 추가
        self.make_img(path)
        self.frame = tk.Label(self.master, image=self.src)

        self.frame.pack()  # 레이블을 프레임에 붙임
        self.sub_fr = tk.Frame(self.master)  # frame 을 하나더 만들어서 추가 위젯을 배치할 프레임 생성
        self.sub_fr.pack()  # tk 객체에 프레임을 붙여줌.

    def change_img(self, img):  # 레이블의 이미지 변경
        img = cv2.resize(img, (640, 400))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)
        self.frame['image'] = self.src

    def preview_img(self, ):
        pass

#  프리뷰를 누르면 사진찍기로 넘어가고 사진찍기 누르면 img폴더에 이미지 저장됨.
