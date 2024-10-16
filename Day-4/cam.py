# # pip install opencv-contrib-python
# import cv2
# cam = cv2.VideoCapture(0)
# while True:
#     _, frame = cam.read() # camera টা  read করার try করব। এটা ২ টা  ভ্যারিয়েবল দিবে প্রথম টা কে আমরা _ দিয়ে declare করলাম, আরেকটা কে আমরা frame দিয়ে declare করলাম 
#     cv2.imshow('my cam',frame) # তারপর cv2 কে বলা হলো image টা  কে show করার জন্য । আর আমার frame টা  কে দেখানোর জন্য frame লিখে দিলাম 
#     cv2.waitKey(1) # কত মিলি সেকেন্ড wait করাবো 
    

import cv2
cam = cv2.VideoCapture(0)
while True:
    _,frame = cam.read()
    cv2.imshow('my cam' , frame)
    cv2.waitKey(1)