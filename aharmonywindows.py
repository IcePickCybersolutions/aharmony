import pyautogui
import os

print(r"""\
       | |
   __ _| |__   __ _ _ __ _ __ ___   ___  _ __  _   _
  / _` | '_ \ / _` | '__| '_ ` _ \ / _ \| '_ \| | | |
 | (_| | | | | (_| | |  | | | | | | (_) | | | | |_| |
  \__,_|_| |_|\__,_|_|  |_| |_| |_|\___/|_| |_|\__, |
                                                __/ |
                                               |___/
""")
print('''
Proudly a creation of IcePickCybersolutions.
Visit my github repo for help, or to file a complaint.

Run the script, answer a couple questions, and voila!
You've automated a task!

Upon the prompt simply tell me what you want to do.

For example if you want to:
- open a file = openfile
- open a file with admin priveleges = adminopenfile
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
    # create a file with the name from filename

    # continue to ask questions until task is automated
    while continueorend == yes or y:
        command = input("What must we do now?: ")
        # save command to a file
