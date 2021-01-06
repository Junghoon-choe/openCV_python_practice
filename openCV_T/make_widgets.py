import sys
import tkinter as tk
import cv2
import threading
import os.path
import openCV_T.camera_service as cam

#   프리뷰 버튼을 누르면 함수실행하며, 쓰레드를 통해서 계속 촬영 시켜준다.
c_serv = None  # 서비스 객체


def btn1_clicked():
    c_serv.preview()


def btn2_clicked(app):
    c_serv.capture(fname=app.ent.get())


def btn3_clicked(app):
    cap = cv2.VideoCapture(0)  # 카메라 오픈
    fname = app.ent.get()
    if not cap.isOpened():  # cap.isOpen():카메라 정상오픈이면 True, 아니면 False
        print('카메라 오픈 안됨')
        sys.exit(0)

    cap.set(3, 300)  # 카메라 영상의 가로 길이를 300으로 변경
    cap.set(4, 200)  # 카메라 영상의 세로 길이를 200으로 변경

    print('영상 가로 길이:', cap.get(3))  # cap.get(3):카메라 영상의 가로 길이 반환
    print('영상 세로 길이:', cap.get(4))  # cap.get(4):카메라 영상의 세로 길이 반환

    # 카메라 영상 읽기. ret:처리결과(True, False) / frame:읽은 영상

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('img', frame)  # 영상을 윈도우에 출력
            if cv2.waitKey(5) == 27:
                # targetdir = 'img'
                # files = os.listdir(targetdir)
                # count = 0
                cv2.imwrite(fname, frame)  # 카메라 영상 저장
                break

    cap.release()
    cv2.destroyAllWindows()


#  사진촬영 버튼을 누르면 함수 실행. 및 쓰레드 종료.
targetdir = 'img'
files = os.listdir(targetdir)
print(files[1])
filelist = []
for i in files:
    filelist.append(i)
count = 0


def btn4_clicked(app):
    global filelist, count
    try:
        img = cv2.imread('img/' + filelist[count])
        app.change_img(img)
        count += 1
    except IndexError:
        print('마지막 사진입니다.')
        count = 0


def btn5_clicked(app):
    c_serv.write_avi(fname=app.ent.get())


def btn6_clicked(app):
    c_serv.view_video(fname=app.ent.get())


def btn7_clicked(app):
    c_serv.view_img()


def btn8_clicked(app):
    c_serv.stop()


def btn33_clicked(app):
    fname = app.ent.get()
    c_serv.write_aviT(fname)


def btn44_clicked():
    c_serv.stop()

def btn55_clicked(app):
    fname = app.ent.get()
    c_serv.view_videoT(fname)


def make(app, service=None):  # 추가할 위젯을 넣는다.
    global c_serv
    c_serv = service
    app.ent = tk.Entry(app.sub_fr, width=60)  # self.sub_fr = None  # frame 에 붙여준다.
    app.btn1 = tk.Button(app.sub_fr, width=15, font=40, text='프리뷰')
    app.btn2 = tk.Button(app.sub_fr, width=15, font=40, text='사진촬영')
    app.btn3 = tk.Button(app.sub_fr, width=15, font=40, text='웹캠 사진 촬영')
    app.btn4 = tk.Button(app.sub_fr, width=15, font=40, text='사진넘기기')
    app.btn5 = tk.Button(app.sub_fr, width=15, font=40, text='영상촬영')
    app.btn6 = tk.Button(app.sub_fr, width=15, font=40, text='동영상보기')
    app.btn7 = tk.Button(app.sub_fr, width=15, font=40, text='사슬시작')
    app.btn8 = tk.Button(app.sub_fr, width=15, font=40, text='사슬종료')

    app.btn33 = tk.Button(app.sub_fr, width=15, font=40, text='영상촬영T')
    app.btn44 = tk.Button(app.sub_fr, width=15, font=40, text='영상종료T')
    app.btn55 = tk.Button(app.sub_fr, width=15, font=40, text='영상보기')

    app.ent.grid(row=0, column=0, columnspan=5)
    app.btn1.grid(row=1, column=0)
    app.btn2.grid(row=1, column=1)
    app.btn3.grid(row=1, column=2)
    app.btn4.grid(row=1, column=3)
    app.btn5.grid(row=2, column=0)
    app.btn6.grid(row=2, column=1)
    app.btn7.grid(row=2, column=2)
    app.btn8.grid(row=2, column=3)

    app.btn33.grid(row=4, column=0)
    app.btn44.grid(row=4, column=1)
    app.btn55.grid(row=4, column=2)

    app.btn1['command'] = btn1_clicked  # 파라미터 없음
    app.btn2['command'] = lambda: btn2_clicked(app)
    app.btn3['command'] = lambda: btn3_clicked(app)
    app.btn4['command'] = lambda: btn4_clicked(app)
    app.btn5['command'] = lambda: btn5_clicked(app)
    app.btn6['command'] = lambda: btn6_clicked(app)
    app.btn7['command'] = lambda: btn7_clicked(app)
    app.btn8['command'] = lambda: btn8_clicked(app)

    app.btn33['command'] = lambda: btn33_clicked(app)
    app.btn44['command'] = btn44_clicked  # 파라미터 없음
    app.btn55['command'] = lambda: btn55_clicked(app)
