import cv2
import os
import sys

try:
    label_name = sys.argv[1]
    num_samples = int(sys.argv[2])
except:
    print("Arguments missing.")
    exit(-1)

data_path = 'training_data'
type_path = os.path.join(data_path, label_name)

try:
    os.mkdir(data_path)
except FileExistsError:
    pass

try:
    os.mkdir(type_path)
except FileExistsError:
    pass

cap = cv2.VideoCapture(0)
start = False
count = 0

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(600,600))

    if not ret:
        continue
    if count == num_samples:
        break

    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 1)
    if start:
        img = frame[100:500, 100:500]
        save_path = os.path.join(type_path, '{}.jpg'.format(count + 1))
        # ret,img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(save_path, img)
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "No of Images Collected : {}".format(count),
            (120, 50), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Data Collection", frame)

    k = cv2.waitKey(1)
    if k == ord('s'):
        start = not start

    if k == ord('q'):
        break

print("{} images saved to {}".format(count, type_path))
cap.release()
cv2.destroyAllWindows()
