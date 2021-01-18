from tkinter import *
from PIL import ImageTk, Image
import time
import webbrowser
import threading
import cv2

window = Tk()
def videoWindow():
    video = Listbox(window)

    camera = cv2.VideoCapture("/home/reeves/Videos/jwb_E_202010_14_r360P.mp4")

    if camera.isOpened() == False:
        Label(video, text='error opening video file')

    while camera.isOpened():
        ret, frame = camera.read()
        if ret == True:
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    camera.release()

    # Closes all the frames
    cv2.destroyAllWindows()


def urlReirect():
    url = 'http://www.tfp.is'
    webbrowser.open(url, new=1)


def imageWindow():
    imageW = Toplevel(window)

    imageW.title('Image')

    loadimage = Image.open("/home/reeves/Pictures/me.jpg")
    render = ImageTk.PhotoImage(loadimage)

    image = Label(imageW, image=render, bd=0)
    image.image = render
    image.pack(fill=BOTH, expand=YES)


def urlWindow():
    urlW = Toplevel(window)

    urlW.title('Url')

    urlW.geometry('200x200')

    Button(urlW, text="Click to visit url",
           command=urlReirect).pack()  # open the URL using default browser on button click.


def textWindow():
    text = Toplevel(window)

    text.title('Text')

    text.geometry('200x200')

    Label(text, text="This is a text!").pack()


def dropDownFunction(arg):

    time.sleep(5)
    textWindow()
    time.sleep(10)
    urlWindow()
    time.sleep(15)
    imageWindow()
    time.sleep(20)
    videoWindow()


window.title("Kinter demo app")
window.geometry('500x350')

variable = StringVar(window)
variable.set("Menu")

x = threading.Thread(target=dropDownFunction, args=(1,))
x.start()

dropDownMenu = OptionMenu(window, variable, 'slab 1', command=dropDownFunction)
dropDownMenu.pack()
dropDownMenu.config(width=20)
dropDownMenu.place(x=10, y=10)

window.mainloop()
