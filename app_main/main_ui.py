import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk

class AppWindow(tk.Frame):#Frame
    def __init__(self, master=None, size=None, path=None):
        super().__init__(master)
        self.master = master #Tk()객체. 윈도우
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()#이미지 레이블 frame
        self.sub_fr = None#버튼 있는 frame
        self.src = None #이미지 변수
        self.frame = None #이미지 출력할 레이블
        self.create_widgets(path)#기본 위젯 생성 함수

    def make_img(self, path):#path 경로의 이미지를 레이블에 출력
        #opencv 이미지
        src = cv2.imread(path) #path 이미지를 읽어서 src에 저장
        src = cv2.resize(src, (640, 400))
        #이미지 color space를 rgb로 변경
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        #넘파이 배열을 필로우 이미지 변환
        img = Image.fromarray(img)#넘파이 배열을 이미지로 변환
        #tkinter에서 사용할 수 있는 이미지로 변환
        #self.src = 이미지
        self.src = ImageTk.PhotoImage(image=img)#tkinter에서 인식할 수 있는 이미지로 생성

    def create_widgets(self, path):#프레임에 위젯 추가
        self.make_img(path)
        #이미지 뿌릴 레이블 생성
        self.frame = tk.Label(self.master, image=self.src)
        #레이블을 프레임에 붙임
        self.frame.pack()
        #추가 위젯을 배치할 프레임 생성
        self.sub_fr = tk.Frame(self.master)#frame
        #프레임 윈도우 붙임
        self.sub_fr.pack()

    def change_img(self, img):#레이블의 이미지 변경
        img = cv2.resize(img, (640, 400))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)
        self.frame['image']=self.src