import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw
import app_main.camera_service as s

def main():
    img_path = 'img/a.jpg'
    root = tk.Tk()
    app = win.AppWindow(root, '650x700+100+100', img_path)
    service = s.CameraService(app)
    mkw.make(app, service)
    app.mainloop()

main()
