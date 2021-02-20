import pyautogui, time
f = open("All Star Lyrics.txt", "r")
for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

