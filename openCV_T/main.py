import tkinter as tk
import openCV_T.main_ui as win
import openCV_T.make_widgets as mkw
import openCV_T.camera_service as s

def main():
    img_path = 'img/a.jpg'
    root = tk.Tk()
    app = win.AppWindow(root, '1300x800+100+100', img_path)  # (윈도우 객체, 크기, 이미지 경로)
    service = s.CameraService(app)  # 카메라로 서비스 연결
    mkw.make(app, service)
    app.mainloop()

main()
