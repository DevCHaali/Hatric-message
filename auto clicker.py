import pyautogui
import time as t
import webbrowser as web
from termcolor import colored

print('   Staring Script ..')
logo = """
    _____ _______  __              _____                    _
            __  / / /  ______ _    __  /_   ________    ___(_)  _______
           __  /_/ /   _  __ `/    _  __/   __  ___/    __  /   _  ___/
           _  __  /    / /_/ /     / /_     _  /        _  /    / /__
          /_/ /_/     \__,_/      \__/     /_/         /_/     \___/
   
                                         

                                         | - - - [+] Coding Youtube @ HC__Hacker__ :
                                                  https://www.youtube.com/channel/UCPFL-picNdanmhCLatBY8oQ  - - - - |

                                         | - - - [+] Github: https://github.com/DevCHaali/  - - - |

   
   
   """


print(colored(logo, 'blue'))
t.sleep(4)
print(colored('   Wait .......','red'))
t.sleep(3)
print(colored("  Write you word :",'yellow'))
word=input()
print(colored("   How often do you want to repeat it ?",'green'))
once=int(input())
t.sleep(1)
print
count=0
print(colored('  Wait 5 seconde and launche app','white'))
t.sleep(2)
print("   How many seconds between a message and a message")
sec = float(input())
while count<=once:
    t.sleep(sec)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    count=count+1

t.sleep(2)    
print("         Finsh")
t.sleep(2)
print(colored('            Thanks for using This Script','magenta'))
t.sleep(2)

by = """ 
                                                            by Chaali Hamza
"""
print(by)
t.sleep(2)
web.open_new('https://github.com/DevCHaali/')
web.open_new('https://www.youtube.com/channel/UCPFL-picNdanmhCLatBY8oQ')
exit()
