"""A python module to automaticaly fish in Minecraft"""
import sys
import time

import keyboard
import pyautogui
import requests
from PIL import Image


def main():
    response = requests.get("https://i.imgur.com/Q8oDXB8.png", stream=True)
    with Image.open(response.raw) as image:
        print("Press F12 to quit the program")
        try:
            while not keyboard.is_pressed("F12"):
                loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9)
                if loc:
                    print("Fishing Bobber splashed!")
                    pyautogui.doubleClick(button='right', interval=0.5)
                    time.sleep(5)  # Prevent from clicking again before gone
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    main()
