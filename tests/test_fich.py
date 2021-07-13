import unittest
from unittest import mock
import csv
import fich
import pathlib as pl


def criaFichTeste(filename):
    dados = [['257', '+', '38'],
             ['5', 'x', '2'],
             ['85', '+', '927'],
             ['0', 'tab', '5']]

    with open(filename,'w', newline ='') as f:
        novo_fich=csv.writer(f)
        novo_fich.writerows(dados)



class TestarFich(unittest.TestCase):

    def test_lerFich(self):
        fichTeste = r'c:\Users\Nuno\Desktop\file2.csv'
        criaFichTeste(fichTeste)
        lista = fich.lerFich(fichTeste )
        self.assertEqual(lista, [['257', '+', '38'], ['5', 'x', '2'], ['85', '+', '927'],  ['0', 'tab', '5']])

    def test_apagaFich(self):
        filename = r'c:\Users\Nuno\Desktop\file2_res.csv'
        fich.apagaFich(filename)
        path = pl.Path(filename)
        self.assertFalse(path.is_file())

    @mock.patch('fich.calc.calcula', return_value=(3, '1+2=3', 'um mais dois é igual a três'))
    def test_procFich(self, mock_calculo):
        fichTeste = r'c:\Users\Nuno\Desktop\file2.csv'
        criaFichTeste(fichTeste)
        fich.procFich(fichTeste)

        lista = fich.lerFich(r'c:\Users\Nuno\Desktop\file2_res.csv')

        listaPrevista = []
        for i in range(len(lista)):
            listaPrevista.append(['1+2=3'])

        self.assertListEqual(lista, listaPrevista)

if __name__ == '__main__':
    unittest.main()
