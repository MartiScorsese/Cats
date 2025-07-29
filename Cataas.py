from email.mime import image
from http.client import responses
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image.data = BytesIO(response.content)
        img = Image.open(image)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


window = Tk()
window.title('Cats!')
window.geometry('600x480')

label = Label(window, text='Cats!')
label.pack()

url = 'https://cataas.com/cat'
img = load_image(ulr)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
