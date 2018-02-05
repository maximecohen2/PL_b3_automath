#!/usr/bin/python3
# coding: utf-8

from copy import deepcopy


class MathIter:

    def __init__(self):
        self.base = []
        self.index = []
        self.delta = []
        self.beta = []
        self.betaIndex = []
        self.z = 0
        self.table = []
        self.input = None
        self.output = None

    def compute_beta_index(self):
        self.input = self.delta.index(max(self.delta))
        for i, beta in enumerate(self.beta):
            if self.table[i][self.input] != 0:
                self.betaIndex.append(str(round(beta / self.table[i][self.input], 1)))
            else:
                self.betaIndex.append("inf.")
        temp_tab = [float(x) for x in self.betaIndex if x != "inf." and float(x) > 0]
        self.output = self.betaIndex.index(str(min(temp_tab)))

    def set_first_iter(self, data):
        self.base = deepcopy(data['base'])
        self.index = deepcopy(data['index'])
        self.table = deepcopy(data['table'])
        self.beta = deepcopy(data['beta'])
        self.delta = deepcopy(data['delta'])
        self.compute_beta_index()


    def compute_table(self, prev_iter):
        s = prev_iter.output
        e = prev_iter.input
        ptable = prev_iter.table
        for i in range(len(ptable)):
            for j in range(len(ptable[i])):
                if i == s:
                    self.table[i][j] = round(ptable[s][j] / ptable[s][e], 3)
                else:
                    self.table[i][j] = round(ptable[i][j] - ptable[s][j] * ptable[i][e] / ptable[s][e], 3)

    def compute_beta(self, prev_iter):
        s = prev_iter.output
        e = prev_iter.input
        pbeta = prev_iter.beta
        ptable = prev_iter.table
        for i in range(len(pbeta)):
            if i == s:
                self.beta[i] = pbeta[s] / ptable[s][e]
            else:
                self.beta[i] = pbeta[i] - pbeta[s] * ptable[i][e] / ptable[s][e]

    def compute_delta(self, prev_iter):
        s = prev_iter.output
        e = prev_iter.input
        pdelta = prev_iter.delta
        ptable = prev_iter.table
        for j in range(len(pdelta)):
            self.delta[j] = round(pdelta[j] - ptable[s][j] * pdelta[e] / ptable[s][e], 3)

    def compute_z(self, prev_iter):
        s = prev_iter.output
        e = prev_iter.input
        pdelta = prev_iter.delta
        ptable = prev_iter.table
        pbeta = prev_iter.beta
        pz = prev_iter.z
        self.z = round(pz - pbeta[s] * pdelta[e] / ptable[s][e], 3)

    def is_finish(self):
        for delta in self.delta:
            if delta > 0:
                return False
        return True

    def compute_from_prev_iter(self, prev_iter):
        self.base = deepcopy(prev_iter.base)
        self.index = deepcopy(prev_iter.index)
        self.table = deepcopy(prev_iter.table)
        self.beta = deepcopy(prev_iter.beta)
        self.delta = deepcopy(prev_iter.delta)
        self.base[prev_iter.output] = self.index[prev_iter.input]
        self.compute_table(prev_iter)
        self.compute_beta(prev_iter)
        self.compute_delta(prev_iter)
        self.compute_z(prev_iter)
        if not self.is_finish():
            self.compute_beta_index()

