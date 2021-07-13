import os
import csv
import calculator1 as calc

def lerFich(filename):
    with open(filename) as f:
        reader =csv.reader(f)
        lista = list(reader)
    return lista

def apagaFich(filename):
    if os.path.exists(filename):
        os.remove(filename)


def procFich(filename):
    out_file=filename[0:len(filename)-4] + "_res.csv"
    apagaFich(out_file)

    lista_ops=lerFich(filename)

    with open(out_file, 'a', newline='') as f_out:
        fich_res = csv.writer(f_out)
        for linha in lista_ops:
            res = s1 = s2 = None

            v1=int(linha[0])
            v2=int(linha[2])
            op=linha[1]
            res, s1, s2 = calc.calcula(v1, op, v2)

            fich_res.writerow([s1])


fichTeste = r'c:\Users\Nuno\Desktop\file2.csv'
procFich(fichTeste)