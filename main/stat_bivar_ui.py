# <<<CODE×FISRT>>>
import tkinter as tk
from tkinter import Scrollbar, messagebox, ttk
# from stat_logic import *
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

import time
import math

global focusIndex
global isCursorOnX
global ap
global bi
global SIZE_OF_VALUE_ENTRY

#SIZE_OF_VALUE_ENTRY = 0
SIZE_OF_VALUE = 50
#isCursorOnX = True

listOfValueObs = ['#'] * SIZE_OF_VALUE
listOfValueXi = ['#'] * SIZE_OF_VALUE
listOfValueYi = ['#'] * SIZE_OF_VALUE
listOfValueEc = ['#'] * SIZE_OF_VALUE
listOfValuexyFrame = ['#'] * SIZE_OF_VALUE
xi_sqrtLabel = ['#'] * SIZE_OF_VALUE
xyFrameLabel = ['#'] * SIZE_OF_VALUE

listOfValueXY = ['#'] * SIZE_OF_VALUE


class OnKeyboard:
    def __init__(self):
        pass

    @staticmethod
    def enter_key():
        pass

    @staticmethod
    def down_key():
        pass

    @staticmethod
    def up_key():
        pass

    @staticmethod
    def r_key():
        pass


class Dialog:
    @staticmethod
    def to_quit():
        leave = messagebox.askokcancel("Confirmation",
                                       "Voullez-vous vraiment quitter?")
        if leave:
            tk.Tk().quit()

    @staticmethod
    def to_error_no_observation_value():
        messagebox.showerror("Erreur", "Veillez entrer une bonne valeur pour lancer le programme")

    @staticmethod
    def to_error_value(message=None):
        msg = "Une erreur s'est produite"
        if (message != None):
            msg = message
        messagebox.showwarning("Erreur", msg)

    @staticmethod
    def to_info():
        messagebox.showinfo("Pas d'info", "C'est ne pas fonctionnel pour l'intant")

    # def toinfo(): messagebox.showinfo("Info","Createur de l'app Hasssan TSHELEKA")
    # def tonotinfo(): messagebox.showinfo("Pas d'info","C'est ne pas fonctionnel pour l'intant")


def get_value_list(array):

    T = []
    print("####### ", SIZE_OF_VALUE_ENTRY)

    try:
        for i in range(SIZE_OF_VALUE_ENTRY):
            T.append(float(array[i].get()))
        print("List : ", T)
        return T
    except Exception as e:
        print(f"Error {e}")
        Dialog.to_error_value(message="Veuillez reverifier vos valeur (Xi, Yi)")
    return []


def stat_bivar(parent_screen):
    class RegressionResult:
        # @staticmethod
        @classmethod
        def graphique(cls):
            global ap
            global bi

            yi_list = get_value_list(listOfValueYi)
            xi_list = get_value_list(listOfValueXi)

            x = np.array(xi_list)
            y = np.array(yi_list)

            fig, axs = plt.subplots(2, 1, figsize=(5, 7), constrained_layout=True)
            fig.suptitle('Graphique et interpretation', fontsize=16)

            axs[0].plot(x, y, 'o', )
            axs[0].set_title('Nuage des points')
            axs[0].set_xlabel('axe des X')
            axs[0].set_ylabel('axe des Y')
            axs[0].grid(True)

            aux = y
            y = ap * x + bi

            axs[1].plot(x, y, '--', x, aux, 'o', )
            axs[1].set_xlabel('axe des X')
            axs[1].set_ylabel('axe des Y')
            axs[1].set_title('droite de regression')
            axs[1].grid(True)

            plt.show()

            # plt.show()

            # plt.plot(z,w, c="green")
            # plt.set_title("Graphique")
            # plt.plot(y,x, c="green")
            # plt.plot(x,z, c="red")
            # plt.show()

        @classmethod
        def sum_list(cls, array):
            if (len(array) > 0):
                r = 0
                for i in array:
                    r += i
                return r
            else:
                return -1

        @classmethod
        def corref(cls):
            yi_list = get_value_list(listOfValueYi)
            xi_list = get_value_list(listOfValueXi)
            n = SIZE_OF_VALUE_ENTRY

            xi_sqrt = cls.xi_sqrt()
            yi_sqrt = 0
            xy = cls.xy()

            for i in yi_list: yi_sqrt += (i * i)

            xi_sum = cls.sum_list(xi_list)
            yi_sum = cls.sum_list(yi_list)
            racine_x = math.sqrt(xi_sqrt - (xi_sum ** 2) / n)
            racine_y = math.sqrt(yi_sqrt - (yi_sum ** 2) / n)
            value = (xy - (xi_sum * yi_sum) / n) / (racine_x * racine_y)
            print('+-----+ :', value)

            # resultFrame4.grid(row=5, column=2, columnspan=2)
            # btnGraphique.grid(row=4, column=4, columnspan=2)

            return value

        @classmethod
        def intercept(cls, pente):

            yi_list = get_value_list(listOfValueYi)
            xi_list = get_value_list(listOfValueXi)
            xi_sum = cls.sum_list(xi_list)
            yi_sum = cls.sum_list(yi_list)
            n = SIZE_OF_VALUE_ENTRY

            value = (yi_sum / n) - (pente * (xi_sum / n))

            intercept_label.config(text="b = {:.3f}".format(value))

            return value

        @classmethod
        def pente(cls):
            xi_sqrt = cls.xi_sqrt()
            xy = cls.xy()
            yi_list = get_value_list(listOfValueYi)
            xi_list = get_value_list(listOfValueXi)

            xi_sum = cls.sum_list(xi_list)
            yi_sum = cls.sum_list(yi_list)
            n = SIZE_OF_VALUE_ENTRY

            value = (xy - (xi_sum * yi_sum) / n) / (xi_sqrt - (xi_sum ** 2) / n)

            pente_label.config(text="a = {:.3f}".format(value))

            return value

        @classmethod
        def xy(cls, ):
            yi_list = get_value_list(listOfValueYi)
            xi_list = get_value_list(listOfValueXi)
            print("xyL :", get_value_list(listOfValueXi))
            T = []

            for i in range(SIZE_OF_VALUE_ENTRY):
                xyFrameLabel[i].config(text="{:.1f}".format(xi_list[i] * yi_list[i]))
                # xyLabel[i].config(text="{:.1f}".format(xi_list[i]*yi_list[i]))
                T.append(xi_list[i] * yi_list[i])

            xy_sum = cls.sum_list(T)
            print("xy_sum :", xy_sum)
            xy_frame_label_result.config(text="{:.2f}".format(xy_sum))
            # xyLabelResult.config(text="{:.2f}".format(xy_sum))

            return xy_sum

        @classmethod
        def xi_sqrt(cls):
            xi_list = get_value_list(listOfValueXi)
            print("XiL :", get_value_list(listOfValueXi))
            array = []

            for i in range(SIZE_OF_VALUE_ENTRY):
                xi_sqrtLabel[i].config(text=f"{xi_list[i] * xi_list[i]}")
                array.append(xi_list[i] * xi_list[i])
            xi_sqrt_sum = cls.sum_list(array)
            print("xi_sqrt_sum :", xi_sqrt_sum)
            xi_sqrt_label_result.config(text="{:.2f}".format(xi_sqrt_sum))

            return xi_sqrt_sum

        @classmethod
        def covariance(cls):
            xi_sqrt_ = cls.xi_sqrt()
            xy = cls.xy()
            yi_list = get_value_list(listOfValueYi)
            xi_list = get_value_list(listOfValueXi)

            xi_sum = cls.sum_list(xi_list)
            yi_sum = cls.sum_list(yi_list)
            n = SIZE_OF_VALUE_ENTRY

            value = (xy - (xi_sum * yi_sum) / n)

            return value

        @classmethod
        def all(cls):
            """this method call all method for calculate"""
            global ap
            global bi
            yi_list = get_value_list(listOfValueYi)
            xi_list = get_value_list(listOfValueXi)
            xi_sum = cls.sum_list(xi_list)
            yi_sum = cls.sum_list(yi_list)
            pente = cls.pente()
            intercept = cls.intercept(pente)
            ap = pente
            bi = intercept
            cls.corref()

            print("yi_sum :", yi_sum)
            print("XiSum :", xi_sum)
            print("XiSum :", intercept)

            sum_yi_label.config(text=f"{yi_sum}")
            sum_xi_label.config(text=f"{xi_sum}")

    def get_value_list(array):
        T = []
        print("####### ", SIZE_OF_VALUE_ENTRY)

        try:
            for i in range(SIZE_OF_VALUE_ENTRY):
                T.append(float(array[i].get()))
            print("List : ", T)
            return T
        except Exception as e:
            print(f"Error {e}")
            Dialog.to_error_value(message="Veuillez reverifier vos valeur (Xi, Yi)")
        return []

    def set_focus_entry(index, is_x = True):
        if is_x:
            listOfValueXi[index].focus_set()
        else:
            listOfValueYi[index].focus_set()

    def down_listener():
        global focusIndex
        global isCursorOnX
        global SIZE_OF_VALUE_ENTRY

        focusIndex += 1
        if (focusIndex >= SIZE_OF_VALUE_ENTRY):
            focusIndex = 0
            isCursorOnX = not isCursorOnX

        set_focus_entry(focusIndex, isCursorOnX)
        # listOfValueYi[0].focus_set()
        print('<onFocusCursorChange> : ', focusIndex, " | isCursorOnX : ", isCursorOnX, " | Direction *DOWN")

    def up_listener():
        global focusIndex
        global isCursorOnX
        global SIZE_OF_VALUE_ENTRY

        focusIndex -= 1
        if (focusIndex < 0):
            focusIndex = SIZE_OF_VALUE_ENTRY - 1
            isCursorOnX = not isCursorOnX

        set_focus_entry(focusIndex, isCursorOnX)
        # listOfValueYi[0].focus_set()
        print('<onFocusCursorChange> : ', focusIndex, " | isCursorOnX : ", isCursorOnX, " | Direction *UP")

    def left_listener():
        global focusIndex
        global isCursorOnX

        isCursorOnX = True
        listOfValueXi[focusIndex].focus_set()
        print('<onFocusCursorChange> : ', focusIndex, " | isCursorOnX : ", isCursorOnX, " | Direction *LEFT")

    def right_listener():
        global focusIndex
        global isCursorOnX

        isCursorOnX = False
        listOfValueYi[focusIndex].focus_set()
        print('<onFocusCursorChange> : ', focusIndex, " | isCursorOnX : ", isCursorOnX, " | Direction *RIGHT")

    def generate_tab():
        global SIZE_OF_VALUE_ENTRY
        global focusIndex
        print(SIZE_OF_VALUE_ENTRY)
        if (True):

            focusIndex = 0
            SIZE_OF_VALUE_ENTRY = int(size_of_observation.get())
            print(SIZE_OF_VALUE_ENTRY)
            calculus_frame.grid(row=1, column=0, columnspan=6, padx=10)
            btn_start.config(text="Relancer")
            listOfValueXi[0].focus_set()

            ww.bind('<Down>', lambda e: down_listener())
            ww.bind('<Up>', lambda e: up_listener())
            ww.bind('<Left>', lambda e: left_listener())
            ww.bind('<Right >', lambda e: right_listener())

            for i in range(SIZE_OF_VALUE_ENTRY):
                tk.Label(observation, text=f"{i + 1}", width=10).grid(row=i, column=0)
                tk.Label(xi_frame).grid(row=i, column=0)
                tk.Label(yi_frame).grid(row=i, column=0)

                listOfValueXi[i].grid(row=i, column=1, padx=(0, 7))
                listOfValueYi[i].grid(row=i, column=1, padx=(0, 7))
                xi_sqrtLabel[i].grid(row=i, column=0)
                xyFrameLabel[i].grid(row=i, column=0)
            obs_total.config(text=f"n = {SIZE_OF_VALUE_ENTRY}")

        try:
            pass
        except Exception as e:
            Dialog.to_error_no_observation_value()

        # RegressionResult.graphique()

    def on_calculate_xy():
        global ap
        global bi
        yi_list = get_value_list(listOfValueYi)
        xi_list = get_value_list(listOfValueXi)
        if (True):
            xi_sum = RegressionResult.sum_list(xi_list)
            yi_sum = RegressionResult.sum_list(yi_list)
            pente = RegressionResult.pente()
            intercept = RegressionResult.intercept(pente)
            ap = pente
            bi = intercept
            value_coef = RegressionResult.corref()
            interptn = ""

            # if(value_coef == 1 and value_coef == -1):
            # interptn = "Liaisons absolues (déterministe)"
            if (-0.7 < value_coef > 0.7):
                # interptn = "Liaison stochastique (probabiliste)"
                interptn = "Les deux variables sont fortement corrélées"
            else:
                # interptn = "Pas de liaison"
                interptn = "Les deux variables sont faiblement corrélées"

            coef_label.config(text="r = {:.3f}".format(value_coef))
            interpretation_label.config(text=f"{interptn}", width=50, )
            covariance = RegressionResult.covariance()

            result_frame4.grid(row=5, column=0, columnspan=3, pady=10, padx=5)
            btn_graphique.grid(row=5, column=3, padx=5)

            print("yi_sum :", yi_sum)
            print("XiSum :", xi_sum)
            print("XiSum :", intercept)

            sum_yi_label.config(text=f"{round(yi_sum, 3)}")
            sum_xi_label.config(text=f"{round(xi_sum, 3)}")
            # cov_label.config(text="Cov(x,y) = *** ",)
            cov_label.config(text="Cov(x,y) = {:.3f}".format(covariance))

    def presentation(screen):
        presentation_frame = tk.LabelFrame(screen)
        tk.Label(presentation_frame, text="Statistique descriptive bivariée").grid(row=1, column=0)
        ptf = tk.LabelFrame(presentation_frame)
        ptf.config(bg="blue")
        ptf.grid(row=3, column=0, padx=(20, 20), pady=(0, 5))
        tk.Label(ptf, text="Régression et Corrélation").grid(row=1, column=0)
        presentation_frame.pack(pady=10)  # grid(row=0,column=0,columnspan=5, pady=(5,5), padx=(15,15))

    ww = tk.Toplevel(parent_screen)
    ww.title("Statistique descriptive bivariée")
    ww.minsize(595, 520)
    ww.geometry("620x640")
    # ww.iconbitmap("image.ico")

    f1 = "Arial", -12
    # f2 = ("Courier New",-24,"bold italic")
    f2 = ("Courier New", -14, "bold")
    f3 = ("Comic Sans MS", -14, "bold underline")
    f4 = ("Helvetica", -12)

    # verticalBar = Scrollbar(ww)

    # verticalBar.grid(row=0,column=0, columnspan=5, rowspan = 5)

    # ================== Main Frame ================

    presentation(ww)

    container = ttk.Frame(ww)
    canvas = tk.Canvas(container, width=570, height=590)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    # for i in range(50):
    # ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    main_frame = tk.Frame(scrollable_frame, )
    main_frame.pack(fill="both")

    calculus_frame = tk.LabelFrame(main_frame)

    canvas_frame = tk.Frame(main_frame)
    canvas_frame.grid(row=0, column=0, columnspan=5, )
    # verticalBar.config(command=canevas.yview)
    # ScrolledWindow(calculFrame)

    # --- --- --- Title --- --- ---

    size_of_observation_label = tk.Label(canvas_frame, text="Entrez le nombre des observations :")
    size_of_observation_label.grid(row=1, column=0, pady=10)

    size_of_observation = tk.Entry(canvas_frame, width=10)
    size_of_observation.focus_set()
    size_of_observation.grid(row=1, column=3)
    btn_start = tk.Button(canvas_frame, fg="blue", font=f2, text="Lancer", command=generate_tab)
    btn_start.config(activebackground="gray")
    btn_start.grid(row=1, column=4, columnspan=2, padx=5)

    def onEnterClick(event):
        global SIZE_OF_VALUE_ENTRY
        if (SIZE_OF_VALUE_ENTRY == 0):
            generate_tab()
            print("OnClicked  <ENTER>.")

    ww.bind('<Return>', onEnterClick)

    observation = tk.LabelFrame(calculus_frame, text="observation")
    xi_frame = tk.LabelFrame(calculus_frame, text="X")
    yi_frame = tk.LabelFrame(calculus_frame, text="Y")
    xi_sqrt = tk.LabelFrame(calculus_frame, text="xi carré")
    xy_frame = tk.LabelFrame(calculus_frame, text="xyFrame")

    # ================== result ================

    result_frame1 = tk.LabelFrame(calculus_frame, text="pente")
    result_frame2 = tk.LabelFrame(calculus_frame, text="intercept")
    result_frame3 = tk.LabelFrame(calculus_frame, text="coef de corrélation")
    result_frame4 = tk.LabelFrame(calculus_frame, text="interpretation")
    result_frame5 = tk.LabelFrame(calculus_frame, text="covariance")
    result_frame6 = tk.LabelFrame(calculus_frame, text="interpretation")
    btn_graphique = tk.Button(calculus_frame, fg="blue", font=f2, text="Graphique", command=RegressionResult.graphique)

    result_frame5.grid(row=4, column=0)
    result_frame2.grid(row=4, column=1)
    result_frame1.grid(row=4, column=2)
    result_frame3.grid(row=4, column=3)

    pente_label = tk.Label(result_frame1, bg="white", text="a = ...", width=10, )
    pente_label.grid(row=1, column=0)
    intercept_label = tk.Label(result_frame2, bg="white", text="b = ...", width=10, )
    intercept_label.grid(row=1, column=0)
    interpretation_label = tk.Label(result_frame4, bg="white", text="...", )
    interpretation_label.grid(row=1, column=0)

    coef_label = tk.Label(result_frame3, bg="white", text="r = ...", width=10, )
    coef_label.grid(row=0, column=1)

    cov_label = tk.Label(result_frame5, bg="white", text="Cov(x,y) = ...", width=20, )
    cov_label.grid(row=0, column=1)

    observation.grid(row=1, column=0)
    xi_frame.grid(row=1, column=1)
    yi_frame.grid(row=1, column=2)
    xi_sqrt.grid(row=1, column=3)
    xy_frame.grid(row=1, column=4)

    btn_evaluate = tk.Button(calculus_frame, fg="blue", font=f2, text="Calculer", command=on_calculate_xy)
    btn_evaluate.config(activebackground="gray")
    btn_evaluate.grid(row=2, column=1, columnspan=3, pady=5)

    # --- observation - Xi - Yi ---#

    i: int
    for i in range(SIZE_OF_VALUE):
        # listOfValueObs[i] = tk.Entry(observation,width=10)
        # listOfValueObs[i].grid(row=i,column=1)

        listOfValueXi[i] = tk.Entry(xi_frame, width=10)
        listOfValueYi[i] = tk.Entry(yi_frame, width=10)

        # xif = tk.LabelFrame(xi_sqrt)
        # xif.grid(row=i,column=0)
        # xyFramef = tk.LabelFrame(xyFrame)
        # xyFramef.grid(row=i,column=0)

        xi_sqrtLabel[i] = tk.Label(xi_sqrt, bg="white", text="-- --", width=10, )

        xyFrameLabel[i] = tk.Label(xy_frame, bg="white", text=" -- --", width=10, )

    # ================== sum ================

    obs_frame = tk.LabelFrame(observation)
    obs_frame.grid(row=SIZE_OF_VALUE + 2, column=0, pady=(5, 5))
    obs_total = tk.Label(obs_frame, bg="white", text="-- --", width=10, )
    obs_total.grid(row=0, column=0)
    sum_xi_frame = tk.LabelFrame(xi_frame)
    sum_xi_frame.grid(row=SIZE_OF_VALUE + 2, column=1, pady=(5, 5))
    sum_yi_frame = tk.LabelFrame(yi_frame)
    sum_yi_frame.grid(row=SIZE_OF_VALUE + 2, column=1, pady=(5, 5))
    sum_xi_label = tk.Label(sum_xi_frame, bg="white", text="-- --", width=10, )
    sum_xi_label.grid(row=0, column=0)
    sum_yi_label = tk.Label(sum_yi_frame, bg="white", text="-- --", width=10, )
    sum_yi_label.grid(row=0, column=0)

    xi_sqrt_result_frame = tk.LabelFrame(xi_sqrt)
    xi_sqrt_result_frame.grid(row=SIZE_OF_VALUE + 2, column=0, pady=(5, 5))
    xy_frame_result_frame = tk.LabelFrame(xy_frame)
    xy_frame_result_frame.grid(row=SIZE_OF_VALUE + 2, column=0, pady=(5, 5))

    xi_sqrt_label_result = tk.Label(xi_sqrt_result_frame, bg="white", text="-- --", width=10, )
    xi_sqrt_label_result.grid(row=0, column=0)
    xy_frame_label_result = tk.Label(xy_frame_result_frame, bg="white", text="-- --", width=10, )
    xy_frame_label_result.grid(row=0, column=0)

    # ================== mainloop ================

    # ww.mainloop()
