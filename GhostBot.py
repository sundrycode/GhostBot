##############################
# GhostBot - 2026
# GPL-3.0 license 
# Dependencies:
# pyautogui, pynput & pygetwindow
# Version: 1.0
# By sundry Code
##############################
# Build command:
# python -m PyInstaller  --icon="ghost-bot-icon.jpg" --onefile ghostB.py

import pyautogui
from pynput import keyboard
import sys
from threading import Timer
import threading
import random
import pygetwindow as gw

interval = 0.8 # In Seconds
codeVersion = "1.0"

inRunningMode = False
locations = {}
rt = 0
menu_open = False  # True while OptionsMenu is active

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
    """Single-entry menu loop. Sets `menu_open` so additional menu requests are ignored while active."""
    global menu_open
    if menu_open:
        return
    menu_open = True
    try:
        while True:
            print("- Type 1 to show the guide/how to use. / Введите 1, чтобы показать руководство / как использовать.")
            print("- Type 2 to set the time interval between clicks. / Введите 2, чтобы установить интервал времени между щелчками.")
            print("- Press Enter to start. / Нажмите Enter, чтобы запустить программу.")
            userinput = input("> ")

            if userinput.strip().lower() in ["1", "show", "show guide", "guide", "how to", "how to use"]:
                showHowTo()
                continue

            elif userinput.strip().lower() in ["2"]:
                global interval
                print("\n Current interval: " + str(interval) + " second(s). / Текущий интервал: " + str(interval) + " секунд.")
                time = input(" Set interval between clicks (in seconds, can be decimal): Установите интервал между щелчками (в секундах): ")
                try:
                    interval = float(time)
                    print(" Interval set to: " + str(interval) + " seconds. / Интервал установлен на: " + str(interval) + " секунд. \n")
                except:
                    print( "Must be a number. Должно быть число.")
                continue

            else:
                print(">> Starting program... / Запуск программы...")
                print("> Ctrl + Alt + C: Close program / Закрыть программу")
                print("> Ctrl + Alt + S: Save a location. / Сохранить местоположение")
                print("> Ctrl + Alt + G: Start Program / Начать выполнение")
                print("> Ctrl + Alt + P: Pause Program / Приостановить программу")
                print("> Ctrl + Alt + R: Reset all saved locations / Сбросить все сохраненные местоположения")
                print("> Ctrl + Alt + M: Show this menu:  / Ctrl + Alt + M: Показать это меню снова \n")
                break
    finally:
        menu_open = False

def showHowTo():
    print(" Version: " + codeVersion)
    print(" English ")
    print("="*25)
    print(" How to use:")
    print(" - First place all the windows on your screen the way you want them. (it's important not to move them after setting the locations)")
    print(" - Set one or more locations by placing you computer cursor over the place you want it to click (use  Ctrl + Alt + S to save the location).")
    print(" - When you have all the locations set, Use Ctrl + Alt + G to begin.")
    print(" - Use Ctrl + Alt + C to stop the program and Ctrl + Alt + P to pause it.")
    print(" Hotkey list:")
    print("> Ctrl + Alt + C: Close program")
    print("> Ctrl + Alt + S: Save a location.")
    print("> Ctrl + Alt + G: Start Program")
    print("> Ctrl + Alt + P: Pause Program")
    print("> Ctrl + Alt + R: Reset all saved locations. (clears all current saved locations so you can set new ones)")
    print("> Ctrl + Alt + M: Show menu.")
    print("="*50)
    ###
    print(" Версия: " + codeVersion)
    print(" Русский ")
    print("="*25)
    print(" Как использовать:")
    print(" - Сначала расположите все окна на экране так, как вам удобно. (Важно не перемещать их после того, как вы определили их местоположение)")
    print(" - Укажите одно или несколько мест, наведя курсор мыши на нужное место на экране (используйте Ctrl + Alt + S для сохранения местоположения).")
    print(" - После того, как вы зададите все местоположения, нажмите Ctrl + Alt + G, чтобы начать.")
    print(" - Для остановки программы используйте сочетание клавиш Ctrl + Alt + C.")
    print(" Список сочетаний клавиш:")
    print("> Ctrl + Alt + C: Закрыть программу")
    print("> Ctrl + Alt + S: Сохранить местоположение.")
    print("> Ctrl + Alt + G: запустить программу")
    print("> Ctrl + Alt + P: Приостановить программу")
    print("> Ctrl + Alt + R: Сбросить все сохраненные местоположения (очищает все текущие сохраненные местоположения, чтобы вы могли установить новые)")
    print("> Ctrl + Alt + M: Показать меню.")
    print("="*50)
    return

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

def runGhostBot(): # <ctrl>+<alt>+r Run program
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
    except Exception as e:
        if e == "An error occurred: Error code from Windows: 0 - The operation completed successfully.":
            return
        else:
            print(f"An error occurred: {e}")
            print("Please contact developer for support if this error persists.")
            sys.exit()
    sys.exit()


def showMenu(): # <ctrl>+<alt>+m Show menu
    global inRunningMode, menu_open
    if menu_open:
        #print("Menu is already open. / Меню уже открыто.")
        print("- Type 1 to show the guide/how to use. / Введите 1, чтобы показать руководство / как использовать.")
        print("- Type 2 to set the time interval between clicks. / Введите 2, чтобы установить интервал времени между щелчками.")
        print("- Press Enter to start. / Нажмите Enter, чтобы запустить программу.")
        return
    if inRunningMode == True:
        print("Cannot show menu while program is running. Pausing program first... / Невозможно показать меню, пока программа работает. Сначала приостановите программу...")
        pauseAll()
    threading.Thread(target=OptionsMenu, daemon=True).start()

def pauseAll(): # <ctrl>+<alt>+p Pause program
    global inRunningMode
    if inRunningMode == False:
        print("Program is already paused. / Программа уже приостановлена.")
        return
    else:
        print('Pausing Program... / Программа приостановлена...')
        global rt
        try: # So it doesn't Error if you close it without starting it
            rt.stop()
            inRunningMode = False
        except Exception as e:
            if e == "An error occurred: Error code from Windows: 0 - The operation completed successfully.":
                return
            else:
                print(f"An error occurred: {e}")
                print("Please contact developer for support if this error persists.")
                sys.exit()

def saveLocation(): # <ctrl>+<alt>+s To save a location
    global locations
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    nextLocation = len(locations) # Get number of the next dict key
    locations.update({nextLocation:{"X": currentMouseX, "Y": currentMouseY}})
    print('Location saved / Местоположение сохранено. Location / Местоположение: X: ' + str(currentMouseX) + " Y: " + str(currentMouseY)) # tell location && save location

def resetAllLocations(): # <ctrl>+<alt>+r To reset all saved locations
    # run the blocking prompt in a background thread so the hotkey listener keeps processing key-up events
    def _reset_worker():
        global inRunningMode
        if inRunningMode == True:
            pauseAll()
            return

        x = input(" Are you sure you want to reset all saved locations? (y/n): Вы уверены, что хотите сбросить все сохраненные местоположения? (да/нет): ")
        if x.lower() in ['y', 'yes', 'д', 'да']:
            global locations
            locations = {}
            print(" All saved locations have been reset. / Все сохраненные местоположения были сброшены.")
            print(" You can now set new locations. / Теперь вы можете установить новые местоположения.\n")
        else:
            print(" Cancelled. / Отменено.\n")
            return
    threading.Thread(target=_reset_worker, daemon=True).start()


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
    '<ctrl>+<alt>+r': resetAllLocations,
    '<ctrl>+<alt>+g': runGhostBot,
    '<ctrl>+<alt>+s': saveLocation,
    '<ctrl>+<alt>+p': pauseAll,
    '<ctrl>+<alt>+m': showMenu
    }) as h:
    h.join()
