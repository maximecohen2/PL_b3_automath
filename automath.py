#!/usr/local/bin/python3
# coding: utf-8

import argparse
import json
from src.MathIter import MathIter
from src.IterToScreen import IterToScreen


def parse_args():
    parser = argparse.ArgumentParser(description="Génère les itérations",
                                     usage="%(prog)s <JsonFile> [OPTIONS]")
    parser.add_argument("json", metavar="JsonFile", help="Nom du fichier json d'entré")
    parser.add_argument("-m", "--min", action="store_true", help="Minimiser le résultat")
    args = parser.parse_args()
    return args


def automath(data, args):
    displayer = IterToScreen()
    actual_iter = MathIter(args.min)
    actual_iter.set_first_iter(data)
    displayer.write_iter(actual_iter, "iteration 0")
    nb_iter = 1
    while not actual_iter.is_finish():
        prev_iter = actual_iter
        actual_iter = MathIter(args.min)
        actual_iter.compute_from_prev_iter(prev_iter)
        displayer.write_iter(actual_iter, "iteration " + str(nb_iter))
        nb_iter += 1


def main():
    args = parse_args()
    with open(args.json, "r") as json_file:
        json_data = json.loads(json_file.read())
        for data in json_data:
            automath(data, args)


if __name__ == '__main__':
    main()
