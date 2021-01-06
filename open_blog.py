# 12 : <이미지 차> 를 사용해서 움직이는 객체만 추출하는 앱 만들기
# 두 이미지 빼기 연산으로 차를 구할 수 있음
# dst(x, y) = src1(x, y) - src2(x, y)
'''
import cv2

cap = cv2.VideoCapture(0)  # 카메라 오픈
cap.set(3, 300)
cap.set(4, 200)

prev_frame = None
# 영상 읽기
ret, prev_frame = cap.read()

while True:
    ret, frame = cap.read()
    if ret:  # 정상 읽기일 때만

        f = cv2.absdiff(prev_frame, frame)
        cv2.imshow('img', f)  # 영상을 윈도우에 출력
        prev_frame = frame

    k = cv2.waitKey(1)
    if k == 27:  # 입력한 키가 esc이면
        break
cap.release()
cv2.destroyAllWindows()
'''

# 11 : <마스크 연산>
# 추출하고 싶은 객체를 제외한 나머지 배경을
# 0으로 처리하면 배경은 검정색, 객체는 그대로인 이미지가 된다.
# 이를 합성하려는 이미지와 더하면 배경은 0이므로 합성하는 이미지의 내용 그대로,
# 객체는 위로 붙게된다.
'''
import cv2

daum_logo = cv2.imread('daum.png', 1)
img1 = cv2.imread('c.jpg', 1)
h, w, c = daum_logo.shape
# 배경이미지의 변경할(다음 로고 넣을) 영역
roi = img1[150:150 + h, 150:150 + w]

# 다음 글자 추출
# 로고를 흑백처리
# 이미지 이진화 => 배경은 검정. 글자는 흰색
mask = cv2.cvtColor(daum_logo, cv2.COLOR_BGR2GRAY)
mask[mask[:] == 255] = 0
mask[mask[:] > 0] = 255

# 마스크 인버트는 bitwise_not함수로 글자만 추출해 낸다.
# mask반전.  => 배경은 흰색. 글자는 검정
mask_inv = cv2.bitwise_not(mask)

#  위에 마스크에서 추출한 부분을 로고에 더해줌으로 마스크만 빼냄
# 마스크와 로고 칼라이미지 and하면 글자만 추출됨
daum = cv2.bitwise_and(daum_logo, daum_logo, mask=mask)
#  로이와 마스크를 합쳐냄. 측 배경에서 글자부분만 파냄.
# roi와 mask_inv와 and하면 roi에 글자모양만 검정색으로 됨
back = cv2.bitwise_and(roi, roi, mask=mask_inv)
# 더해서 결과 값을 만들어낸다.
# 로고 글자와 글자모양이 뚤린 배경을 합침
dst = cv2.add(daum, back)
#  원본 이미지에 넣어준다.
# roi를 제자리에 넣음
img1[150:150 + h, 150:150 + w] = dst
cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 10 : 트랙바를 사용하여 두 이미지 합성 비율을 조절하는 프로그램을 만들기
# 두이미지의 픽셀 값을 더하여 이미지를 합성한다.
# 그냥 하면 포화문제로 포화연산을 넣어추가 작업한다.

'''
import cv2


def s(pos):
    # addWeighted
    pic = cv2.addWeighted(img1, (100 - pos) / 100, img2, pos / 100, 0)
    cv2.imshow('img', pic)


# 이미지 두개가 달라서 사이즈 같게 설정
img1 = cv2.imread('a.jpg', 1)
img1 = cv2.resize(img1, (320, 270))
img2 = cv2.imread('b.jpg', 1)
img2 = cv2.resize(img2, (320, 270))

cv2.imshow('img', img1)
cv2.createTrackbar('bright', 'img', 0, 100, s)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# 9 : 이미지에 and, or, not, xor 연산 수행
# 이미지 연산은 각 픽셀의 b, g, r bit 별로 수행 한다
# bitwise_and()함수는 img1 과 img2의 값이 일치하면 True를 반환해준다. 연산자인 and(&) 를 생각하면 쉽다.
# bitwise_or()함수는 img1 또는 img2의 값이 1이면 True를 반환한다.
# bitwise_not() 함수는 파라메터에 입력된 값을 반대로 돌려준다. 즉, 1이면 0, 0이면 1 이렇게 반전된다.
# bitwise_xor() 함수는 bitwise_or()함수와 비슷한데, img1 또는 img2의 값이 같을경우에만 0을 반환해준다.
'''
import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

img3 = cv2.bitwise_and(img1, img2)
img4 = cv2.bitwise_or(img1, img2)
img5 = cv2.bitwise_not(img2)
img6 = cv2.bitwise_xor(img1, img2)

imgh1 = cv2.hconcat([img1, img2, img3])
imgh2 = cv2.hconcat([img4, img5, img6])

res = cv2.vconcat([imgh1, imgh2])

cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 8 : 히스토그램 평활화

# 평활화는 어두운 픽셀과 밝은 픽셀의 값들을 평준화 시킨다는 말이다.
# 즉 픽셀 값들을 평준화 시키면 그만큼 선명도가 올라가게된다.
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt


def saturate_contrast2(p, num):
    pic = p.copy()
    pic = pic.astype('int32')
    pic = np.clip(pic + (pic - 128) * num, 0, 255)
    pic = pic.astype('uint8')
    return pic


def e_hist(src):
    hist, bins = np.histogram(src.flatten(), 256, [0, 256])
    cdf = hist.cumsum()  # 누적합. 각 빈의 누적합 계산
    cdf_m = np.ma.masked_equal(cdf, 0)  # 속도개선을 위해 0인 부분 제외

    # 히스토그램 평활화
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())

    # Mask처리를 했던 부분을 다시 0으로 변환
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    src = cdf[src]
    return src


GRAY = 0
COLOR = 1
img = cv2.imread('b.jpg', GRAY)

img1 = saturate_contrast2(img, 2)
img2 = e_hist(img1)  # equalizeHist() 함수를 구현한 함수.
img3 = cv2.equalizeHist(img1)  # equalizeHist()함수를 사용.

hist1 = cv2.calcHist([img2], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img3], [0], None, [256], [0, 256])
plt.subplot(4, 1, 1), plt.imshow(img1, 'gray')
plt.subplot(4, 1, 2), plt.imshow(img2, 'gray')
plt.subplot(4, 1, 3), plt.plot(hist1, color='r') # e_hist()함수를 사용.
plt.subplot(4, 1, 4), plt.plot(hist2, color='r') # equalizeHist()함수를 사용.

plt.show()
'''

# def saturate_contrast_deep(p, num):
#     pic = p.copy()
#     pic = pic.astype('int16')
#     pic = np.clip(pic + (pic - 128) * num, 0, 255)
#     pic = pic.astype('uint8')
#     return pic
#
#
# def saturate_contrast_shallow(p, num):
#     pic = p.copy()
#     pic = pic.astype('int16')
#     pic = np.clip(pic + (pic - 128) * ((-1 / 100) * num), 0, 255)
#     pic = pic.astype('uint8')
#     return pic
#
#
# GRAY = 0
# COLOR = 1
# img = cv2.imread('a.jpg', COLOR)
#
# cv2.imshow('img', img)
# cv2.createTrackbar('deep', 'img', 0, 10, lambda pos: cv2.imshow('img', saturate_contrast_deep(img, pos)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 7 : <히스토그램 분석>

# Histogram은 이미지의 밝기의 분포를 그래프로 표현한 방식입니다.
# 히스토그램을 이용하면 이미지의 전체의 밝기 분포와 채도(색의 밝고 어두움)를 알 수 있습니다.

# cv2.calcHist(img,channel,mask,histSize,range)
# img: 이미지 배열
# channel: 분석할 칼라
# mask: 분석할 영역. None이면 이미지 전체
# histSize: 히스토그램 크기. x축 값 개수
# range: x축 값 범위

# calcHist = 히스토그램 계산기
# cv2.calcHist(이미지의 배열, 분석할 칼라, 분석할 영역(None 이면 전체), x축 값 개수, x축 값 범위)
# 즉, 해당 이미지를 넣고, 0의 칼라를 분석한다. 영역은 전체이면서, x축값은 256개로 0부터 255까지 지정한다.
# hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# subplot(m,n,p)는 현재 Figure를 mxn 그리드로 나누고, p로 지정된 위치에 좌표축을 만듭니다.
# MATLAB®은 행을 기준으로 서브플롯 위치의 번호를 매깁니다.
# 첫 번째 서브플롯은 첫 번째 행의 첫 번째 열이고,
# 두 번째 서브플롯은 첫 번째 행의 두 번째 열이 되는 방식으로 진행됩니다.
# 지정된 위치에 좌표축([1,2])이 있는 경우 이 명령은 그 좌표축을 현재 좌표축으로 지정합니다.

'''
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('a.jpg', 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.subplot(2, 1, 1), plt.imshow(img, 'gray')
plt.subplot(2, 1, 2), plt.plot(hist, color='r')
plt.show()
'''

# 6 : 트랙바를 이용해서 이미지의 명암을 조절하는 앱 만들기
'''
import numpy as np
import cv2


def saturate_contrast_deep(p, num):
    pic = p.copy()
    pic = pic.astype('int16')
    pic = np.clip(pic + (pic - 128) * num, 0, 255)
    pic = pic.astype('uint8')
    return pic

def saturate_contrast_shallow(p, num):
    pic = p.copy()
    pic = pic.astype('int16')
    pic = np.clip(pic + (pic - 128) * ((-1/100)*num), 0, 255)
    pic = pic.astype('uint8')
    return pic


GRAY = 0
COLOR = 1
img = cv2.imread('a.jpg', COLOR)

cv2.imshow('img', img)
cv2.createTrackbar('deep', 'img', 0, 10, lambda pos: cv2.imshow('img', saturate_contrast_deep(img, pos)))
cv2.createTrackbar('shallow', 'img', 0, 50, lambda pos: cv2.imshow('img', saturate_contrast_shallow(img, pos)))
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 5 : 이미지의 명암비를 조절하는 방법
# 명암비란 이미지의 밝은 부분과 어두운 부분의 밝기 차를 의미.
# 명암비 조절은 이미지의 밝은 부분은 더 밝게,
# 이미지의 어두운 부분은 더 어둡게 함으로써 이미지 윤곽을 뚜렷하게 처리하므로 활용도 높음
#
# *명암비 효율적 조절
# 픽셀 중간값인 128을 기준으로 이 보다 큰 값은 더 밝게 만들고
# 128보다 작은 값은 더 어둡게 만듦으로써 대비를 크게 함
# dst(x, y) = src(x, y) + (src(x, y)-128) * alpha
'''

import numpy as np
import cv2

def saturate_contrast(p, num):
    pic = p.copy()
    pic = pic.astype('int16')
    pic = np.clip(pic + (pic - 128) * num, 0, 255)
    pic = pic.astype('uint8')
    return pic


GRAY = 0
COLOR = 1
img = cv2.imread('a.jpg', COLOR)

# 명암비를 1보다 작게 주면 밝기 차가 줄어들고 전반적으로 어두어짐
# 함수에서 pic * num << 이와같이 곱해줌을 유의하자
img1 = saturate_contrast(img, 2)

# 명암비를 1보다 크게 주면 밝기 차가 커지고 흰색 영역이 넓어짐
img2 = saturate_contrast(img, 0.5)


cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 4 : 트랙바를 이용해서 이미지 밝기를 조절하는 앱 만들기
'''
import numpy as np
import cv2


def saturate_bright(p, num):
    pic = p.copy()  # 깊은 복사로 타입을 변환
    pic = pic.astype('int16')
    pic = np.clip(pic + num, 0, 255)  # 받아온 숫자로 밝기를 높혀줌
    pic = pic.astype('uint8')  # 타입을 다시 변경시켜줌. 그러면 사진 안 깨짐.
    return pic


def saturate_dark(p, num):
    pic = p.copy()  # 깊은 복사로 타입을 변환
    pic = pic.astype('int16')
    pic = np.clip(pic - num, 0, 255)  # 받아온 숫자를 밝기를 빼서 낮혀줌
    pic = pic.astype('uint8')  # 타입을 다시 변경시켜줌. 그러면 사진 안 깨짐.
    return pic


GRAY = 0
COLOR = 1
img = cv2.imread('a.jpg', COLOR)

cv2.imshow('img', img)
cv2.createTrackbar('brighter', 'img', 0, 100, lambda pos: cv2.imshow('img', saturate_bright(img, pos)))
cv2.createTrackbar('darker', 'img', 0, 100, lambda pos: cv2.imshow('img', saturate_dark(img, pos)))
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 3 : 함수를 통해 어두운 이미지와 밝은 이미지 생성
'''
import numpy as np
import cv2

def saturate_bright(p, num):
    pic = p.copy() # 깊은 복사로 타입을 변환
    pic = pic.astype('int32') # 2,147,483,647의 값을 갖는 타입으로 변경
    pic = np.clip(pic+num, 0, 255) # 받아온 숫자로 밝기를 높혀줌
    pic = pic.astype('uint8') # 타입을 다시 변경시켜줌. 그러면 사진 안 깨짐. 이유는 2
    return pic

def saturate_dark(p, num):
    pic = p.copy()
    pic = pic.astype('int32')
    pic = np.clip(pic-num, 0, 255) # 받아온 숫자를 밝기를 빼서 낮혀줌
    pic = pic.astype('uint8') # 타입을 다시 변경시켜줌. 그러면 사진 안 깨짐.
    return pic

GRAY = 0
COLOR = 1
img = cv2.imread('a.jpg', COLOR)

img2 = saturate_bright(img, 100)  #이미지 밝게 처리
img3 = saturate_dark(img, 100)  #이미지 어둡게 처리
cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 2 : 이미지 밝기 조절
'''
import cv2
import numpy as np

GRAY = 0
COLOR = 1
img = cv2.imread('a.jpg', COLOR)

img2 = np.clip(img.astype('int32')+100,0,255).astype('uint8') # 이미지 밝게 처리
img3 = np.clip(img.astype('int32')-100,0,255).astype('uint8') # 이미지 어둡게 처리
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 1 : 포화연산 안하고 이미지 밝게
'''
import cv2

GRAY = 0
COLOR = 1

# 1을 넣으면 되지만 굳이 상수는 만들어서 넣는 이유는 가독성 때문이다.
img = cv2.imread('a.jpg', COLOR)
img2 = img+100 # 이미지 밝게 처리
img3 = img-100 # 이미지 어둡게 처리

cv2.imshow('img', img)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
