import os
import matplotlib.pyplot as plt

curves = []

for curve_name in os.listdir('Ressources'):
    curves.append(curve_name)

print("curves:\n", curves)