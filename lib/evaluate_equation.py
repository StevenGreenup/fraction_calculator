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
        num = int(fraction.numerator)
        den = int(fraction.denominator)

        integral_part = num // den
        fractional_part_num = num % den

        if fractional_part_num > 0:
            return ("%s_%s/%s" % (integral_part, fractional_part_num, den))
        else:
            return ("%s" % integral_part)