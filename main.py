import random
import pyautogui

char = "abcdefgfijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`,.!@#$%^&*()_+-=[]|;':,.?"

all_Char = [char]

pwd = pyautogui.password("Enter password")

pwd = input("Enter password: ")

sample_pwd = ""

while (sample_pwd != pwd):
    sample_pwd = random.choices(all_Char, k=len(pwd))



print("<====" + str(sample_pwd) + "====>")
if(sample_pwd == list(pwd)):
    print("Password: " + "".join(sample_pwd))
   
  

    