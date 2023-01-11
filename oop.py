import Foundation

class NameOfClass():

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def some_method(self):
        # executa alguma ação
        pass

class Calculadora():

    def __init__(self):
        pass

    def soma(self, n1, n2):
        return n1 + n2
    
    def subtracao(self, n1, n2):
        return n1 - n2
    
    def multiplicacao(self, n1, n2):
        return n1 * n2
    
    def divisao(self, n1, n2):
        return n1 / n2

calc = Calculadora()
# print(calc.divisao(calc.soma(6,2), calc.soma(1,1)))