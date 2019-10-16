#!/usr/bin/env python3

import argparse
from lib.equation_parser import EquationParser
from lib.evaluate_equation import EvaluateEquation


"""
Author: Steven Greenup
Date: 10.15.19
Problem: 

Coding Challenge


Write a command line program in the language of your choice that will take operations on fractions as an input and produce a fractional result.


* Legal operators shall be *, /, +, - (multiply, divide, add, subtract)

* Operands and operators shall be separated by one or more spaces

* Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"

* Improper fractions and whole numbers are also allowed as operands


Example Command Lines
    ./script.py --string_equation "3_1/4 * 5_1/2"
    ./script.py --string_equation "3_1/4 / -5 + 11/4"
    ./script.py --string_equation "3_1/4 / -5_1/2 - 11/4"
    
    
    ./script.py --operand1 "3_1/4" --operator "*" --operand2 "3_1/4"
"""



parser = argparse.ArgumentParser(description='')

parser.add_argument('--operand1',
                    help="first operand",
                    required=False)

parser.add_argument('--operator',
                    help="operator",
                    required=False)

parser.add_argument('--operand2',
                    help="second operand",
                    required=False)

parser.add_argument('--string_equation',
                    help="equation to evaluate",
                    required=False)

args = parser.parse_args()



def parse_equation():
    string_equation = args.string_equation
    operand1 = args.operand1
    operand2 = args.operand2
    operator = args.operator

    equation_parser = EquationParser(string_equation=string_equation,
                                     operand_1=operand1,
                                     operand_2=operand2,
                                     operator=operator)

    return equation_parser.evaluate()

def main():
    string_equation = parse_equation()
    evaluate_equation = EvaluateEquation(equation=string_equation)


    print("Equation: ",string_equation)
    print('Decimal value: ', evaluate_equation.to_decimal())
    print("Fraction value:", evaluate_equation.to_fraction())
    print("Mixed Number value:", evaluate_equation.to_mixed_number())


if __name__ == '__main__':
    main()