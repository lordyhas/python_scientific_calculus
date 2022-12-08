


import stat_bivar_ui as bivar
import stat_univar_ui as univar
import proba_ui
import tkinter
from tkinter import messagebox
import os


# import sys
# sys.path.append("/stat/")


# ***Foction Manage***

def presentation(screen):
    # Vernada
    f2 = ("Helvetica", -14,)
    presentation_frame = tkinter.LabelFrame(screen)
    presentation_frame.pack()  # grid(row=0,column=0,columnspan=5, pady=(5,5), padx=(15,15))
    tkinter.Label(presentation_frame, text="L2CS-21", font=f2).grid(row=0, column=0)
    tkinter.Label(presentation_frame, text="L2 Calcul Scientifique - 2021", font=f2).grid(row=1,
                                                                                                             column=0)
    tkinter.Label(presentation_frame, text="Dirigé par : Prof. NDONDO Apollinaire", font=f2).grid(row=2, column=0)

    ptf = tkinter.LabelFrame(presentation_frame)
    ptf.config(bg="blue")
    ptf.grid(row=3, column=0, padx=(10, 10), pady=(0, 5))
    tkinter.Label(ptf, text="Outil de calcul scientifique pour la statisque et la probabilité").grid(row=1, column=0)


def about_app():
    about_w = tkinter.Toplevel(mainScreen)
    about_w.title("A propos")
    about_w.minsize(260, 140)
    f2 = ("Helvetica", -14,)
    presentation_frame = tkinter.LabelFrame(about_w)
    presentation_frame.pack(padx=15, pady=15)  # grid(row=0,column=0,columnspan=5, pady=(5,5), padx=(15,15))
    tkinter.Label(presentation_frame,
                  text="Fait par : Hassan Kajila  \n"
                       + "Jacques Makabi  \n"
                       + "Martin Ntambwe \n"
                       + "Benjamin Oleko \n",
                  font=f2).grid(row=0, column=0)
    tkinter.Label(presentation_frame, text="L2 / Calcul Scientifique (L2CS v21.4)", font=f2).grid(row=1, column=0)
    tkinter.Label(presentation_frame, text="Dirigé par : Prof. NDONDO Apollinaire", font=f2).grid(row=2, column=0)
    ptf = tkinter.LabelFrame(presentation_frame)
    ptf.config(bg="blue")
    ptf.grid(row=3, column=0, padx=(10, 10), pady=(0, 5))
    tkinter.Label(ptf, text="Outil de calcul scientifique pour la statisque et la probabilité").grid(row=1, column=0)


def message_to_quit():
    ask_ = messagebox.askokcancel("Confirmation", "Voulez-vous vraiment quitter?")
    if ask_:
        window.quit()


    else:
        print("_")


def message_to_not_info():
    messagebox.showinfo("Pas d'info", "C'est ne pas fonctionnel pour l'intant")


def fs(change=True):
    window.attributes("-fullscreen", not window.attributes("-fullscreen"))
    print(type(change))
    print(change)

    if change:
        menu3.delete(6)
        menu3.insert_cascade(6, label="Normal Screen [Esc]", command=lambda: fs(False))
        window.bind('<Escape>', lambda e: fs(False))
    else:
        menu3.delete(6)
        menu3.insert_cascade(6, label="Full Screen", command=lambda: fs())
        window.unbind('<Escape>', lambda e: fs(False))


def open_guide():
    try:
        from tkPDFViewer import tkPDFViewer as pdf

        # Initializing tk
        pdf_view = tkinter.Toplevel()
        pdf_view.title("Manuel d'utilisation")
        pdf_view.iconbitmap("image.ico")
        pdf_view.geometry("620x750")
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(pdf_view, pdf_location=r"Guide.pdf", width=180, height=100)

        v2.pack()
    except Exception as e:
        print("#run time error : ", e)
        os.system("../Guide.pdf")


# ########################### Parametre de fnt ################################
window = tkinter.Tk()
window.title("Calcul Scientifique")
window.minsize(480, 360)
window.geometry("480x360")
fontHelvetica = ("Helvetica", -14, "bold")
fontCourierNew = ("Courier New", -14, "bold")

# window.config(background="")
# window.iconbitmap("image.ico")

window.bind('<space>', lambda e: about_app())

# photo = tkinter.PhotoImage(file="image.png" )
# panneau= tkinter.Label(window, image= photo)
# panneau.config(bg='systemTransparent')
# panneau.place(x="15", y="15")
mainScreen = tkinter.Frame(window)
mainScreen.pack()
# ***Widgets***
mainmenu = tkinter.Menu(window)

menu0 = tkinter.Menu(mainmenu, tearoff=0)
menu0.add_command(label="Nouveau Fichier")
menu0.add_command(label="Ouvrir", command=lambda: about_app())
menu0.add_separator()
# menu0.add_command(label="______________")
menu0.add_command(label="Enregistrer")
menu0.add_command(label="Print")
menu0.add_separator()
# menu0.add_command(label="______________")
menu0.add_command(label="Close")
menu0.add_command(label="Exit", command=message_to_quit)

menu1 = tkinter.Menu(mainmenu, tearoff=1)
menu1.add_command(label="Stat Univarié", command=lambda: univar.stat_univar(window))
menu1.add_command(label="Stat Bivariée", command=lambda: bivar.stat_bivar(window))
menu1.add_separator()
menu1.add_command(label="Dist de probabilité", command=lambda: proba_ui.main_proba(window))

menu2 = tkinter.Menu(mainmenu, tearoff=0)
menu2.add_command(label="Manuel d'utilisation", command=open_guide)
menu2.add_command(label="A propos", command=about_app)

menu3 = tkinter.Menu(mainmenu, tearoff=0)
menu3.add_command(label="Format ")
menu3.add_separator()
menu3.add_command(label="480x360", command=lambda: window.geometry("480x360"))
menu3.add_command(label="640x480", command=lambda: window.geometry("640x480"))
menu3.add_command(label="820x560", command=lambda: window.geometry("820x560"))

menu3.add_separator()
menu3.add_command(label="Full Screen", command=lambda: fs())

menuz = tkinter.Menu(mainmenu, tearoff=0)
menuz.add_command(label="About", command=about_app)

mainmenu.add_cascade(labe="Fichier", menu=menu0)
mainmenu.add_cascade(label="Calcul", menu=menu1)
mainmenu.add_cascade(label="Format", menu=menu3)
# mainmenu.add_cascade(label="Info ",menu=menuz)
mainmenu.add_cascade(label="Info", menu=menu2)

mainframe0 = tkinter.Frame(mainScreen)
mainframe1 = tkinter.LabelFrame(mainScreen, text="Menu Calcul", borderwidth=2)
mainframe2 = tkinter.Frame(mainScreen, width=240, height=180, borderwidth=5)

# rool = tkinter.Scale(mainScreen)
btn1 = tkinter.Button(mainframe1, text="Statistique univariée", borderwidth=5, highlightthickness=3, width=30,
                      command=lambda: univar.stat_univar(window))
btn2 = tkinter.Button(mainframe1, text="Statistique bivariée", borderwidth=4, highlightthickness=3, width=30,
                      command=lambda: bivar.stat_bivar(window))
btn3 = tkinter.Button(mainframe1, text="Distribution de probabilité", borderwidth=4, highlightthickness=3, width=30,
                      command=lambda: proba_ui.main_proba(window))

mainframe0.pack(pady=5)  # .grid(row=1,column=1,columnspan=2)
mainframe1.pack()  # .grid(row=2,column=0)
mainframe2.pack()  # .grid(row=2,column=1)
presentation(mainframe0)

#       Frame1
tkinter.Label(mainframe1, text=" ---    Statistique descriptive    --- ").pack(pady=(5, 0))
btn1.pack(pady=(2, 2), padx=15)
btn2.pack(pady=2, padx=15)
tkinter.Label(mainframe1, text="---    Probabilité    --- ").pack()
btn3.pack(pady=2, padx=15)

# ***Loop***
window.config(menu=mainmenu)
window.protocol("WM_DELETE_WINDOW", message_to_quit)
window.mainloop()

"""<<<×>>>"""
