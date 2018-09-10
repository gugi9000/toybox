import pyautogui
import time

delay_small = 0.3
delay_medium = 0.5
delay_big = 1
message_codes_number = 0

for i in range(220, 240, 1):
    time.sleep(delay_medium)
    istr = str(i)
    pyautogui.click(38, 198, 1, delay_small)
    pyautogui.click(787, 243, 1, delay_small)
    pyautogui.press('e')
    pyautogui.click(787, 243, 1, delay_big)
    pyautogui.click(761, 268, 1, delay_small)
    pyautogui.click(761, 268, 1, delay_small)
    pyautogui.typewrite(istr)
    pyautogui.click(853, 310, 1, delay_small)
    message_codes_number += 1
print(message_codes_number, 'message codes were added, please check if data was added without errors before proceeding')
