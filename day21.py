import aocinput
from sympy import sympify, solve

DAY = 21

class Monke:
    def __init__(self, function, name=''):
        self.name = name
        self.function = function
        self.monke_1, self.monke_2 = (function[0:4], function[7:11]) if not function.isdigit() else (None, None)
        self.num = int(function) if function.isdigit() else None
        self.first_val, self.second_val = None, None
    
    def get_num(self, monkes):
        if self.name == 'humn':
            return None
        return self.evaluate(monkes) if not self.num else self.num

    def get_monke_wo_calc_num(self): #get monke without calculated num
        return self.monke_1 if not self.first_val else self.monke_2

    def evaluate(self, monkes):
        self.first_val = monkes[self.monke_1].get_num(monkes)
        self.second_val = monkes[self.monke_2].get_num(monkes)
        return int(eval(self.function, {self.monke_1: self.first_val, self.monke_2: self.second_val})) if (self.first_val and self.second_val) else None
    def solve_eq(self, score):
        eq = self.function.replace(str(self.monke_1), str(self.first_val).lower())
        eq = eq.replace(str(self.monke_2), str(self.second_val).lower())
        return solve(sympify(f"Eq({eq.replace(' ', '')},{score})"))[0]
    def a(input):
        monkes = {name:Monke(function) for name,function in [line.split(': ') for line in aocinput.import_aoc_readlines(DAY)]}
        