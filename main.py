import cv2
import mss
# import pyautogui
import time

colors = {
    "blue": "#226CA7",
    "red": "#A51E2B",
    "green": "#1E9750"
}

def screenDetection():
    with mss.MSS() as sct:
        # The screen part to capture
        # monitor = {
        #     "top": 160, 
        #     "left": 160, 
        #     "width": 160, 
        #     "height": 135
        # }
        monitor = sct.primary_monitor
        # print(monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # return sct_img.size, sct_img.width, sct_img.height, sct_img.pixel(x, y)
        return sct_img
        # return sct_img.pixel(0, 0)

def main():
    time.sleep(2.5)
    screenDetectionData = screenDetection()
    # return screenDetectionData
    print("Top-left:", screenDetectionData.pixel(0, 0))
    print("Center:", screenDetectionData.pixel(80, 67))
    print("Bottom-right:", screenDetectionData.pixel(159, 134))


def test():
    time.sleep(2.5)
    with mss.MSS() as sct:
        monitor = sct.primary_monitor
        print(monitor)

test()

# main()
# print(main())
