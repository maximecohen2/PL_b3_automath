#!/usr/bin/python3
# coding: utf-8

import argparse
from src.MathIter import MathIter
from src.IterToScreen import IterToScreen
from data import data


def parse_args():
    parser = argparse.ArgumentParser(description="Generate table",
                                     usage="%(prog)s [OPTIONS]")
    parser.add_argument("-x", "--excel", metavar="fileName", help="Write to the excel file", type=str)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    displayer = IterToScreen()
    actual_iter = MathIter()
    actual_iter.set_first_iter(data)
    displayer.write_iter(actual_iter, "iteration 0")
    nb_iter = 1
    while not actual_iter.is_finish():
        prev_iter = actual_iter
        actual_iter = MathIter()
        actual_iter.compute_from_prev_iter(prev_iter)
        displayer.write_iter(actual_iter, "iteration " + str(nb_iter))
        nb_iter += 1



if __name__ == '__main__':
    main()
