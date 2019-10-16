import unittest
from .equation_parser import EquationParser


class TestEquationParser(unittest.TestCase):

    def equation_with_singular_sudo_mixed_fraction(self):
        return "3_1/4"

    def equation_with_singular_sudo_negative_improper_fraction(self):
        return "-11/4"

    def equation_with_two_proper_operands(self):
        return "3_1/4 / 1_1/2"

    def equation_with_decimal_mixed_numbers(self):
        return "5.5 + 4.1"

    def equation_with_more_than_two_operands(self):
        return "3_1/4 / 1_1/2 * 5.5"

    def equation_with_more_than_two_operands_with_negative_values(self):
        return "-3_1/4 / -1_1/2 * -5.5"

    def equation_with_no_spaces(self):
        return "3_1/4*5+11/4"

    def equation_with_whole_number_as_operand(self):
        return "3_1/4 + 7"

    def equation_with_improper_fraction(self):
        return "3_11/4 + 7"

    def equation_with_improper_fraction_as_operand(self):
        return "11/4 + 7"

    def equation_with_illegal_operator(self):
        return "3_1/4 / 1_1/2 % 5_9/10"

    def legal_operators(self):
        return ["+","-","*","/"]

    def example_illegal_operators(self):
        return ['^','$','#', '@']

    def example_proper_operands(self):
        return ['3_11/4', '11/4', '5', '5.5', "-11/4"]

    def example_int_array(self):
        return [3,"+",5]

    def test_legal_operators(self):
        equation_parser = EquationParser()
        for operator in self.legal_operators():
            self.assertTrue(equation_parser._variable_is_a_legal_operator(operator))

    def test_illegal_operators(self):
        equation_parser = EquationParser()
        for illegal_operator in self.example_illegal_operators():
            self.assertRaises(ValueError, equation_parser._variable_is_a_legal_operator, illegal_operator)

    def test_proper_operands(self):
        equation_parser = EquationParser()
        for operand in self.example_proper_operands():
            self.assertTrue(equation_parser._variable_is_a_proper_operand(operand))

    def test_will_return_correct_constants_from_equation(self):
        equation_parser = EquationParser(string_equation=self.equation_with_singular_sudo_mixed_fraction())
        value = equation_parser.evaluate()
        self.assertEqual(value, "3.25", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_will_return_correct_constants_from_equation_with_negative_improper_fraction(self):
        equation_parser = EquationParser(string_equation=self.equation_with_singular_sudo_negative_improper_fraction())
        value = equation_parser.evaluate()
        self.assertEqual(value, "-2.75", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_will_split_equation_to_proper_array(self):
        equation_parser = EquationParser(string_equation=self.equation_with_two_proper_operands())
        split_equation = equation_parser.split_equation_to_array()
        self.assertEqual(split_equation, ["3_1/4", "/", "1_1/2"], "")

    def test_will_return_correct_constants_from_equation_2(self):
        equation_parser = EquationParser(string_equation=self.equation_with_two_proper_operands())
        value = equation_parser.evaluate()
        self.assertEqual(value, "3.25 / 1.5", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_will_return_correct_constants_from_equation_with_decimal_mixed_numbers(self):
        equation_parser = EquationParser(string_equation=self.equation_with_decimal_mixed_numbers())
        value = equation_parser.evaluate()
        self.assertEqual(value, "5.5 + 4.1", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_will_return_correct_constants_from_equation_with_more_than_two_operands(self):
        equation_parser = EquationParser(string_equation=self.equation_with_more_than_two_operands())
        value = equation_parser.evaluate()
        self.assertEqual(value, "3.25 / 1.5 * 5.5", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_will_return_correct_constants_from_equation_with_more_than_two_operands_with_negative_values(self):
        equation_parser = EquationParser(string_equation=self.equation_with_more_than_two_operands_with_negative_values())
        value = equation_parser.evaluate()
        self.assertEqual(value, "-3.25 / -1.5 * -5.5", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_will_return_correct_constants_from_equation_6(self):
        equation_parser = EquationParser(string_equation=self.equation_with_whole_number_as_operand())
        value = equation_parser.evaluate()
        self.assertEqual(value, "3.25 + 7", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_will_return_correct_constants_from_equation_7(self):
        equation_parser = EquationParser(string_equation=self.equation_with_improper_fraction_as_operand())
        value = equation_parser.evaluate()
        self.assertEqual(value, "2.75 + 7", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_will_return_correct_constants_with_improper_fractions_from_equation(self):
        equation_parser = EquationParser(string_equation=self.equation_with_improper_fraction())
        value = equation_parser.evaluate()
        self.assertEqual(value, "5.75 + 7", "Should convert sudo mixed numbers to decimal values in string equation")

    def test_should_return_exception_if_no_spaces_in_equation(self):
        equation_parser = EquationParser(string_equation=self.equation_with_no_spaces())
        self.assertRaises(ValueError, equation_parser.evaluate)

    def test_should_raise_exception_if_illegal_operator_in_equation(self):
        equation_parser = EquationParser(string_equation=self.equation_with_illegal_operator())
        self.assertRaises(ValueError, equation_parser.evaluate)

    def test_equation_parser_will_handle_integer_values(self):
        equation_parser = EquationParser()
        value = equation_parser.evaluate_equation_array(self.example_int_array())
        self.assertEqual(value, "3 + 5")

if __name__ == '__main__':
    unittest.main()