import os
import time
import hashlib
import pyautogui

print("################ PASSWORD HACKING ####################### \n")
# to check if the password is found or not in the text file.
password_found = 0
input_hash = input("ENTER sha256 hash of the victim \n")
try:
    passfile = open("10-million-password-list-top-1000000.txt", "r")
except:
    print("PASSCODE FILE NOT FOUND!!")
    time.sleep(3)
    quit()

time.sleep(5)
for password in passfile:
    encode_password = password.encode('utf-8')
    digest = hashlib.sha256(encode_password.strip()).hexdigest()
    new_passcode = f"password = {digest}"
    # pyautogui.write(new_passcode, interval=0.2)
    # pyautogui.press("enter")
    # time.sleep(1)

    if input_hash == digest:
        print('PASSWORD FOUND!')
        print(f"PASSWORD IS {password} \n")
        password_found = 1
        time.sleep(3)
        print("########### THANK YOU ##############")
        break

if not password_found:
    print("PASSWORD NOT FOUND IN THE PASSCODE FILE!! \n")
    print("########### THANK YOU ##############")
