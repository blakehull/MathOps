import sys

class Operator:

    def __init__(self):
        return None

    def poly_differential(self, polynomial = []):
        if len(polynomial) % 2 == 0:
            sys.tracebacklimit = 0
            raise ValueError("You need to have a space between each term and the signs (e.g. '3x^2 + 2x + 3')")
        return int("")

    def powerrule(self, coefficients=None, powers=[], funct=None):
        if coefficients == None:
            coefficients = []
            for i in range(len(powers)):
                coefficients.append(1)
        to_return = []
        if not funct:
            for c, i in enumerate(coefficients):
                print c,i,powers[c],i*powers[c]
                to_return.append(str(powers[c]*i) + str("x^" + str((powers[c] - 1))))
            return to_return
        return None