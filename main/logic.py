from tkinter import Scrollbar, messagebox, ttk
import math
from math import sqrt

import matplotlib
from matplotlib import pyplot as plt
from scipy import stats


class UnivarContinous:
    """ UnivarContinous : ---  """

    @classmethod
    def _most_frequent(cls, array):
        counter = 0
        num = array[0]

        for i in array:
            curr_frequency = array.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = i

        return num

    @classmethod
    def interval(cls, L):
        return round((max(L) - min(L)) / int(cls.len_group(len(L))), 4)

    @classmethod
    def len_group(cls, n):
        return int(1 + 3.3 * (math.log(n, 10)))

    @classmethod
    def group(cls, L):
        inf_list = []
        sup_list = []
        interval = cls.interval(L)
        len_g = cls.len_group(len(L))
        min_val = min(L)
        max_val = min_val + interval
        for i in range(len_g):
            inf_list += [round(min_val, 3)]
            sup_list += [round(max_val, 3)]
            min_val += interval
            max_val += interval

        return (inf_list, sup_list)

    @staticmethod
    def mean(population, nixi):

        n = population
        v = sum(nixi)
        # print("sum : ", v)
        return round(v / n, 3)

    @classmethod
    def median(cls, n, a, index, Linf, Lni):
        q = 0
        freq = []
        for i in Lni:
            q += i
            freq += [q]
        med = Linf[index] + a * (((n / 2) - freq[index - 1]) / Lni[index])
        return round(med, 4)

    @classmethod
    def mode(cls, a, list_inf, list_ni, list_mod):
        mod = []
        delta1 = 0
        delta2 = 0

        length = len(list_mod)
        for i in list_mod:
            print("mode-pos = ", i)
            if i == 0:
                mod += [list_inf[i] + a * ((list_ni[i] - 0) / ((list_ni[i] - 0) + (list_ni[i] - list_ni[i + 1])))]
            elif i >= length - 1:
                mod += [list_inf[i] + a * ((list_ni[i] - list_ni[i - 1]) / ((list_ni[i] - list_ni[i - 1]) + (list_ni[i] - 0)))]
            else:
                mod += [list_inf[i] + a * ((list_ni[i] - list_ni[i - 1]) / ((list_ni[i] - list_ni[i - 1]) + (list_ni[i] - list_ni[i + 1])))]

        return mod

    @classmethod
    def variance(cls, somFiXi2, mu):
        return round((somFiXi2 - (mu ** 2)), 4)

    @classmethod
    def ecartType(cls, var):
        return round(sqrt(var), 4)

    @classmethod
    def coefVar(cls, ecr, mu):
        return round((ecr / mu) * 100, 4)

    @classmethod
    def display(cls, L):
        print("k : ", cls.len_group(len(L)))
        print("interval : ", cls.interval(L))
        print("Linf : ", cls.group(L)[0])
        print("Lsup : ", cls.group(L)[1])


class UnivarListBuider:
    @staticmethod
    def build_xi_list(L1, L2):
        assert (len(L1) == len(L2))
        L = []
        for i in range(len(L1)):
            L += [round((L1[i] + L2[i]) / 2, 3)]
        # L[5] = (L1[5]+L2[5])/2
        # L[5] = 2
        # print("L : ",L)
        return L

    @staticmethod
    def build_ni_list(Lpop, Linf, Lsup):
        Lpop = sorted(Lpop)
        print("\nPop : ", Lpop)
        L = []
        count = 0
        for e in range(len(Linf)):
            # print(e, "inf - sup : ",Linf[e]," - ",Lsup[e])
            for i in range(len(Lpop)):
                if (Lpop[i] >= Linf[e] and Lpop[i] <= Lsup[e]):
                    count += 1
            L += [count]
            count = 0
        # print("Ni : ",L)
        return L

    @staticmethod
    def build_fi_list(n, listNi):
        n = n
        L = []
        for i in range(len(listNi)):
            L += [round(listNi[i] / n, 3)]
        return L

    @staticmethod
    def buildNiXiList(listNi, listXi):
        L = []
        for i in range(len(listNi)):
            L += [round(listNi[i] * listXi[i], 3)]
        return L

    @staticmethod
    def buildNiXi2List(listNi, listXi):
        L = []
        for i in range(len(listNi)):
            L += [round(listNi[i] * (listXi[i] ** 2), 3)]
        return L

    @staticmethod
    def buildXiFiList(listXi, listFi):
        assert (len(listXi) == len(listFi))
        L = []
        for i in range(len(listXi)):
            L += [round((listXi[i] ** 2) * listFi[i], 3)]
        return L

    @staticmethod
    def ni_modal(niList):
        m = max(niList)
        count = 0
        L = []
        for i in range(len(niList)):
            if (niList[i] == m):
                L += [i]

        return (m, L)


class BinomialDistribution:
    @staticmethod
    def binomiale(k, n, p):
        return format(stats.binom.pmf(k, n, p), ".2f")

    @staticmethod
    def variance(n, p):
        return format(stats.binom.var(n, p), ".2f")

    @staticmethod
    def esperence(n, p):
        return format(stats.binom.mean(n, p), ".2f")


class GeometricDistribution:


    @staticmethod
    def geometrique(k, p):
        return format(stats.geom.pmf(k, p), ".2f")

    @staticmethod
    def variance(p):
        return format(stats.geom.var(p), ".2f")

    @staticmethod
    def esperence(p):
        return format(stats.geom.mean(p), ".2f")


class HyperGeometricDistribution:
    @staticmethod
    def hyper_geometric(k, M, n, N):
        return format(stats.hypergeom.pmf(k, M, n, N), ".2f")

    @staticmethod
    def variance(M, n, N):
        return format(stats.hypergeom.var(M, n, N), ".2f")

    @staticmethod
    def esperence(M, n, N):
        return format(stats.hypergeom.mean(M, n, N), ".2f")


class PoissonDistribution:
    @staticmethod
    def poisson(l, k):
        return format(stats.poisson.pmf(k, mu=l), ".2f")

    @staticmethod
    def variance(l):
        return format(stats.poisson.var(mu=l), ".2f")

    @staticmethod
    def esperence(l):
        return format(stats.poisson.var(mu=l), ".2f")


'''----------------------------------------------------'''

ppltn_test = [
    15,
    16,
    33,
    25,
    22,
    33,
    15,
    25,
    20,
    40,
    24,
    24,
    35,
    20,
    32,
    23,
    43,
    32,
    26,
    40,
    23,
    17,
    27,
    42,
    31,
    25,
    27,
    31,
    25,
    24,
    19,
    21,
    23,
    34,
    23,
    30,
    21,
    24,
    24,
    28,
    30,
    29,
    19,
    32,
    36,
    35,
    27,
    29,
    17,
    17,
    30,
    42,
    42,
    30,
    42,
    25,
    37,
    25,
    44,
    40,
    29,
    43,
    22,
    34,
    47,
    34,
    18,
    17,
    45,
    30]
