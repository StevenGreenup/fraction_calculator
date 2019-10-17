from fractions import Fraction

class EvaluateEquation(object):
    def __init__(self, **kwargs):
        self._equation = kwargs.get('equation', None)
        self.value = self._evaluate()

    def _evaluate(self):
        if self._equation:
            return eval(self._equation)
        else:
            raise ValueError('Must supply equation')

    def to_decimal(self):
        return self.value

    def to_fraction(self):
        return Fraction(self.value)

    def to_mixed_number(self):
        fraction = self.to_fraction()

        num, den = (int(fraction.numerator), int(fraction.denominator))

        whole_part = abs(num) // den

        if num < 0:
            whole_part = -whole_part

        fractional_part_num = abs(num) % den

        if fractional_part_num > 0:


            return ("%s_%s/%s" % (whole_part, fractional_part_num, den))
        else:
            return ("%s" % whole_part)