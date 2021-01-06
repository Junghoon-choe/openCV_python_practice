import os
import threading
import cv2


def preview_th(stop, app):
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 400)

    # flag가 True일 경우만 실행됨
    while stop():  # stop함수가 호출 될 때 까지.
        ret, frame = cam.read()
        if ret:
            app.change_img(frame)  # 프레임에 뿌려준다. 반복문에 의해서 영상이 계속 전환된다.
        cv2.waitKey(100)
    cam.release()


def img_view_th(stop, app):
    flist = os.listdir('./img')
    i = 0
    # flag가 True일 경우만 실행됨
    while stop():  # stop함수가 호출 될 때 까지.
        p = './img/' + flist[i % len(flist)]  # 012 012 012를 만들어주는 수식
        i += 1
        print(i % len(flist))
        src = cv2.imread(p)
        app.change_img(src)
        cv2.waitKey(1000)


def video_write_th(stop, app, fname):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 400)
    codec = cv2.VideoWriter_fourcc(*'mp4v')  # 사용할 코덱 생성
    # 동영상 작성자 객체 생성
    path = './video/' + fname + '.mp4'
    out = cv2.VideoWriter(path, codec, 25.0, (640, 400))  # (제목, 초당 25장을 찍음, 크기)
    # flag가 True일 경우만 실행됨
    while stop():  # stop함수가 호출 될 때 까지.
        ret, frame = cam.read()
        if ret:
            frame = cv2.resize(frame, (640, 400))
            out.write(frame)
            app.change_img(frame)  # 프레임에 뿌려준다. 반복문에 의해서 영상이 계속 전환된다.
        else:
            break
        cv2.waitKey(26)
    cam.release()

def video_read_th(stop, app, fname):
    path = './video/'+fname+'.mp4'
    cam = cv2.VideoCapture(path) #경로에서 읽어들린다.

    # flag가 True일 경우만 실행됨
    while stop():  # stop함수가 호출 될 때 까지.
        ret, frame = cam.read()
        if ret:
            app.change_img(frame)  # 프레임에 뿌려준다. 반복문에 의해서 영상이 계속 전환된다.
        else:
            break
        cv2.waitKey(26)
    cam.release()

class CameraService:
    def __init__(self, app):
        self.cam = None
        self.app = app  # main_ui 에서 만든 ui 창. appWindow 객체
        self.flag = True  # 쓰레드 종료 flag True면 실행. 아니면 종료.

    def stop(self):
        self.flag = False

    def preview(self):
        self.flag = True
        cam_th = threading.Thread(target=preview_th, args=(lambda: self.flag, self.app))
        cam_th.start()

    def capture(self, fname):
        self.stop()  # 플레그를 False로 만들어서 종료 시키고.
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)
        self.cam.set(4, 400)
        ret, frame = self.cam.read()
        self.app.change_img(frame)
        cv2.imwrite('img/' + fname, frame)
        self.cam.release()

    def write_aviT(self, fname):
        self.flag = True
        cam_th = threading.Thread(target=video_write_th, args=(lambda: self.flag, self.app, fname))
        cam_th.start()

    def write_avi(self, fname):
        cap = cv2.VideoCapture(0)  # 카메라 오픈
        codec = cv2.VideoWriter_fourcc(*'DIVX')  # 사용할 코덱 생성
        # 동영상 작성자 객체 생성
        out = cv2.VideoWriter('video/' + fname + '.avi', codec, 25.0, (640, 480))  # (제목, 초당 25장을 찍음, 크기)
        while cap.isOpened():  # 카메라 정상 오픈일 때 동작
            ret, frame = cap.read()  # 카메라 영상 읽기
            if ret:  # abs읽기가 정상이면
                out.write(frame)  # 동영상 작성
                self.app.change_img(frame)  # 현재 frame에 영상출력
                cv2.imshow('frame', frame)  # 새로운 frame만들어 출력

                cv2.imshow('frame', frame)  # 새로운 frame만들어 출력
                if cv2.waitKey(1) & 0xFF == ord('q'):  # q입력 시 종료
                    break
            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def view_video(self, fname):
        cap = cv2.VideoCapture('video/' + fname + '.avi')  # 동영상 파일 오픈
        while cap.isOpened():  # 동영상 파일이 정상 오픈이면
            ret, frame = cap.read()  # 동영상에서 frame을 읽음
            if not ret:
                break

            cv2.imshow('video/' + fname + '.avi', frame)  # 읽은 frame을 윈도우에 출력
            if cv2.waitKey(42) & 0xFF == ord('q'):  # q입력 시 종료
                break
        cap.release()
        cv2.destroyAllWindows()

    def view_videoT(self, fname):
        self.flag = True
        cam_th = threading.Thread(target=video_read_th,
                                  args=(lambda: self.flag, self.app, fname))
        cam_th.start()


    def view_img(self):
        self.flag = True
        cam_th = threading.Thread(target=img_view_th, args=(lambda: self.flag, self.app))
        cam_th.start()