import tkinter as tk

c_serv = None  #서비스 객체

def btn1_clicked():
    c_serv.preview()

def btn2_clicked(app):
    fname = app.ent.get()
    c_serv.capture(fname)

def btn3_clicked():
    print('btn3 clicked')

def make(app, service=None):
    global c_serv
    c_serv = service
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.btn1 = tk.Button(app.sub_fr, width=10, font=60, text='preview')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=60, text='사진저장')
    app.btn3 = tk.Button(app.sub_fr, width=10, font=60, text='영상촬영')
    app.btn4 = tk.Button(app.sub_fr, width=10, font=60, text='촬영종료')
    app.btn5 = tk.Button(app.sub_fr, width=10, font=60, text='동영상보기')
    app.btn6 = tk.Button(app.sub_fr, width=10, font=60, text='슬라이드시작')
    app.btn7 = tk.Button(app.sub_fr, width=10, font=60, text='슬라이드종료')

    app.ent.grid(row=0, column=0, columnspan=4)
    app.btn1.grid(row=1, column=0)
    app.btn2.grid(row=1, column=1)
    app.btn3.grid(row=1, column=2)
    app.btn4.grid(row=1, column=3)
    app.btn5.grid(row=2, column=0)
    app.btn6.grid(row=2, column=1)
    app.btn7.grid(row=2, column=2)

    app.btn1['command'] = lambda: btn1_clicked()
    app.btn2['command'] = lambda: btn2_clicked(app)
    app.btn3['command'] = btn3_clicked