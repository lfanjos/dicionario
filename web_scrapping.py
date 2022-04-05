import tkinter as tk
import web_scrapping_support
from tkinter.messagebox import showerror
import requests
from bs4 import BeautifulSoup as bs
import textwrap

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Dicionário")
        top.configure(background="#d9d9d9")

        self.top = top
        self.html = "https://www.dicio.com.br/{}/"

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=-0.017, rely=0.0, height=71, width=604)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 48")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Dicionário''')

        self.input_lbl = tk.Label(self.top)
        self.input_lbl.place(relx=0.033, rely=0.244, height=21, width=54)
        self.input_lbl.configure(anchor='w')
        self.input_lbl.configure(background="#d9d9d9")
        self.input_lbl.configure(compound='left')
        self.input_lbl.configure(disabledforeground="#a3a3a3")
        self.input_lbl.configure(foreground="#000000")
        self.input_lbl.configure(text='''Palavra:''')

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.117, rely=0.244, height=20, relwidth=0.14)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.bind('<Return>', self.btn_callback)

        self.input_btn = tk.Button(self.top)
        self.input_btn.place(relx=0.28, rely=0.238, height=24, width=67)
        self.input_btn.configure(activebackground="#ececec")
        self.input_btn.configure(activeforeground="#000000")
        self.input_btn.configure(background="#d9d9d9")
        self.input_btn.configure(compound='left')
        self.input_btn.configure(disabledforeground="#a3a3a3")
        self.input_btn.configure(foreground="#000000")
        self.input_btn.configure(highlightbackground="#d9d9d9")
        self.input_btn.configure(highlightcolor="black")
        self.input_btn.configure(pady="0")
        self.input_btn.configure(text='''Pesquisar''')
        self.input_btn.configure(command=self.btn_callback)

        self.meaning_txt = tk.Text(self.top)
        self.meaning_txt.place(relx=0.067, rely=0.467, relheight=0.364
                , relwidth=0.623)
        self.meaning_txt.configure(background="white")
        self.meaning_txt.configure(font="TkTextFont")
        self.meaning_txt.configure(foreground="black")
        self.meaning_txt.configure(highlightbackground="#d9d9d9")
        self.meaning_txt.configure(highlightcolor="black")
        self.meaning_txt.configure(insertbackground="black")
        self.meaning_txt.configure(selectbackground="blue")
        self.meaning_txt.configure(selectforeground="white")
        self.meaning_txt.configure(wrap="word")

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.065, rely=0.418, height=21, width=84)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Significado:''')

    def btn_callback(self, *args):
        word = self.Entry1.get()
        if not len(word):
            showerror("Campo Vazio", "Insira alguma palavra antes de continuar.")
            return True
        url = self.html.format(word)
        r = requests.get(url).content
        soup = bs(r, 'html.parser')
        meaning = soup.find_all('p', {'class': 'significado'})[0].getText()
        meaning = meaning.split('ino', maxsplit=1)
        meaning[0] = meaning[0] + 'ino'
        meaning[1] = meaning[1].split('[')

        count = 0
        for x in meaning[1]:
            if meaning[1].index(x) == 0:
                pass
            else:
                meaning[1][count] = "[" + x
            count += 1
        self.meaning_txt.delete("1.0", 'end')
        self.meaning_txt.insert(tk.END, meaning[0] + '\n\n')
        for x in meaning[1]:
            if x == ' ':
                pass
            else:
                self.meaning_txt.insert(tk.END, x)
                self.meaning_txt.insert(tk.END, "\n\n")
        print(meaning)


def start_up():
    web_scrapping_support.main()



if __name__ == '__main__':
    web_scrapping_support.main()




