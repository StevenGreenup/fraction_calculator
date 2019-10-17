import unittest
from lib.equation_parser import EquationParser
from lib.evaluate_equation import EvaluateEquation

class TestIntegrationEquationParserAndEvaluate(unittest.TestCase):

    def equation_with_singular_sudo_mixed_fraction(self):
        return "3_1/4"

    def equation_with_singular_sudo_negative_improper_fraction(self):
        return "-11/4"

    def equation_with_singular_sudo_positive_improper_fraction(self):
        return "11/4"

    def equation_with_two_proper_positive_operands(self):
        return "3_1/2 + 1_3/4"


    def test_will_properly_evaluate_simple_operand(self):
        equation_parser = EquationParser(string_equation=self.equation_with_singular_sudo_mixed_fraction())
        string_equation = equation_parser.evaluate()

        evaluate = EvaluateEquation(equation=string_equation)
        mixed_number = evaluate.to_mixed_number()
        decimal_number = evaluate.to_decimal()

        self.assertEqual(decimal_number, 3.25)
        self.assertEqual(mixed_number, "3_1/4")

    def test_will_properly_evaluate_a_negative_mixed_number(self):
        equation_parser = EquationParser(string_equation=self.equation_with_singular_sudo_negative_improper_fraction())
        string_equation = equation_parser.evaluate()

        evaluate = EvaluateEquation(equation=string_equation)
        mixed_number = evaluate.to_mixed_number()
        decimal_number = evaluate.to_decimal()

        self.assertEqual(decimal_number, -2.75)
        self.assertEqual(mixed_number, "-2_3/4")

    def test_will_properly_evaluate_a_positive_mixed_number(self):
        equation_parser = EquationParser(string_equation=self.equation_with_singular_sudo_positive_improper_fraction())
        string_equation = equation_parser.evaluate()

        evaluate = EvaluateEquation(equation=string_equation)
        mixed_number = evaluate.to_mixed_number()
        decimal_number = evaluate.to_decimal()

        self.assertEqual(decimal_number, 2.75)
        self.assertEqual(mixed_number, "2_3/4")

    def test_will_properly_evaluate_simple_equation(self):
        equation_parser = EquationParser(string_equation=self.equation_with_two_proper_positive_operands())
        string_equation = equation_parser.evaluate()

        evaluate = EvaluateEquation(equation=string_equation)
        mixed_number = evaluate.to_mixed_number()
        decimal_number = evaluate.to_decimal()

        self.assertEqual(decimal_number, 5.25)
        self.assertEqual(mixed_number, "5_1/4")



if __name__ == '__main__':
    unittest.main()