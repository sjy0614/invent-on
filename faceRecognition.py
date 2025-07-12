# 1. 필요한 라이브러리 임포트
from picamera2 import Picamera2
import cv2
import time

# 2. 얼굴 탐지를 위한 Haar Cascade 모델 로드
face_cascade_name = './haarcascades/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier()

if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)

# 3. 카메라 설정 및 시작
frame_width = 640
frame_height = 480

picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (frame_width, frame_height), "format": "BGR888"})
picam2.configure(config)
picam2.start()
time.sleep(1.0)

# 4. 메인 루프
while True:
    # 카메라에서 프레임(이미지)을 가져옴
    image = picam2.capture_array()

    # 얼굴 탐지를 위해 흑백 이미지로 변환
    frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    # 흑백 이미지에서 얼굴 탐지
    faces = face_cascade.detectMultiScale(frame_gray)

    # 탐지된 모든 얼굴에 대해 반복
    for (x, y, w, h) in faces:
        # 원본 컬러 이미지에 녹색 사각형 그리기
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 결과 이미지 보여주기
    cv2.imshow("Face Detection", image)

    # 'q' 키를 누르면 종료
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# 5. 종료 처리
picam2.stop()
cv2.destroyAllWindows()
