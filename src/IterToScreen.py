#!/usr/bin/python3
# coding: utf-8

from terminaltables import AsciiTable


class IterToScreen():

    def get_blank_line(self, math_iter):
        line = ["" for x in range(3 + len(math_iter.index) + 3)]
        return line

    def get_first_line(self, math_iter):
        line = self.get_blank_line(math_iter)
        line[1] = "base"
        for i, index in enumerate(math_iter.index):
            line[3 + i] = index
        line[3 + len(math_iter.index) + 1] = "beta"
        return line

    def get_middle_lines(self, math_iter):
        for i, base in enumerate(math_iter.base):
            line = self.get_blank_line(math_iter)
            if math_iter.output == i:
                line[0] = "S"
            line[1] = str(base)
            for j, table in enumerate(math_iter.table[i]):
                line[3 + j] = str(table)
            line[3 + len(math_iter.index) + 1] = str(math_iter.beta[i])
            line[3 + len(math_iter.index) + 2] += math_iter.betaIndex[i] if i < len(math_iter.betaIndex) else ""
            yield line

    def get_last_line(self, math_iter):
        line = self.get_blank_line(math_iter)
        line[1] = "delta"
        for i, delta in enumerate(math_iter.delta):
            line[3 + i] = str(delta)
        line[3 + len(math_iter.delta) + 1] = str(math_iter.z)
        return line

    def get_input_line(self, math_iter):
        line = self.get_blank_line(math_iter)
        if math_iter.input is not None:
            line[3 + math_iter.input] = "E"
        return line

    def init_table_instance(self, table, name):
        table_instance = AsciiTable(table, name)
        for i in range(len(table[0])):
            table_instance.justify_columns[i] = 'center'
        table_instance.inner_heading_row_border = False
        table_instance.inner_column_border = False
        return table_instance

    def write_iter(self, math_iter, name):
        table = list()
        table.append(self.get_first_line(math_iter))
        table.append(self.get_blank_line(math_iter))
        for line in self.get_middle_lines(math_iter):
            table.append(line)
        table.append(self.get_blank_line(math_iter))
        table.append(self.get_last_line(math_iter))
        table.append(self.get_input_line(math_iter))
        table_instance = self.init_table_instance(table, name)
        print(table_instance.table)

    def open(self):
        pass

    def close(self):
        pass