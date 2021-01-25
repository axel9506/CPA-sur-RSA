import os
import matplotlib.pyplot as plt

curves = []

for curve_name in os.listdir('Ressources'):
    file_rd = open(curve_name)
    file_rd.readlines()
    

print("curves:\n", curves)