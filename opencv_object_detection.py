import cv2
import time
import cvlib
from gtts import gTTS
# from playsound import playsound
from pygame import mixer
from cvlib.object_detection import draw_bbox


def speak(text):
    print(text)
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./output/items.mp3")
    
    mixer.init()
    mixer.music.load('./output/items.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    
video = cv2.VideoCapture(index=0)
labels = []

while True:
    ret, frame = video.read()
    bbox, label, conf = cvlib.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    cv2.imshow("frame", output_image)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

counter = 0
new_sentence = []
for label in labels:
    if counter==0:
        new_sentence.append(f'I found a {label}, and, ')
    else:
        new_sentence.append(f'{label}, ')

    counter += 1

speak(''.join(new_sentence))


    