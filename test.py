import cv2
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# Read the video from specified path
cam = cv2.VideoCapture('video1.mp4')
#cam = cv2.VideoCapture('video2.mp4')

# try:
#
#     # creating a folder named data
#     if not os.path.exists('data'):
#         os.makedirs('data')
#
#     # if not created then raise error
# except OSError:
#     print('Error: Creating directory of data')

# frame
#currentframe = 0

file = open('data1.txt', 'w')
tempx = 2;

while (True):

    data = ""
    # reading from frame
    ret, frame = cam.read()

    if ret:
        if ( tempx > 0 ):
            tempx -= 1
            continue
        else:
            tempx = 2
            # if video is still left continue creating images
            #name = './data/frame' + str(currentframe) + '.jpg'
            #print('Creating...' + name)

            # writing the extracted images
            #cv2.imwrite(name, frame)

            img = frame
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            hImg, wImg, _ = img.shape
            boxes = pytesseract.image_to_data(img)
            print(boxes)
            for a, b in enumerate(boxes.splitlines()):
                print(b)
                if (a != 0):
                    b = b.split()
                    print(b)
                    if len(b) == 12:
                        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                        cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
                        cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
                        data += b[11] + " "





            cv2.imshow('Result', img)
            cv2.waitKey(1)
            # increasing counter so that it will
            # show how many frames are created
            #currentframe += 1
            print(data)
            file.write(data + '\n')

    else:
        break


file.close()
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()



# we can use image to string to get raw data
#print(pytesseract.image_to_string(img))

# ### Detecting character
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#    print(b)
#    b = b.split(' ')
#    print(b)
#    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
#    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)


### Detecting words
# hImg,wImg,_ = img.shape
# boxes = pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     #print(b)
#     if ( x!= 0):
#         b = b.split()
#         print(b)
#         if len(b)==12:
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
#
# cv2.imshow('Result',img)
# cv2.waitKey(0)
