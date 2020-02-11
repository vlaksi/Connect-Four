"""
Modul u kome vrsimo iscitavanje podataka.
"""
import csv

# Dve liste koje sluze iscitavanje trainingSet kako bi vrsil numericke proracune nad njima
x = []
y = []
pom_y = []

# Iscitavanje iz fajla i smestanje u liste x i y
with open('trainingSet.csv', 'r') as csvfile:
    citac = csv.reader(csvfile, delimiter='\t')
    next(citac)
    for entitet in citac:
        x.append(int(entitet[0]))
        y.append(int(entitet[1]))

# Ispisivanje ucitanih lista
#print(x)
#print(y)