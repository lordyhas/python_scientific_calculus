# <<<CODE×FISRT>>>
import tkinter as tk
from tkinter import messagebox, ttk
# import stat_logic
from logic import UnivarContinous as Univar
from logic import UnivarListBuider as ListBuider

# from scipy import stats


global SIZE_OF_VALUE_ENTRY
global populationList

SIZE_OF_VALUE_ENTRY = 0
sizeOfValue = 5

listOfPopulation = [0] * sizeOfValue
listOfLimInf = [0] * sizeOfValue
listOfLimSup = [0] * sizeOfValue
listOfXi = [0] * sizeOfValue
listOfFi = [0] * sizeOfValue
listOfNi = [0] * sizeOfValue
listOfNiXi = [0] * sizeOfValue
listOfNiXi2 = [0] * sizeOfValue
listOfFiXi2 = [0] * sizeOfValue
xyLabel = [0] * sizeOfValue


class MessageUniv:
    @staticmethod
    def toQuit():
        leave = messagebox.askokcancel("Confirmation",
                                       "Voullez-vous vraiment quitter?")
        if leave:
            quit()

    @staticmethod
    def toErrorNoObservationValue():
        messagebox.showerror("Erreur", "Veillez verifier vos valeur avant de regrouper")

    @staticmethod
    def toErrorCalcul():
        messagebox.showerror("Erreur", "Calcul Error")

    @staticmethod
    def toErrorValue(message=None):
        msg = "Une erreur s'est produite"
        if (message != None):
            msg = message
        messagebox.showwarning("Erreur", msg)

    @staticmethod
    def toinfo():
        messagebox.showinfo("Pas d'info", "C'est ne pas fonctionnel pour l'intant")


window_width, window_height = 0, 0


def stat_univar(parentWW):
    global populationList

    ww = tk.Toplevel(parentWW)
    ww.title("Statistique descriptive univariée")
    ww.minsize(890, 540)
    ww.geometry("920x580")
    # ww.iconbitmap("image.ico")

    f1 = "Arial", -12
    # f2 = ("Courier New",-24,"bold italic")
    f2 = ("Courier New", -14, "bold")
    f3 = ("Comic Sans MS", -14, "bold underline")
    f4 = ("Helvetica", -12)

    def getListFromString(string):
        var = "".join(string.split())
        var = var.split(",")
        varList = list(map(float, var))
        return varList

    def onBuildClass():
        global SIZE_OF_VALUE_ENTRY
        global populationList
        #print(sizeOfValueEntry)
        if (True):
            # L = val.ppltn
            # sizeOfValueEntry = int(populationEntry.get())
            populationList = getListFromString(str(populationEntry.get()))
            # populationList = ppltn
            n = len(populationList)
            # buildInfSupList()
            listOfLimInf = Univar.group(populationList)[0]
            listOfLimSup = Univar.group(populationList)[1]
            listOfXi = ListBuider.build_xi_list(listOfLimInf, listOfLimSup)
            listOfNi = ListBuider.build_ni_list(populationList, listOfLimInf, listOfLimSup)

            listOfFi = ListBuider.build_fi_list(n, listOfNi)
            print("listOfNi : ", listOfNi)
            print("listOfFi : ", listOfFi)
            print("listOfXi : ", listOfXi)

            listOfNiXi = ListBuider.buildNiXiList(listOfNi, listOfXi)
            listOfNiXi2 = ListBuider.buildNiXi2List(listOfNi, listOfXi)
            listOfFiXi2 = ListBuider.buildXiFiList(listOfXi, listOfFi)

            listOfXi2 = [0] * (len(listOfXi))
            for i in range(len(listOfXi)):
                listOfXi2[i] = (listOfXi[i] ** 2)

            sizeOfValueEntry = len(listOfLimInf)
            print("size : ", sizeOfValueEntry)
            print("populationList : ", populationList)
            print("listOfNi : ", listOfNi)
            print("listOfFi : ", listOfFi)
            calculFrame.grid(row=1, column=0, columnspan=10, padx=10)
            # btnBuild.config(text="Relancer")
            for i in range(sizeOfValueEntry):
                tk.Label(observation, text=f"{i + 1}", width=7).grid(row=i, column=0)
                tk.Label(niFrame, bg="white", text=f"{listOfNi[i]}", width=10, ).grid(row=i, column=1)
                tk.Label(fiFrame, bg="white", text=f"{listOfFi[i]}", width=10, ).grid(row=i, column=1, padx=5)
                tk.Label(xiFrame, bg="white", text=f"{listOfXi[i]}", width=10, ).grid(row=i, column=1, padx=5)
                tk.Label(nixiFrame, bg="white", text=f"{listOfNiXi[i]}", width=10, ).grid(row=i, column=1, padx=5)
                tk.Label(nixi_sqrtFrame, bg="white", text=f"{listOfNiXi2[i]}", width=10, ).grid(row=i, column=1, padx=5)

                tk.Label(limInfFrame, bg="white", text=f"{listOfLimInf[i]} - {listOfLimSup[i]}", width=15).grid(row=i,
                                                                                                                column=1,
                                                                                                                padx=5)
                # tk.Label(niFrame,bg="white",text= "-- --",width=10).grid(row=i,column=1,padx=5)

                # listOfLimInf[i].grid(row=i,column=1,padx=(0,7))
                # listOfLimSup[i].grid(row=i,column=1,padx=(0,7))
                tk.Label(xi_sqrtFrame, bg="white", text=f"{round(listOfXi2[i], 3)}", width=10, ).grid(row=i, column=0,
                                                                                                      padx=5)
                tk.Label(fiXiFrame, bg="white", text=f"{listOfFiXi2[i]}", width=10, ).grid(row=i, column=0, padx=5)
                # xi_sqrtLabel[i]
                # xyLabel[i]
            obsTotal.config(text=f" n = {sizeOfValueEntry} ")
            sumXiLabel.config(text=f" {round(sum(listOfXi), 3)}")
            xi_sqrtLabelResult.config(text=f" {round(sum(listOfXi2), 3)}")
            sumFiLabel.config(text=f" {round(sum(listOfFi), 3)}")
            sumNiLabel.config(text=f" {len(populationList)}")
            sumNiXiLabel.config(text=f" {round(sum(listOfNiXi), 3)}")
            sumNiXi2Label.config(text=f" {round(sum(listOfNiXi2), 3)}")

            fixiLabel.config(text=f" {round(sum(listOfFiXi2), 3)}")
            btnCalc["state"] = "normal"

        try:
            pass
        except Exception as e:
            print("Error (univar 1)  : ", e)
            MessageUniv.toErrorNoObservationValue()

        # RegressionResult.graphique()

    def onCalculate():
        global populationList
        # populationList = ppltn
        n = len(populationList)
        listOfLimInf = Univar.group(populationList)[0]
        listOfLimSup = Univar.group(populationList)[1]
        listOfXi = ListBuider.build_xi_list(listOfLimInf, listOfLimSup)
        listOfNi = ListBuider.build_ni_list(populationList, listOfLimInf, listOfLimSup)
        listOfFi = ListBuider.build_fi_list(n, listOfNi)
        listOfNiXi = ListBuider.buildNiXiList(listOfNi, listOfXi)
        listOfNiXi2 = ListBuider.buildNiXi2List(listOfNi, listOfXi)
        listOfFiXi2 = ListBuider.buildXiFiList(listOfXi, listOfFi)

        niMode = ListBuider.ni_modal(listOfNi)
        print("modal : ", niMode)
        mid = int(n / 2)
        index = 0
        po = sorted(populationList)
        for i in range(len(listOfLimInf)):
            if (po[mid] >= listOfLimInf[i] and po[mid] < listOfLimSup[i]):
                index = i
                break
        print("median class : ", po[mid], " - mid = ", mid, " - i = ", index)
        if (True):
            amp = Univar.interval(populationList)
            mean = Univar.mean(n, listOfNiXi)
            median = Univar.median(n, amp, index, listOfLimInf, listOfNi)
            mode = Univar.mode(amp, listOfLimInf, listOfNi, niMode[1])
            # wmode = stats.mode(populationList)
            # print("### ### mode : ",wmode)

            variance = Univar.variance(sum(listOfFiXi2), mean)
            print("variance : ", variance)
            ecartType = Univar.ecartType(variance)
            coefVar = Univar.coefVar(ecartType, mean)

            modeString = ""
            if (len(mode) > 1):
                for i in range(len(mode)):
                    modeString += f"mod{i + 1} = {round(mode[i])} , "
            else:
                modeString = f"mod = {round(mode[0], 3)}"

            moyLabel.config(text=f"Moy = {mean}")
            modLabel.config(text=f"{modeString}", width=25)
            medLabel.config(text=f"Med = {median}")
            varianceLabel.config(text=f"V(x) = {variance}")
            ecartypeLabel.config(text=f"S = {ecartType}")
            cvLabel.config(text=f"cv = {coefVar}%")
            mainResult.grid(row=2, column=0, columnspan=10, padx=10, pady=16.0)

        try:
            pass
        except Exception as e:
            print("Error (univar 2) : ", e)
            MessageUniv.toErrorCalcul()

    def titleScreen(screen):
        presentationFrame = tk.LabelFrame(screen)
        presentationFrame.pack(pady=(10, 5))  # grid(row=0,column=0,columnspan=5, pady=(5,5), padx=(15,15))
        tk.Label(presentationFrame, text="Statistique descriptive univariée").grid(row=1, column=0)
        ptf = tk.LabelFrame(presentationFrame)
        ptf.config(bg="blue")
        ptf.grid(row=3, column=0, padx=(10, 10), pady=(0, 5))
        tk.Label(ptf, text="Série statistique & regroupement en classe").grid(row=1, column=0)

    # verticalBar = Scrollbar(ww)

    # verticalBar.grid(row=0,column=0, columnspan=5, rowspan = 5)

    # ================== Main Frame ================

    titleScreen(ww)

    container = ttk.Frame(ww)
    canvas = tk.Canvas(container, width=860, height=520)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    canvas.update_idletasks()

    # ww.bind("<Configure>", resize)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((window_width, window_height), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    # for i in range(50):
    # ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    mainFrame = tk.Frame(scrollable_frame, )
    mainFrame.pack(fill="both")

    calculFrame = tk.LabelFrame(mainFrame)
    mainResult = tk.Frame(mainFrame, )

    canevas = tk.Frame(mainFrame)
    canevas.grid(row=0, column=0, columnspan=5, )
    # verticalBar.config(command=canevas.yview)
    # ScrolledWindow(calculFrame)

    # --- --- --- Title --- --- ---

    populationLabel = tk.Label(canevas, text="population : ")
    populationLabel.grid(row=1, column=0, pady=10)

    populationEntry = tk.Entry(canevas, width=120)
    populationEntry.focus_set()
    populationEntry.grid(row=1, column=1, columnspan=8)
    btnCalc = tk.Button(canevas, fg="blue", font=f2, text="Calculer", command=onCalculate)
    btnCalc["state"] = "disabled"
    btnBuild = tk.Button(canevas, fg="blue", font=f2, text="Regrouper", command=onBuildClass)
    btnCalc.config(activebackground="gray")
    btnCalc.grid(row=2, column=2, pady=5)
    btnBuild.grid(row=2, column=1, pady=5, padx=5)

    def onEnterClick(event):
        global SIZE_OF_VALUE_ENTRY
        if (sizeOfValueEntry == 0):
            onBuildClass()
            print("onEnterClick.")

    ww.bind('<Return>', onEnterClick)

    observation = tk.LabelFrame(calculFrame, text=" numero ")
    limInfFrame = tk.LabelFrame(calculFrame, text=" Linf-Lsup ")
    niFrame = tk.LabelFrame(calculFrame, text=" ni ")
    fiFrame = tk.LabelFrame(calculFrame, text=" fi")
    xiFrame = tk.LabelFrame(calculFrame, text=" Xi ")
    nixiFrame = tk.LabelFrame(calculFrame, text=" ni × Xi ")
    xi_sqrtFrame = tk.LabelFrame(calculFrame, text=" Xi^2 ")
    nixi_sqrtFrame = tk.LabelFrame(calculFrame, text=" Ni × Xi^2 ")
    fiXiFrame = tk.LabelFrame(calculFrame, text=" fi × Xi^2 ")

    # ================== result ================

    moyFrame = tk.LabelFrame(mainResult, text="Moyenne")
    medFrame = tk.LabelFrame(mainResult, text="Mediane")
    modFrame = tk.LabelFrame(mainResult, text="Mode")

    varianceFrame = tk.LabelFrame(mainResult, text="variance")
    ecartypeFrame = tk.LabelFrame(mainResult, text="ecart-type")
    cvFrame = tk.LabelFrame(mainResult, text="c.v")

    moyFrame.grid(row=4, column=1)
    medFrame.grid(row=4, column=2)
    modFrame.grid(row=4, column=3)

    varianceFrame.grid(row=5, column=1)
    ecartypeFrame.grid(row=5, column=2)
    cvFrame.grid(row=5, column=3)

    moyLabel = tk.Label(moyFrame, bg="white", text="moy = ...", width=15, )
    moyLabel.grid(row=1, column=0)
    medLabel = tk.Label(medFrame, bg="white", text="med = ...", width=15, )
    medLabel.grid(row=1, column=0)
    modLabel = tk.Label(modFrame, bg="white", text="mod = ...", width=15, )
    modLabel.grid(row=0, column=1, columnspan=5)

    varianceLabel = tk.Label(varianceFrame, bg="white", text="...", width=15, )
    varianceLabel.grid(row=1, column=0, )
    ecartypeLabel = tk.Label(ecartypeFrame, bg="white", text="...", width=15, )
    ecartypeLabel.grid(row=1, column=0, )
    cvLabel = tk.Label(cvFrame, bg="white", text="...", width=15, )
    cvLabel.grid(row=1, column=0, )

    observation.grid(row=1, column=0)
    limInfFrame.grid(row=1, column=1)
    niFrame.grid(row=1, column=2)
    fiFrame.grid(row=1, column=3)
    xiFrame.grid(row=1, column=4)
    nixiFrame.grid(row=1, column=5)
    xi_sqrtFrame.grid(row=1, column=6)
    nixi_sqrtFrame.grid(row=1, column=7)
    fiXiFrame.grid(row=1, column=8)

    # btnEvaluate = tk.Button(mainResult,fg="blue",font=f2,text="Calculer",)
    # btnEvaluate.config(activebackground="gray")
    # btnEvaluate.grid(row=2,column=1,columnspan=3,pady=5)

    # --- observation - Xi - Yi ---#

    # for i in range(sizeOfValue):
    # listOfValueObs[i] = tk.Entry(observation,width=10)
    # listOfValueObs[i].grid(row=i,column=1)

    # listOfLimInf[i] = 0
    # listOfLimSup[i] = 0

    # xif = tk.LabelFrame(Frame)
    # xif.grid(row=i,column=0)
    # xyf = tk.LabelFrame(fiXiFrame)
    # xyf.grid(row=i,column=0)

    # xi_sqrtLabel[i] = tk.Label(xi_sqrtFrame,bg="white",text="-- --",width=10,)

    # xyLabel[i] =

    # ================== sum ================

    obsFrame = tk.LabelFrame(observation)
    obsFrame.grid(row=sizeOfValue + 2, column=0, padx=5, pady=5)
    obsTotal = tk.Label(obsFrame, bg="white", text="-- --", width=3, )
    obsTotal.grid(row=0, column=0)
    sumLimClassFrame = tk.LabelFrame(limInfFrame)
    sumLimClassFrame.grid(row=sizeOfValue + 2, column=1, pady=(5, 5))

    sumNiFrame = tk.LabelFrame(niFrame)
    sumNiFrame.grid(row=sizeOfValue + 2, column=1, pady=(5, 5))

    sumFiFrame = tk.LabelFrame(fiFrame)
    sumFiFrame.grid(row=sizeOfValue + 2, column=1, pady=(5, 5))

    sumXiFrame = tk.LabelFrame(xiFrame)
    sumXiFrame.grid(row=sizeOfValue + 2, column=1, pady=(5, 5))

    sumNiXiFrame = tk.LabelFrame(nixiFrame)
    sumNiXiFrame.grid(row=sizeOfValue + 2, column=1, pady=(5, 5))

    sumNiXiSqrtFrame = tk.LabelFrame(nixi_sqrtFrame)
    sumNiXiSqrtFrame.grid(row=sizeOfValue + 2, column=1, pady=(5, 5))

    numberOfClass = tk.Label(sumLimClassFrame, bg="white", text="-- --", width=10, )
    numberOfClass.grid(row=0, column=0)
    sumNiLabel = tk.Label(sumNiFrame, bg="white", text="-- --", width=10, )
    sumNiLabel.grid(row=0, column=0)
    sumFiLabel = tk.Label(sumFiFrame, bg="white", text="-- --", width=10, )
    sumFiLabel.grid(row=0, column=0)
    sumXiLabel = tk.Label(sumXiFrame, bg="white", text="-- --", width=10, )
    sumXiLabel.grid(row=0, column=0)
    sumNiXiLabel = tk.Label(sumNiXiFrame, bg="white", text="-- --", width=10, )
    sumNiXiLabel.grid(row=0, column=0)
    sumNiXi2Label = tk.Label(sumNiXiSqrtFrame, bg="white", text="-- --", width=10, )
    sumNiXi2Label.grid(row=0, column=0)

    xi_sqrtResultFrame = tk.LabelFrame(xi_sqrtFrame)
    xi_sqrtResultFrame.grid(row=sizeOfValue + 2, column=0, pady=(5, 5))
    # nixi_sqrtResultFrame = tk.LabelFrame(xi_sqrtFrame)
    # nixi_sqrtResultFrame.grid(row=sizeOfValue+2, column = 0, pady=(5,5))
    fixiResultFrame = tk.LabelFrame(fiXiFrame)
    fixiResultFrame.grid(row=sizeOfValue + 2, column=0, pady=(5, 5))

    xi_sqrtLabelResult = tk.Label(xi_sqrtResultFrame, bg="white", text="-- --", width=10, )
    xi_sqrtLabelResult.grid(row=0, column=0)
    fixiLabel = tk.Label(fixiResultFrame, bg="white", text="-- --", width=10, )
    fixiLabel.grid(row=0, column=0)

    # ================== mainloop ================

    # ww.mainloop()

    '''def getValueList(L):
        T = []
        print("####### ",sizeOfValueEntry)
            
        try:
            for i in range(sizeOfValueEntry):
                T.append(float(L[i].get()))     
            print("List : ",T)
            return T
        except Exception as e:
            print(f"Error {e}")
            MessageUniv.toErrorValue(message="Veuillez reverifier vos valeur (Xi, Yi)")    
        return []'''
