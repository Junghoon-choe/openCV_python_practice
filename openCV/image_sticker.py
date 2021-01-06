import cv2
import numpy as np

img1 = cv2.imread('c.jpg')
color = [255, 255, 255]
img2 = np.full(img1.shape, color, dtype=np.uint8)

_start = None
_end = None
roi = None


def open():
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    def drag(event, x, y, flags, param):
        global _start, _end, roi
        if event == cv2.EVENT_LBUTTONDOWN:
            _start = [x, y]
        elif event == cv2.EVENT_LBUTTONUP:
            _end = [x, y]
            roi = img1[_start[1]:_end[1], _start[0]:_end[0]]

    def drop(event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            w = np.abs(_start[0] - _end[0])  # 절대 값으로 w를 선언한다. 드래그한 만큼의 공간의 넓이
            h = np.abs(_start[1] - _end[1])  # 드래그한 만큼의 공간의 높이
            img2[y:y + h, x:x + w] = roi
            cv2.imshow('img2', img2)
            # roi = None

    cv2.setMouseCallback('img1', drag)
    cv2.setMouseCallback('img2', drop)

    while True:
        if cv2.waitKey(0) & 0xFF == 27:
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''import cv2
import numpy as np

src = cv2.imread('c.jpg')  # d.jpg 파일. src는 메모리에 저장된 배열
h, w, c = src.shape  # src의 shape들을 각각저장해서
color = [255, 255, 255]
dst = np.full((h, w, c), color, dtype=np.uint8)  # 이와같이 흰색으로 만들어준다.

p0 = None  # LBUTTONDOWN이벤트가 발생하는 지점. 복사할 영역 시작점.
p1 = None  # LBUTTONUP이벤트가 발생하는 지점. 복사할 영역 끝점.
roi = None  # p0 p1을 합친 점을 말한다. 리전오브이미지


def open():
    cv2.imshow('src', src)  # 이미지와
    cv2.imshow('dst', dst)  # 흰판을 화면에 출력.

    def handdler_src(event, x, y, flags, param):
        global p0, p1
        if event == cv2.EVENT_LBUTTONDOWN:
            p0 = (x, y)  # 범위 설정
        elif event == cv2.EVENT_LBUTTONUP:
            p1 = (x, y)  # 범위 설정
            make_roi()  # roi함수 호출

    def make_roi():
        global roi
        roi = src[p0[1]:p1[1], p0[0]:p1[0]]  # src[줄(p1[]),칸]

    def handdler_dst(event, x, y, flags, param):
        global roi  # 쓰는 이유는 roi에러를 막기위해 사용.
        if event == cv2.EVENT_LBUTTONDOWN:
            if roi is not None:  # roi랑 같은 크기의 영역을 클릭한 위치에 넣는다.
                h = np.abs(p0[1] - p1[1])
                w = np.abs(p0[0] - p1[0])
                dst[y:y + h, x:x + w] = roi
                cv2.imshow('dst', dst)
                roi = None

    # 빈 Image 생성
    cv2.setMouseCallback('src', handdler_src)  # src창에서 마우스이벤트 발생하면 handdler_src 함수 실행
    cv2.setMouseCallback('dst', handdler_dst)  # dst창에서 마우스이벤트 발생하면 handdler_dst 함수 실행

    while True:
        if cv2.waitKey(0) & 0xFF == 27:
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
