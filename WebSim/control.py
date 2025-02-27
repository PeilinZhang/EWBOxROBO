import requests
import time
import os
from PIL import Image

SERVER_URL = "http://127.0.0.1:5000"

def move_car(direction):
    response = requests.post(f"{SERVER_URL}/move", json={"direction": direction})
    print(response.json())

def capture_screenshot():
    response = requests.get(f"{SERVER_URL}/screenshot")
    print(response.json())  

    time.sleep(5)

    print("Files in directory:", os.listdir())

    if "camera_view.png" in os.listdir():
        img = Image.open("camera_view.png")
        #modify the code below if you dont want to modify the image
        #or if you want to pass the image to a variable.
        img.show()
    else:
        print("Error: Screenshot not found!")

#add image processing code here (and in the capture_screenshot function)

# Example usage:
move_car("forward")
time.sleep(1)
move_car("left")
time.sleep(1)
move_car("forward")
capture_screenshot()
