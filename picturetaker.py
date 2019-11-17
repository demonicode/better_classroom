import cv2
import requests
import base64
import json
import urllib.parse
import urllib.request

imageUrl = 'http://127.0.0.1:5000/image'

def check_sadness(emotions):
    if (emotions['sadness']>0.6 or emotions['surprise']>0.6 or (emotions['neutral']>0.7 and emotions['sadness']>0.4)):
        print('getting bored')
    else:
        print("not boring")

def upload(frame):
    data = {}
    img = cv2.imencode('.jpg', frame)[1]
    data['image'] = base64.b64encode(img).decode()
    results = requests.post(url=imageUrl, json=data)
    print(results.json())
    #check_sadness(results.json())

cam = cv2.VideoCapture(0)
cv2.namedWindow('Press space to take a photo')

while True:
    ret, frame = cam.read()
    cv2.imshow('Press space to take a photo', frame)
        
    key = cv2.waitKey(1)
    if key%256 == 32:
        upload(frame)
        break

cam.release()
cv2.destroyAllWindows()