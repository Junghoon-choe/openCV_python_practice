from tkinter import *
import cv2



def open():
    window = Tk()
    window.title("Camera")
    window.geometry('1600x800+100+50')

    def take_photo():
        cap = cv2.VideoCapture(0)  # 카메라 오픈

        if not cap.isOpened():  # cap.isOpen():카메라 정상오픈이면 True, 아니면 False
            print('카메라 오픈 안됨')
            sys.exit(0)

        cap.set(3, 300)  # 카메라 영상의 가로 길이를 300으로 변경
        cap.set(4, 200)  # 카메라 영상의 세로 길이를 200으로 변경

        print('영상 가로 길이:', cap.get(3))  # cap.get(3):카메라 영상의 가로 길이 반환
        print('영상 세로 길이:', cap.get(4))  # cap.get(4):카메라 영상의 세로 길이 반환

        # 카메라 영상 읽기. ret:처리결과(True, False) / frame:읽은 영상
        ret, frame = cap.read()

        if ret:
            cv2.imwrite('pic1.jpg', frame)  # 카메라 영상 저장
            cv2.imshow('img', frame)  # 영상을 윈도우에 출력
            cv2.waitKey(0)
            cap.release()
            cv2.destroyAllWindows()


    def take_video():
        cap = cv2.VideoCapture(0)  # 카메라 오픈
        codec = cv2.VideoWriter_fourcc(*'DIVX')  # 사용할 코덱 생성
        # 동영상 작성자 객체 생성
        out = cv2.VideoWriter('a.avi', codec, 25.0, (640, 480))  # (제목, 초당 25장을 찍음, 크기)
        while cap.isOpened():  # 카메라 정상 오픈일 때 동작
            ret, frame = cap.read()  # 카메라 영상 읽기
            if ret:  # abs읽기가 정상이면
                out.write(frame)  # 동영상 작성
                cv2.imshow('frame', frame)  # 현재 frame을 윈도우에 출력
                if cv2.waitKey(1) & 0xFF == ord('q'):  # q입력 시 종료
                    break
            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def get_photo():
        pass

    def get_video():
        cap = cv2.VideoCapture('a.avi')  # 동영상 파일 오픈
        while cap.isOpened():  # 동영상 파일이 정상 오픈이면
            ret, frame = cap.read()  # 동영상에서 frame을 읽음
            if not ret:
                break
            cv2.imshow('a.avi', frame)  # 읽은 frame을 윈도우에 출력
            if cv2.waitKey(42) & 0xFF == ord('q'):  # q입력 시 종료
                break
        cap.release()
        cv2.destroyAllWindows()

    Button(window, font='bold 60', text="[ 사진찍기 ]", width=12, command=take_photo).pack()
    Button(window, font='bold 60', text="[ 동영상찍기 ]", width=12, command=take_video).pack()
    Button(window, font='bold 60', text="[ 사진보기 ]", width=12, command=get_photo).pack()
    Button(window, font='bold 60', text="[ 동영상보기 ]", width=12, command=get_video).pack()
    Button(window, font='bold 60', text="[ 뒤로가기 ]", width=12, command=window.destroy).pack()

    window.mainloop()
