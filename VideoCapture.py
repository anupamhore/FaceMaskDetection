import cv2
import os
import time
import uuid

IMAGE_PATH = "Collections1"
labels= ['With Mask', 'Without Mask']
number_of_images = 140

for label in labels:
    folder = os.path.join(IMAGE_PATH, label)
    os.makedirs(folder, exist_ok=True)
    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(2)

    for idx in range(number_of_images):
        print(f'Count:{idx + 1}')
        ret, frame = cap.read()
        image_name = os.path.join(IMAGE_PATH, label, label + "_" + str(uuid.uuid1()) + ".jpg")
        if not cv2.imwrite(image_name,frame):
            raise Exception("Could not write image")
        cv2.imshow('frame',frame)
        time.sleep(2)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



