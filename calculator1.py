import num2words
import tabuada as t

def str_nrs(v1,op,v2,res):
    return str(v1) + op + str(v2) + " = " + str(res)

def calcula(v1, op, v2):
    res = s1 = s2 = None
    c = Calculator()
    if op == '+':
        res, s1, s2 = c.add(v1, v2)
    if op == '-':
        res, s1 = c.sub(v1, v2)
    if op == 'x':
        res, s1 = c.mult(v1, v2)
    if op == '/':
        res, s1 = c.div(v1, v2)
    if op == 'tab':
        s1= t.tabuada(v2)

    return res, s1, s2

class Calculator:

    def add(self, a, b, tipo='a'):
        """

               :param a:
               :param b:
               :param tipo: v=valor, m=expressão matemática, t=expressão textual, a=todos
               :return:
               """
        res= a+b
        matematica = str_nrs(a, '+', b, res)
        textual = num2words.num2words(a, lang='pt') + ' mais ' + \
                  num2words.num2words(b, lang='pt') + ' é igual a ' + \
                  num2words.num2words(res, lang='pt')
        if tipo == 'v':
            return res
        elif tipo == 'm':
            return matematica
        elif tipo == 't':
            return textual
        else:
            return res, matematica, textual

    def sub(self, a, b):
        res= a - b
        return res,str_nrs(a, '-', b, res)

    def mult(self, a, b):
        res= a * b
        return res,str_nrs(a, 'x', b, res)

    def div(self, a, b):
        if b==0:
            raise ZeroDivisionError('Divisao por zero')
        res= a / b
        return res,str_nrs(a, '/', b, res)