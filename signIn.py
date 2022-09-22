import time
import pyautogui
from datetime import datetime
print("腾讯会议自动签到（MacOS适用）")
while True:
    print(datetime.now())
    isSuccess=False
    signin = pyautogui.locateCenterOnScreen('signin.png',grayscale=False,confidence=0.8)  # 检测发起签到
    if signin is not None:
        print("检测到签到发起，执行自动签到。")
        while True:
            if isSuccess:
                break
            print("检测\"打开应用\"按钮")
            openapp = pyautogui.locateCenterOnScreen('openapp.png', grayscale=False, confidence=0.8)  # "打开应用"按钮
            if openapp is not None:
                print(openapp)
                x,y=openapp
                pyautogui.moveTo(x*0.5,y*0.5)  # 鼠标移动  *0.5是为了hidpi引起的显示大小与渲染大小不同导致的实际坐标问题。
                time.sleep(0.2)
                pyautogui.click()  # 单击一下
                while True:
                    openapp = pyautogui.locateCenterOnScreen('openapp.png', grayscale=False,confidence=0.8)  # 检测是否还存在"打开应用"按钮，以防未进入签到应用
                    if openapp is not None:
                        break
                    print("检测\"点击签到\"按钮")
                    signinbtn = pyautogui.locateCenterOnScreen('signinbtn.png', grayscale=False, confidence=0.9)  # "点击签到"按钮
                    if signinbtn is not None:
                        print(signinbtn)
                        x, y = signinbtn
                        pyautogui.moveTo(x * 0.5, y * 0.5)  # 鼠标移动  *0.5是为了hidpi引起的显示大小与渲染大小不同导致的实际坐标问题。
                        time.sleep(0.2)
                        pyautogui.click()  # 单击一下
                    print("检测是否成功")
                    success = pyautogui.locateCenterOnScreen('success.png', grayscale=False,confidence=0.8)  # 签到结果
                    if success is not None:
                        print("本次签到完成，等待下次签到。")
                        isSuccess=True
                        break
                    time.sleep(1)
            time.sleep(1)
        time.sleep(1)
    time.sleep(3)  # 等待3s
