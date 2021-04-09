
# function to take user's code, print it out, then put it in a file
def outputcode():
	print("Your code is %s" % codeline)
	open("%s.py" % filename, "a")
	f.write("%s" % codeline)
	continueorend = input("Are more actions necessary?: ")


print(r'''\
        _
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

# question to either begin or quit before starting
initiateprog = input("Do you want a task automated?: ")

# if user wants to continue the script will
if initiateprog == yes or y:
    filename = input("What should we name the file?: ")
    open("%s.py" % filename, "a")
	f.write('''import os
	import webbrowser
	import pyautogui
	''')

    # continue to ask questions until task is automated
    while continueorend == y:
        command = input("What must we do now?: ")
       
        if command == "openfile":
			ofile = input('What is the path to the file?: ')
			codeline = subprocess.Popen(r"%s" % ofile)
			outputcode()
		
		elif command == "adminopenfile":
			afile = input("What program do you want admin to open?: ")
			codeline = (''' pyautogui.keyDown('winright')
            pyautogui.press('r')
            pyautogui.keyUp('winright')
            pyautogui.write(%s''' % afile''')
            pyauotgui.press('enter')
            pyautogui.press('left')
            pyauotgui.press('enter')
            ''')
            codeline = subprocess.Popen(r"%s" % ofile)
            outputcode()
        
        elif command == "hotkey":
			hk ("what keys? ex. ctrl alt fn f4: ")
			codeline = ('''pyautogui.hotkey("%s")''' % hk)
		
		elif command == "type":
			write = input("what do you need to type?: ")
			codeline = ('''pyautogui.write("%s")''' % write)
			outputcode()
		
		elif command == "search":
			google = input("What do you want to search for?: ")
			codeline = ('''webbrowser.open_new_tab("%S"''' %s google)
			outputcode()
		
		elif command == "createfile":
			cfname = input("What should we name the file?: ")
			cflocate = input("What path this file have?: ")
			codeline = ('''os.system("cd %s")
			open("%s", "x")''' %s cflocate, %s cfname)
			outputcode()
			
		elif command == "pyrun":
			pyname = input("What's the file's name?: ")
			pylocate = input("What's the file's path?: ")
			codeline = ('''os.system("cd %s")
			os.system("python %s")''' %s pylocate, %s pyname)
			outputcode()

		else: print("That doesn't seem to be one of our commands, if you want to request a feature feel free to drop a comment on my github")
		
else:
	print("See ya later")
	exit()
