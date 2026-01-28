##############################
# GhostBot - 2026
# GPL-3.0 license 
# Dependencies:
# pyautogui, pynput & pygetwindow
# Version: 0.6
# By sundry Code
##############################
# Build command:
# python -m PyInstaller  --icon="ghost-bot-icon.jpg" --onefile ghostB.py

import pyautogui
from pynput import keyboard
import sys
from threading import Timer
import random
import pygetwindow as gw

interval = 1 # In Seconds
codeVersion = "0.6"

inSetLocationMode = False
inRunningMode = False
locations = {}
rt = 0

# Show the how to info
def main():
    print("""
            88                                          88                              
            88                                  ,d      88                       ,d     
            88                                  88      88                       88     
 ,adPPYb,d8 88,dPPYba,   ,adPPYba,  ,adPPYba, MM88MMM   88,dPPYba,   ,adPPYba, MM88MMM  
a8"    `Y88 88P'    "8a a8"     "8a I8[    ""   88      88P'    "8a a8"     "8a  88     
8b       88 88       88 8b       d8  `"Y8ba,    88      88       d8 8b       d8  88     
"8a,   ,d88 88       88 "8a,   ,a8" aa    ]8I   88,     88b,   ,a8" "8a,   ,a8"  88,    
 `"YbbdP"Y8 88       88  `"YbbdP"'  `"YbbdP"'   "Y888   8Y"Ybbd8"'   `"YbbdP"'   "Y888  
 aa,    ,88                                                                           
  "Y8bbdP"                           
    """)
    print(" Version: " + codeVersion)
    OptionsMenu()



def OptionsMenu():
    print("- Type 1 to show the guide/how to use. / Введите 1, чтобы показать руководство / как использовать.")
    print("- Type 2 to set the time interval between clicks. / Введите 2, чтобы установить интервал времени между щелчками.")
    print("- Press Enter to start. / Нажмите Enter, чтобы запустить программу.")
    userinput = input("> ")
    if userinput.lower() in [1, "1", "show", "show guide", "guide", "how to", "how to use"]:
        showHowTo()
    elif userinput.lower() in [2, "2"]:
        global interval
        print("\n Current interval: " + str(interval) + " second(s). / Текущий интервал: " + str(interval) + " секунд.")
        time = input(" Set interval between clicks (in seconds): Установите интервал между щелчками (в секундах): ")
        try:
            interval = float(time)
            print(" Interval set to: " + str(interval) + " seconds. / Интервал установлен на: " + str(interval) + " секунд. \n")
            OptionsMenu()
        except:
            print( "Must be a number. Должно быть число.")
            OptionsMenu()
    else:
        print(" Starting program... / Запуск программы...")
        print("> Ctrl + Alt + C: Close program / Закрыть программу")
        print("> Ctrl + Alt + L: Enter set location mode. / Перейти в режим установки местоположения")
        print("> Ctrl + Alt + S: Save a location (When in set location mode). / Сохранить местоположение (если вы находитесь в режиме установки местоположения).")
        print("> Ctrl + Alt + G: Go at them (i.e start) / Начать выполнение")
        print("> Ctrl + Alt + P: Pause Program / Приостановить программу")

def showHowTo():
    print(" Version: " + codeVersion)
    print(" English ")
    print("="*25)
    print(" How to use:")
    print(" - First place all the windows on your screen the way you want them. (it's important not to move them after setting the locations)")
    print(" - Second Enter location mode (Ctrl + Alt + L) and set one or more locations by placing you computer  cursor over the place you want it to click (use  Ctrl + Alt + S to save the location).")
    print(" - When you have all the locations set, Use Ctrl + Alt + G to begin.")
    print(" - Use Ctrl + Alt + C to stop the program and Ctrl + Alt + P to pause it.")
    print(" Hotkey list:")
    print("> Ctrl + Alt + C: Close program")
    print("> Ctrl + Alt + L: Enter set location mode.")
    print("> Ctrl + Alt + S: Save a location (When in set location mode).")
    print("> Ctrl + Alt + X: Exit set location mode.")
    print("> Ctrl + Alt + G: Go at them (i.e start)")
    print("> Ctrl + Alt + P: Pause Program")
    print("="*50)
    ###
    print(" Версия: " + codeVersion)
    print(" Русский ")
    print("="*25)
    print(" Как использовать:")
    print(" - Сначала расположите все окна на экране так, как вам удобно. (Важно не перемещать их после того, как вы определили их местоположение)")
    print(" - Во-вторых, перейдите в режим определения местоположения. (Ctrl + Alt + L). Укажите одно или несколько мест, наведя курсор мыши на нужное место на экране (используйте Ctrl + Alt + S для сохранения местоположения).")
    print(" - После того, как вы зададите все местоположения, нажмите Ctrl + Alt + G, чтобы начать.")
    print(" - Для остановки программы используйте сочетание клавиш Ctrl + Alt + C.")
    print(" Список сочетаний клавиш:")
    print("> Ctrl + Alt + C: Закрыть программу")
    print("> Ctrl + Alt + L: Перейдите в режим настройки мест нажатия на экране.")
    print("> Ctrl + Alt + S: Сохранить местоположение (работает только в режиме выбора местоположения).")
    print("> Ctrl + Alt + X:Выйти из режима выбора местоположения.")
    print("> Ctrl + Alt + G: запустить программу")
    print("> Ctrl + Alt + P: Приостановить программу")
    print("="*50)
    OptionsMenu()

def run():
    total = len(locations)
    for i in range(0, total):
        X = locations[i]["X"]
        Y = locations[i]["Y"]
        shouldClick = True 
        if shouldClick == True:
            # Define the coordinates of the window you want to activate
            # (e.g., the top-left corner of the window)
            x_coord = X
            y_coord = Y

            # Get a list of window objects at the specified coordinates
            windows_at_location = gw.getWindowsAt(x_coord, y_coord)

            if windows_at_location:
                # Get the first window in the list (usually the topmost/most relevant one)
                window_to_activate = windows_at_location[0]

                # Activate the window
                try:
                # Code that might raise an exception
                    window_to_activate.activate()
                except Exception as e:
                    # 'e' is a variable holding the exception instance
                    print(f"An error occurred: {e}") 
                
                # Optional: Wait a moment to observe the change
                #time.sleep(2)
            else:
               print("Error (ошибка)")
               print(f"No window found at coordinates ({x_coord}, {y_coord}).")
              
            ran1 = random.randint(1, 10)
            ran2 = random.randint(1, 10)
            if random.random() % 2 == 0:
               print("clicked (нажато): X: " + str(X+ran1) + " Y: " + str(Y+ran2))
               pyautogui.click(button='left', x=X+ran1, y=Y+ran2)
            else:
                print("clicked (нажато): X: " + str(X+ran1) + " Y: " + str(Y+ran2))
                pyautogui.click(button='left', x=X-ran1, y=Y-ran2)

def getColor(X, Y):
    screenshot = pyautogui.screenshot()
    pic = screenshot.load()
    return pic[X,Y]

def runGhostBot(): # <ctrl>+<alt>+r Run program
    # Exit Location mode if in it
    global inSetLocationMode
    if inSetLocationMode == True:
        print('Exiting Set location mode... (Выход из режима установки местоположения...)')
        inSetLocationMode = False
    # Run program
    if len(locations) != 0: # Make sure they have at least one location saved
        print('Starting GhostBot... (Начало)')
        global inRunningMode
        if inRunningMode == False:
            inRunningMode = True
            global rt
            rt = RepeatedTimer(interval, run) # it auto-starts, no need of rt.start()
    else:
        print("You must set at least one location! (Необходимо указать хотя бы одно местоположение!)\n")

def closeProgram(): # <ctrl>+<alt>+c Close program
    print('Closing GhostBot... (завершение программы)')
    global rt
    try: # So it doesn't Error if you close it without starting it
        rt.stop()
    except:
        print("Error")
        sys.exit()
    sys.exit()

def pauseAll():
    print('Pausing Program... (Программа приостановлена...)')
    global rt
    try: # So it doesn't Error if you close it without starting it
        rt.stop()
        global inRunningMode
        inRunningMode = False
    except:
        print("Error")
        sys.exit()

def enterLocationMode(): # <ctrl>+<alt>+l Set location mode
    global inSetLocationMode
    if inSetLocationMode == False:
        print('Entering Set location mode... (Включение режима выбора местоположения...)')
        inSetLocationMode = True

def saveLocation(): # <ctrl>+<alt>+s To save a location (When in set location mode)
    if inSetLocationMode == True:
        global locations
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        nextLocation = len(locations) # Get number of the next dict key
        color = getColor(currentMouseX, currentMouseY)
        update = {nextLocation:{"X": currentMouseX, "Y": currentMouseY, "color": color}} 
        locations.update({nextLocation:{"X": currentMouseX, "Y": currentMouseY, "color": color}})
        print('Location saved. Location: X: ' + str(currentMouseX) + " Y: " + str(currentMouseY)) # tell location && save location
        print('Местоположение сохранено. Местоположение: ' + str(currentMouseX) + " Y: " + str(currentMouseY)) # tell location && save location
        
    else:
        print('Must be in set location mode to save a new location. (Для сохранения нового местоположения необходимо находиться в режиме выбора местоположения.)')

def exitLocationMode(): 
    global inSetLocationMode
    if inSetLocationMode == True:
        print('Exiting Set location mode... (Выход из режима выбора местоположения...)')
        inSetLocationMode = False

# Timer 
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()
    
    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)
    
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True
    
    def stop(self):
        self._timer.cancel()
        self.is_running = False

main()


# Hotkey handlers
with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+c': closeProgram,
    '<ctrl>+<alt>+l': enterLocationMode,
    '<ctrl>+<alt>+g': runGhostBot,
    '<ctrl>+<alt>+s': saveLocation,
    '<ctrl>+<alt>+x': exitLocationMode,
    '<ctrl>+<alt>+p': pauseAll,
    }) as h:
    h.join()
