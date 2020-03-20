from tkinter import *
import time
import pyautogui
import array
from pynput.mouse import Listener
from pynput import keyboard

clics = []
seconds: int = 0


def startGUI():
    window = Tk()
    window.title("Clicker")
    window.config(padx=16, pady=16)

    lbl = Label(window, text="Clicker", font=("Arial Bold", 24))
    lbl.pack()

    frameMain = Frame()
    frameMain.pack()

    frame2 = Frame(frameMain, pady=8, padx=8)
    frame2.grid(column=0, row=0)

    lbl = Label(frame2, text="Time: ", font=("Arial Bold", 10))
    lbl.grid(column=0, row=0)

    global spin
    spin = Spinbox(frame2, from_=0, to=100, width=10)
    spin.grid(column=1, row=0)

    lbl = Label(frame2, text="seconds", font=("Arial Bold", 10))
    lbl.grid(column=2, row=0)

    global listBox
    listBox = Listbox(frameMain, font=("Arial Bold", 12))
    listBox.grid(column=0, row=1)

    frame = Frame(frameMain, pady=8, padx=8)
    frame.grid(column=1, row=1)

    btnAdd = Button(frame, width=10, height=1, text="Add", font=("Arial Bold", 10), command=addClic)
    btnAdd.pack()
    btnDelete = Button(frame, width=10, height=1, text="Delete", font=("Arial Bold", 10), command=deleteClic)
    btnDelete.pack()
    btnClear = Button(frame, width=10, height=1, text="Clear", font=("Arial Bold", 10), command=clearClics)
    btnClear.pack()
    global btnStart
    btnStart = Button(frame, width=10, height=2, text="START", font=("Arial Bold", 10), command=startClicking)
    btnStart.pack()

    lbl2 = Label(window, text="Remember to press ESC to finish", font=("Arial Bold", 10))
    lbl2.pack()

    window.mainloop()


def updateList():
    listBox.delete(0, END)
    for num, point in enumerate(clics, start=0):
        listBox.insert(num, "Clic {}: {}".format(num + 1, point))


def on_click(x, y, button, pressed):
    if pressed:
        clics.append([x, y])
        return False


def on_key_pressed(key):
    if key == keyboard.Key.esc:
        return False


def addClic():
    with Listener(on_click=on_click) as listener:
        listener.join()
    updateList()


def startClicking():
    if len(clics) == 0:
        print("There are not any clics")
    else:
        listener = keyboard.Listener(
            on_press=on_key_pressed)
        listener.start()
        while listener.is_alive():
            for i in clics:
                pyautogui.click(i[0], i[1])
            time.sleep(int(spin.get()))


def deleteClic():
    clics.pop(listBox.curselection()[0])
    updateList()


def clearClics():
    clics.clear()
    updateList()


if __name__ == '__main__':
    startGUI()
