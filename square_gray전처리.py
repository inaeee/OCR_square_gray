#필수 패키지 가져오기
import cv2
import numpy as np



num=1
for i in range(1,208):
    #img파일 가져오기
    path="C:\\Users\\inaee\\Desktop\\2020-1MAKERS\\OCR\\square_size500\\square_"+str(i)+".jpg"
    image=cv2.imread(path)
    print(image)
    print("가져옴")
    
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(gray)
    print("gray 완료")

    #noise=cv2.medianBlur(gray,5)
    #print(noise)
    #print("noise 완료")
    
    
    cv2.imshow("img", gray)

    
    # 이미지 저장하기
    cv2.imwrite("C:\\Users\\inaee\\Desktop\\2020-1MAKERS\\OCR\\square_size500\\gray\\square_gray_"+str(num)+".jpg",gray)
    num=num+1
    print("완료")
