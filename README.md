# fraction_calculator


Author: Steven Greenup

Date: 10.15.19

Problem: 

Coding Challenge


Write a command line program in the language of your choice that will take operations on fractions as an input and produce a fractional result.


* Legal operators shall be *, /, +, - (multiply, divide, add, subtract)

* Operands and operators shall be separated by one or more spaces

* Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"

* Improper fractions and whole numbers are also allowed as operands


#MUST BE RAN WITH python3

Example Command Lines

    ./script.py --string_equation "3_1/4 * 5_1/2"
    ./script.py --string_equation "3_1/4 / -5 + 11/4"
    ./script.py --string_equation "3_1/4 / -5_1/2 - 11/4"
        
    ./script.py --operand1 "3_1/4" --operator "*" --operand2 "3_1/4"
    
    
RUN TESTS
    
    cd path/to/fraction_calc
    python3 -m unittest discover