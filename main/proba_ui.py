from tkinter import *
from tkinter import ttk

from logic import BinomialDistribution as Binomiale
from logic import GeometricDistribution as Geometrique
from logic import HyperGeometricDistribution as HyperGeometrique
from logic import PoissonDistribution as Poisson


def main_proba(ww):  # grid(rpassow=0,column=0,columnspan=5, pady=(5,5), padx=(15,15))
    root = Toplevel(ww)
    root.title("PROBABILITE")
    root.geometry("720x720")
    root.minsize(720, 480)
    # root.iconbitmap("image.ico")

    container = ttk.Frame(root)
    canvas = Canvas(container, width=700, height=720)
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

    #######################################################################
    # NoteFrame
    note_frame = LabelFrame(scrollable_frame, text="Note")
    note_frame.grid(row=0, column=0, padx=20, pady=20, sticky=W)

    Label(note_frame,
          text="1. Decochez la case 'probabilite' pour calculer seulement la variance et l'esperance mathematique",
          fg='blue').grid(row=0, column=0, padx=5, pady=5, sticky=W)

    #############################################################################################################
    # Binomiale
    binomial_frame = LabelFrame(scrollable_frame, text="Distribution Binomiale", font='Helvetica 10 bold', borderwidth=1)
    binomial_frame.grid(row=1, column=0, padx=20, pady=5, sticky=W)

    bk = IntVar()
    bn = IntVar()
    bp = DoubleVar()

    cbBProb = IntVar(value=1)

    Label(binomial_frame, text="n: ").grid(row=0, column=0, padx=5, pady=5)
    entry_bn = Entry(binomial_frame, textvariable=bn, width=5)
    entry_bn.grid(row=0, column=1, padx=5, pady=5)

    Label(binomial_frame, text="p: ").grid(row=0, column=2, padx=5, pady=5)
    entry_bp = Entry(binomial_frame, textvariable=bp, width=5)
    entry_bp.grid(row=0, column=3, padx=5, pady=5)

    label_bk = Label(binomial_frame, text="k: ")
    label_bk.grid(row=0, column=4, padx=5, pady=5)
    entry_bk = Entry(binomial_frame, textvariable=bk, width=5)
    entry_bk.grid(row=0, column=5, padx=5, pady=5)

    def visibility_binomial():
        if cbBProb.get() == 0:
            entry_bk.grid_remove()
            label_bk.grid_remove()
        else:
            entry_bk.grid()
            label_bk.grid()

    choice_label_binomial = LabelFrame(binomial_frame, text='Choix resultat')
    choice_label_binomial.grid(row=1, column=0, padx=5, pady=5, columnspan=5, sticky=W)

    check_button_b_prob = Checkbutton(choice_label_binomial, text='Probabilite', variable=cbBProb, onvalue=1, offvalue=0,
                                   command=visibility_binomial)
    check_button_b_prob.grid(row=0, column=0, padx=5, pady=5)

    result_binom_frame = LabelFrame(choice_label_binomial, text="Resultat")

    result_variable_b_prob = StringVar()
    result_variable_b_var = StringVar()
    result_variable_b_esp = StringVar()

    label_b_prob = Label(result_binom_frame)
    result_label_b_prob = Label(result_binom_frame, textvariable=result_variable_b_prob, font='Helvetica 12 bold')
    result_label_b_var = Label(result_binom_frame, textvariable=result_variable_b_var, font='Helvetica 12 bold')
    result_label_b_esp = Label(result_binom_frame, textvariable=result_variable_b_esp, font='Helvetica 12 bold')

    def effectuer_binom():

        result_variable_b_var.set(value=Binomiale.variance(bn.get(), bp.get()))
        result_variable_b_esp.set(value=Binomiale.esperence(bn.get(), bp.get()))

        result_binom_frame.grid(row=2, column=0, padx=5, pady=5, columnspan=5, sticky=W)
        if cbBProb.get() == 1:
            label_b_prob.config(text=f"P(X= {bk.get()}): ")
            result_variable_b_prob.set(value=Binomiale.binomiale(bk.get(), bn.get(), bp.get()))
            label_b_prob.grid(row=0, column=0, padx=5, pady=5)
            result_label_b_prob.grid(row=0, column=1, padx=5, pady=5)
        else:
            label_b_prob.grid_remove()
            result_label_b_prob.grid_remove()

        Label(result_binom_frame, text="Variance: ").grid(row=1, column=0, padx=5, pady=5)
        result_label_b_var.grid(row=1, column=1, padx=5, pady=5)
        Label(result_binom_frame, text="Esperence Mathematique: ").grid(row=2, column=0, padx=5, pady=5)
        result_label_b_esp.grid(row=2, column=1, padx=5, pady=5)

    def effacer_binomiale():
        entry_bk.delete(0, 'end')
        entry_bn.delete(0, 'end')
        entry_bp.delete(0, 'end')
        result_binom_frame.grid_forget()

    Button(binomial_frame, text='Effectuer', fg='blue', command=effectuer_binom).grid(row=0, column=6, padx=5, pady=5)
    Button(binomial_frame, text='Effacer', fg='red', command=effacer_binomiale).grid(row=0, column=7, padx=5, pady=5)

    Label(binomial_frame, text="k: Nombre de succes, n: Nombre d'epreuve, p: Probabilite", fg='blue').grid(row=2,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5,
                                                                                                          columnspan=6,
                                                                                                          sticky=W)

    #############################################################################################################
    # Poisson
    poissonFrame = LabelFrame(scrollable_frame, text="Distribution de Poisson", font='Helvetica 10 bold', borderwidth=1)
    poissonFrame.grid(row=2, column=0, padx=20, pady=5, sticky=W)

    pl = DoubleVar()
    pk = IntVar()

    Label(poissonFrame, text="l: ").grid(row=0, column=0, padx=5, pady=5)
    entry_pl = Entry(poissonFrame, textvariable=pl, width=5)
    entry_pl.grid(row=0, column=1, padx=5, pady=5)

    Label(poissonFrame, text="k: ").grid(row=0, column=2, padx=5, pady=5)
    entry_pk = Entry(poissonFrame, textvariable=pk, width=5)
    entry_pk.grid(row=0, column=3, padx=5, pady=5)

    result_poisson_frame = LabelFrame(poissonFrame, text="Resultat")

    result_variable_p_prob = StringVar()
    result_variable_p_var = StringVar()
    result_variable_p_esp = StringVar()

    result_label_p_prob = Label(result_poisson_frame, textvariable=result_variable_p_prob, font='Helvetica 12 bold')
    result_label_p_var = Label(result_poisson_frame, textvariable=result_variable_p_var, font='Helvetica 12 bold')
    result_label_p_esp = Label(result_poisson_frame, textvariable=result_variable_p_esp, font='Helvetica 12 bold')

    def effectuer_poisson():
        result_variable_p_prob.set(value=Poisson.poisson(pl.get(), pk.get()))
        result_variable_p_var.set(value=Poisson.variance(pl.get()))
        result_variable_p_esp.set(value=Poisson.esperence(pl.get()))

        result_poisson_frame.grid(row=1, column=0, padx=5, pady=5, columnspan=5, sticky=W)
        Label(result_poisson_frame, text=f"P(X= {pk.get()}): ").grid(row=0, column=0, padx=5, pady=5)
        result_label_p_prob.grid(row=0, column=1, padx=5, pady=5)
        Label(result_poisson_frame, text="Variance: ").grid(row=1, column=0, padx=5, pady=5)
        result_label_p_var.grid(row=1, column=1, padx=5, pady=5)
        Label(result_poisson_frame, text="Esperence Mathematique: ").grid(row=2, column=0, padx=5, pady=5)
        result_label_p_esp.grid(row=2, column=1, padx=5, pady=5)

    def effacer_poisson():
        entry_pk.delete(0, 'end')
        entry_pl.delete(0, 'end')
        result_poisson_frame.grid_forget()

    Button(poissonFrame, text='Effectuer', fg='blue', command=effectuer_poisson).grid(row=0, column=4, padx=5, pady=5)
    Button(poissonFrame, text='Effacer', fg='red', command=effacer_poisson).grid(row=0, column=5, padx=5, pady=5)

    Label(poissonFrame, text="k: Nombre de succes, l : nombre moyen", fg='blue').grid(row=2, column=0, padx=5, pady=5,
                                                                                      columnspan=6, sticky=W)
    #############################################################################################################
    # Geometric
    geoFrame = LabelFrame(scrollable_frame, text="Distribution geometrique", font='Helvetica 10 bold', borderwidth=1)
    geoFrame.grid(row=3, column=0, padx=20, pady=5, sticky=W)

    gk = IntVar()
    gp = DoubleVar()

    Label(geoFrame, text="p: ").grid(row=0, column=0, padx=5, pady=5)
    entry_gp = Entry(geoFrame, textvariable=gp, width=5)
    entry_gp.grid(row=0, column=1, padx=5, pady=5)

    Label(geoFrame, text="k: ").grid(row=0, column=2, padx=5, pady=5)
    entry_gk = Entry(geoFrame, textvariable=gk, width=5)
    entry_gk.grid(row=0, column=3, padx=5, pady=5)

    choix_label_geo = LabelFrame(geoFrame, text='Choix resultat')
    choix_label_geo.grid(row=1, column=0, padx=5, pady=5, columnspan=5, sticky=W)

    result_geo_frame = LabelFrame(geoFrame, text="Resultat")

    result_variable_g_prob = StringVar()
    result_variable_g_var = StringVar()
    result_variable_g_esp = StringVar()

    result_label_g_prob = Label(result_geo_frame, textvariable=result_variable_g_prob, font='Helvetica 12 bold')
    result_label_g_var = Label(result_geo_frame, textvariable=result_variable_g_var, font='Helvetica 12 bold')
    result_label_g_esp = Label(result_geo_frame, textvariable=result_variable_g_esp, font='Helvetica 12 bold')

    def effectuerGeo():
        result_variable_g_prob.set(value=Geometrique.geometrique(gk.get(), gp.get()))
        result_variable_g_var.set(value=Geometrique.variance(gp.get()))
        result_variable_g_esp.set(value=Geometrique.esperence(gp.get()))

        result_geo_frame.grid(row=1, column=0, padx=5, pady=5, columnspan=5, sticky=W)
        Label(result_geo_frame, text=f"P(X= ):{gk.get()}").grid(row=0, column=0, padx=5, pady=5)
        result_label_g_prob.grid(row=0, column=1, padx=5, pady=5)
        Label(result_geo_frame, text="Variance: ").grid(row=1, column=0, padx=5, pady=5)
        result_label_g_var.grid(row=1, column=1, padx=5, pady=5)
        Label(result_geo_frame, text="Esperence Mathematique: ").grid(row=2, column=0, padx=5, pady=5)
        result_label_g_esp.grid(row=2, column=1, padx=5, pady=5)

    def effacerGeo():
        entry_gk.delete(0, 'end')
        entry_gp.delete(0, 'end')
        result_geo_frame.grid_forget()

    Button(geoFrame, text='Effectuer', fg='blue', command=effectuerGeo).grid(row=0, column=4, padx=5, pady=5)
    Button(geoFrame, text='Effacer', fg='red', command=effacerGeo).grid(row=0, column=5, padx=5, pady=5)

    Label(geoFrame, text="k: Nombre de succes, p: Probabilite", fg='blue').grid(row=2, column=0, padx=5, pady=5,
                                                                                columnspan=6, sticky=W)

    #############################################################################################################
    # HyperGeometric
    hypergeo_frame = LabelFrame(scrollable_frame, text="Distribution hypergeometrique", font='Helvetica 10 bold',
                               borderwidth=1)
    hypergeo_frame.grid(row=4, column=0, padx=20, pady=5, sticky=W)

    hk = IntVar()
    hm = IntVar()
    h_n = IntVar()
    h_n = IntVar()

    cb_h_prob = IntVar(value=1)

    Label(hypergeo_frame, text="M: ").grid(row=0, column=0, padx=5, pady=5)
    entry_hm = Entry(hypergeo_frame, textvariable=hm, width=5)
    entry_hm.grid(row=0, column=1, padx=5, pady=5)

    Label(hypergeo_frame, text="n: ").grid(row=0, column=2, padx=5, pady=5)
    entry_hn = Entry(hypergeo_frame, textvariable=h_n, width=5)
    entry_hn.grid(row=0, column=3, padx=5, pady=5)

    Label(hypergeo_frame, text="N: ").grid(row=0, column=4, padx=5, pady=5)
    entry_hn = Entry(hypergeo_frame, textvariable=h_n, width=5)
    entry_hn.grid(row=0, column=5, padx=5, pady=5)

    label_hk = Label(hypergeo_frame, text="k: ")
    label_hk.grid(row=0, column=6, padx=5, pady=5)
    entry_hk = Entry(hypergeo_frame, textvariable=hk, width=5)
    entry_hk.grid(row=0, column=7, padx=5, pady=5)

    choix_label_hyper = LabelFrame(hypergeo_frame, text='Choix resultat')
    choix_label_hyper.grid(row=1, column=0, padx=5, pady=5, columnspan=5, sticky=W)

    def visibilityHyper():
        if cb_h_prob.get() == 0:
            entry_hk.grid_remove()
            label_hk.grid_remove()
        else:
            entry_hk.grid()
            label_hk.grid()

    check_button_h_prob = Checkbutton(choix_label_hyper, text='Probabilite', variable=cb_h_prob, onvalue=1, offvalue=0,
                                   command=visibilityHyper)
    check_button_h_prob.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    result_hypergeo_frame = LabelFrame(choix_label_hyper, text="Resultat")

    result_variable_h_prob = StringVar()
    result_variable_h_var = StringVar()
    result_variable_h_esp = StringVar()

    label_h_prob = Label(result_hypergeo_frame)
    result_label_h_prob = Label(result_hypergeo_frame, textvariable=result_variable_h_prob, font='Helvetica 12 bold')
    result_label_h_var = Label(result_hypergeo_frame, textvariable=result_variable_h_var, font='Helvetica 12 bold')
    result_label_h_esp = Label(result_hypergeo_frame, textvariable=result_variable_h_esp, font='Helvetica 12 bold')

    def effectuer_hyper_geo():
        result_variable_h_var.set(value=HyperGeometrique.variance(hm.get(), h_n.get(), h_n.get()))
        result_variable_h_esp.set(value=HyperGeometrique.esperence(hm.get(), h_n.get(), h_n.get()))

        result_hypergeo_frame.grid(row=1, column=0, padx=5, pady=5, columnspan=5, sticky=W)
        if cb_h_prob.get() == 1:
            label_h_prob.config( text=f"P(X= {hk.get()}): ")
            result_variable_h_prob.set(
                value=HyperGeometrique.hyper_geometric(hk.get(), hm.get(), h_n.get(), h_n.get()))
            label_h_prob.grid(row=1, column=0, padx=5, pady=5)
            result_label_h_prob.grid(row=1, column=1, padx=5, pady=5)
        else:
            label_h_prob.grid_remove()
            result_label_h_prob.grid_remove()

        Label(result_hypergeo_frame, text="Variance: ").grid(row=2, column=0, padx=5, pady=5)
        result_label_h_var.grid(row=2, column=1, padx=5, pady=5)
        Label(result_hypergeo_frame, text="Esperence Mathematique: ").grid(row=3, column=0, padx=5, pady=5)
        result_label_h_esp.grid(row=3, column=1, padx=5, pady=5)

    def effacer_hypergeo():
        entry_hn.delete(0, 'end')
        entry_hn.delete(0, 'end')
        entry_hk.delete(0, 'end')
        entry_hm.delete(0, 'end')
        result_hypergeo_frame.grid_forget()

    Button(hypergeo_frame, text='Effectuer', fg='blue', command=effectuer_hyper_geo).grid(row=0, column=8, padx=5, pady=5)
    Button(hypergeo_frame, text='Effacer', fg='red', command=effacer_hypergeo).grid(row=0, column=9, padx=5, pady=5)

    Label(hypergeo_frame,
          text="k: nombre de succes, n: Effectif d'échantillon, M: Effectif de la population ,N: Nombre d'événements de la population'",
          fg='blue').grid(row=2, column=0,
                          padx=5, pady=5,
                          columnspan=10, sticky=W)
    #######################################################################################################################
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # ww.mainloop()
