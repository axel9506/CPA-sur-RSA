import os
import matplotlib.pyplot as plt


def curve():
    curves = []

    for curve_name in os.listdir('Ressources'):
        curves.append(curve_name)
    
    print("curves:\n", curves)

def generate(name, number):
    result = []
    for i in range(number):
        with open("Ressources/" + name + str(i) + ".txt", "r") as file:
            for line in file:
                if name == "curve_":
                    result.append([float(X) for X in line.split()])
                else:
                    result.append(int(line.split()[0]))
    return result

Y = generate("curve_", 5)
X = [k for k in range(len(Y[0]))]
print(Y[0])
print(X)

plt.plot(X, Y[0])
plt.axis([0, len(X), 0, max(Y[0])])
plt.xlabel("time")
plt.ylabel("consommation")
plt.show()

