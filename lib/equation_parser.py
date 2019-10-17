import re

class EquationParser(object):
    def __init__(self, **kwargs):
        self._operand_1 = kwargs.get('operand_1', None)
        self._operator = kwargs.get('operator', None)
        self._operand_2 = kwargs.get('operand_2', None)
        self._string_equation = kwargs.get('string_equation', None)


    def evaluate(self):
        '''
        Evaluates equation and massages it to proper equation python can evaluate
        3_1/4 * 5_1/2 + 5

        :return: String
        3.25 * 5.5 + 5
        '''
        if self._operand_1 and self._operator and self._operand_2:
            split_equation = [self._operand_1,self._operator ,self._operand_2]
            string_equation = self.evaluate_equation_array(split_equation)
        elif self._string_equation:
            split_equation = self.split_equation_to_array()
            string_equation = self.evaluate_equation_array(split_equation)
        else:
            raise ValueError("Must supply equation")

        return string_equation

    def split_equation_to_array(self):
        if type(self._string_equation) == str:
            return self._string_equation.split()
        else:
            self._raise_value_error()

    def evaluate_equation_array(self, split_equation):
        '''
            Evaluates each index whether it be an operator or operand and joins
            the equation as an equation that can be easily evaluated
        :param split_equation: List
                ["3_1/4", "/", "1_1/2"]
        :return: String
                3.25 / 1.5
        '''
        array_equation = []
        for variable in split_equation:
            variable_string = str(variable)

            if self._variable_is_a_legal_operator(variable_string):
                array_equation.append(variable_string)

            elif self._variable_is_a_proper_operand(variable_string):
                mixed_decimal_number = self._evaluate_mixed_number(variable_string)
                array_equation.append(mixed_decimal_number)

            else:
                self._raise_value_error()

        return " ".join(array_equation)

    def legal_operators(self):
        return ["+","-","*","/"]

    def _variable_is_a_legal_operator(self, variable):
        if self._operator_contains_special_characters_and_no_number_characters(variable):
            if variable in self.legal_operators():
                return True
            else:
                raise ValueError('Illegal Operator Used: ' + variable + "\n Legal operators are: " + ", ".join(
                    self.legal_operators()))
        else:
            return False

    def _operator_contains_special_characters_and_no_number_characters(self, variable):
        if self._variable_contains_special_characters(variable):
            if self._variable_contains_numbers(variable):
                return False
            else:
                return True
        else:
            return False

    def _variable_contains_special_characters(self, variable):
        regex_everything_but_numbers = r"[^0-9]"

        if re.match(regex_everything_but_numbers, variable) is not None:
            return True
        else:
            return False

    def _variable_contains_numbers(self, variable):
        regex_numbers = r'\d'
        if re.search(regex_numbers, variable):
            return True
        else:
            return False

    def _variable_is_a_proper_operand(self, variable):
        contains_proper_amount_of_non_numeric_chars = self._operand_contains_proper_number_of_non_numeric_characters(variable)
        contains_numbers = self._variable_contains_numbers(variable)
        if contains_proper_amount_of_non_numeric_chars and contains_numbers:
            return True
        else:
            return False

    def _operand_contains_proper_number_of_non_numeric_characters(self, variable):
        number_of_slashes = 0
        number_of_negatives = 0
        for operator in self.legal_operators():
            if operator in variable:
                if operator == "/":
                    number_of_slashes += 1
                elif operator == "-":
                    number_of_negatives += 1
                else:
                    # * and + cannot be in an operand
                    return False

        if number_of_slashes > 1 or number_of_negatives > 1:
            return False
        else:
            return True

    def _raise_value_error(self):
        raise ValueError(
            'Please reevaluate equation and make sure there are spaces between operands and operators')

    def _evaluate_mixed_number(self, mixed_number):
        '''
        Takes sudo mixed number or decimal value and returns the equivalent decimal value
        :param mixed_number: String
                3_1/4, 5.5, 3_11/4, 11/4, -11/4

        :return: String
                3.25, 5.5, 5.75, 2.75, -2.75
        '''
        try:

            mixed_number_regex = r'(-*\d+\/*\d*)\_*([-*\d*\/*\d*|\.*\d*]*)'

            match = re.match(mixed_number_regex, mixed_number)

            integer_or_float_or_improper_fraction = match.group(1)
            fraction = match.group(2)

            evaluated_value = eval(integer_or_float_or_improper_fraction) if integer_or_float_or_improper_fraction else 0
            evaluated_fraction = eval(fraction) if fraction else 0

            if evaluated_value < 0:
                mixed_decimal_number = str(evaluated_value - evaluated_fraction)
            else:
                mixed_decimal_number = str(evaluated_value + evaluated_fraction)


            return mixed_decimal_number
        except:
            raise ValueError('Malformed Mixed number:' + mixed_number)