import threading
import cv2

def preview_th(stop, app):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 400)
    while stop():
        ret, frame = cam.read()
        if ret:
            app.change_img(frame)
        cv2.waitKey(100)
    cam.release()

class CameraService:
    def __init__(self, app):
        self.cam = None
        self.app = app#main_ui에서 만든 ui 창. AppWindow 객체
        self.flag = True  #쓰레드 종료 flag

    def stop(self):
        self.flag = False

    def preview(self):
        self.flag = True
        cam_th = threading.Thread(target=preview_th, args=(lambda:self.flag, self.app))
        cam_th.start()

    def capture(self, fname):
        print('capture')
        self.stop()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)
        self.cam.set(4, 400)
        ret, frame = self.cam.read()
        self.app.change_img(frame)
        cv2.imwrite('img/'+fname, frame)
        self.cam.release()

    def write_avi(self):
        pass

    def view_img(self):
        pass

    def view_video(self):
        pass

