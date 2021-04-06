import pyautogui
import os
import subprocess

print(r'''\
       | |
   __ _| |__   __ _ _ __ _ __ ___   ___  _ __  _   _
  / _` | '_ \ / _` | '__| '_ ` _ \ / _ \| '_ \| | | |
 | (_| | | | | (_| | |  | | | | | | (_) | | | | |_| |
  \__,_|_| |_|\__,_|_|  |_| |_| |_|\___/|_| |_|\__, |
                                                __/ |
                                               |___/
''')
print('''
Proudly a creation of IcePickCybersolutions.
Visit my github repo for help, or to file a complaint.
Run the script, answer a couple questions, and voila!
You've automated a task!
Upon the prompt simply tell me what you want to do.
For example if you want to:
- open a file = openfile
- open a file with admin priveleges = adminfile
- use a hotkey = hotkey
- type out something = type
- search the web = search
- create a file = createfile
- run a python script = pyrun
-
''')


initiateprog = input("Do you want a task automated?: ")
if initiateprog == yes or y:
    filename = input("What should we name the file?: ")
    open("%s.py" % filename)

    # continue to ask questions until task is automated
    while continueorend == y:
        command = input("What must we do now?: ")
        if command == openfile:
			ofile = input('What is the path to the file?: ')
			codeline = subprocess.Popen(r"%s" % ofile)
			print("Your code is %s" % codeline)
			open("%s.py" % filename, "a")
			f.write("%s" % codeline)
			continueorend = input("Are more actions necessary?: ")
		elif command == adminopenfile:
			afile = input("What program do you want admin to open?: ")
			codeline = (''' pyautogui.keyDown('winright')
            pyautogui.press('r')
            pyautogui.keyUp('winright')
            pyautogui.write(%s''' % afile''')
            pyauotgui.press('enter')
            pyautogui.press('left')
            pyauotgui.press('enter')
            ''')
