import sys
import re

class Differential:

    class Function:
        def __init__(self, func):
            self.func = func
            self.variables = self.extract_variables()
            self.powers = self.extract_powers()
            self.coefficients = self.extract_coefficients()

        def extract_variables(self):
            to_return = []
            for char in self.func:
                if char.isalpha():
                    to_return.append(char)
            return list(set(to_return))

        def extract_powers(self):
            powers = {}
            tokey = []
            for term in self.func.split():
                if term not in ['+', '-']:
                    var = "".join(re.findall("[a-zA-Z]+", term))
                    try:
                        tokey = term.split('^')[1]
                    except:
                        tokey = '1'


                    if var in powers.keys():
                        powers[var].append(tokey)
                    else:
                        powers[var] = [tokey]
                tokey = []
            return powers

        def extract_coefficients(self, var=None):
            to_return = {}
            powers = {}
            for term in self.func.split():
                if term not in ['+', '-']:
                    for char in term:
                        if term[0].isalpha():
                            try:
                                whichpower = term.split('^')[1]
                            except IndexError:
                                whichpower = '1'

                            powers[whichpower] = 1

                        if term.isnumeric():
                            if 'constant' in powers.keys():
                                powers['constant'].append(char)
                            else:
                                powers['constant'] = [char]
                        if char.isnumeric():
                            try:
                                whichpower = term.split('^')[1]
                            except IndexError:
                                whichpower = '1'

                            if whichpower in powers.keys():
                                powers[whichpower].append(char)
                            else:
                                powers[whichpower] = [char]
                        else:
                            break
            for key in powers:
                if type(powers[key]) == list:
                    concat = ''.join(powers[key])
                    powers[key] = concat
            return powers


        def get_powers(self):
            return self.powers

        def get_variables(self):
            return self.variables

        def get_coefficients(self):
            return self.coefficients

        def get_function(self):
            return self.func

    def derivative(self, order=int, func=Function):
        to_return = []
        if order < 1:
            return func.get_function()
        for i in range(0, order):
            powers = func.get_powers()
            var = func.get_variables()
            coefficients = func.get_coefficients()
            for pow in powers[var[0]]:
                newpow = int(pow) - 1
                if newpow == 0:
                    newpow = ''
                elif newpow == 1:
                    newpow = var[0] + ''
                else:
                    newpow = var[0] + '^' + str(newpow)

                term = str(int(coefficients[pow]) * int(pow)) + newpow
                to_return.append(term)
            func = self.Function(' + '.join(to_return))
            newfunction = ' + '.join(to_return)
            to_return = []
        return newfunction


class Integration:

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
                print(c,i,powers[c],i*powers[c])
                to_return.append(str(powers[c]*i) + str("x^" + str((powers[c] - 1))))
            return to_return
        return None