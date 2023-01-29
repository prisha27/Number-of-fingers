import cv2
import time
import os
import handgesturemodule as hgm

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(5, 480)
cap.set(10, 150)

folderPath = "fingers_names"
myList = os.listdir(folderPath)
print(myList)
listimges = []
for imgpath in myList:
    image = cv2.imread(f'{folderPath}/{imgpath}')

    listimges.append(image)

print(len(listimges))
detector = hgm.handDetector()

upfinger = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lml = detector.findPosition(img, draw=False)

    if len(lml) !=0:
        finger = []

        if lml[upfinger[0]][1] > lml[upfinger[0]-1][1]: #thumb
            finger.append(1)
        else:
            finger.append(0)


        for id in range (1,5):

            if lml[upfinger[id]][2] < lml[upfinger[id]-2][2]:
                  finger.append(1)
            else:
                 finger.append(0)

        tfing = finger.count(1)
        print(tfing)

        ht, wt, ch = listimges[tfing].shape
        img[0:ht, 0:wt] = listimges[tfing]

        cv2.rectangle(img, (20,255), (170,425),(0,255,0), cv2.FILLED)
        cv2.putText(img, str(tfing), (45,375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255,0,0), 25)


        cv2.imshow("output", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                   break

