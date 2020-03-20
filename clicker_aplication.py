from tkinter import *
import time
from tkinter import messagebox
import pyautogui
from pynput.mouse import Listener
from pynput import keyboard

clics = []
seconds: int = 0
bg = "#353c4a"
bg2 = "#495666"
fg = "#fff"


def startGUI():
    global window
    window = Tk()
    window.title("Clicker")
    window.resizable(width=0, height=0)
    window.config(bg=bg)
    window.iconphoto(False, PhotoImage(file='clickerIcon.png'))

    canvas = Canvas(height=100, bg=bg, highlightthickness=0)
    canvas.pack(expand=YES, fill=BOTH)
    gif1 = PhotoImage(file='clickerLogo.png')
    canvas.create_image(50, 10, image=gif1, anchor=NW)

    # lbl = Label(window, text="Clicker", font=("Arial Bold", 24), bg=bg, fg=fg)
    # lbl.pack()

    frameMain = Frame(bg=bg)
    frameMain.pack()

    frame2 = Frame(frameMain, pady=12, padx=8, bg=bg)
    frame2.grid(column=0, row=0)

    lbl = Label(frame2, text="Time: ", font=("Arial Bold", 10), bg=bg, fg=fg)
    lbl.grid(column=0, row=0)

    global spin
    spin = Spinbox(frame2, from_=0, to=100, width=10, bg=bg2, fg=fg, highlightthickness=0)
    spin.grid(column=1, row=0)
    spin.focus_set()

    lbl = Label(frame2, text="seconds", font=("Arial Bold", 10), bg=bg, fg=fg)
    lbl.grid(column=2, row=0)

    global listBox
    listBox = Listbox(frameMain, font=("Arial Bold", 12), bg=bg2, fg=fg, highlightthickness=0)
    listBox.grid(column=0, row=1)

    frame = Frame(frameMain, pady=8, padx=8, bg=bg)
    frame.grid(column=1, row=1)

    btnAdd = Button(frame, width=10, height=1, text="Add", font=("Arial Bold", 10), command=addClic, bg="#5564eb",
                    fg=fg)
    btnAdd.pack()
    btnDelete = Button(frame, width=10, height=1, text="Delete", font=("Arial Bold", 10), command=deleteClic,
                       bg="#e30052", fg=fg)
    btnDelete.pack()
    btnClear = Button(frame, width=10, height=1, text="Clear", font=("Arial Bold", 10), command=clearClics,
                      bg="#dc2d22", fg=fg)
    btnClear.pack()
    global btnStart
    btnStart = Button(frame, width=10, height=2, text="START", font=("Arial Bold", 10), command=startClicking,
                      bg="#308446", fg=fg)
    btnStart.pack()

    global lbl2
    lbl2 = Label(window, text="Remember to press ESC to finish clicking", font=("Arial Bold", 10), bg=bg, fg=fg, pady=8)
    lbl2.pack()

    message = messagebox.showwarning("Remember", "Remember to press ESC to finish clicking")

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
    window.iconify()
    with Listener(on_click=on_click) as listener:
        listener.join()
    updateList()
    window.deiconify()


def startClicking():
    if len(clics) == 0:
        lbl2.config(text="There are not clics", fg="red")
    else:
        window.iconify()
        listener = keyboard.Listener(
            on_press=on_key_pressed)
        listener.start()
        # res = messagebox.askyesno('Confirmation', 'Are you sure to start clicking?')
        # time.sleep(1)
        while listener.is_alive():
            for i in clics:
                pyautogui.click(i[0], i[1])
            time.sleep(int(spin.get()))
        window.deiconify()


def deleteClic():
    if len(listBox.curselection()) > 0:
        clics.pop(listBox.curselection()[0])
    updateList()


def clearClics():
    clics.clear()
    updateList()


if __name__ == '__main__':
    startGUI()
