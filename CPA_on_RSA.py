import os
import matplotlib.pyplot as plt

print("Welcome to Axel's and Yassine's baby RSA !")

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

# find N in the files
N = open("Ressources/N.txt", "r").readlines()[0]
print(f"N : {N}")

# get the curves from the files
curves = generate("curve_", 999)
x_curves = [k for k in range(len(curves[0]))]

# get the messages from the files
messages = generate("msg_", 999)

plt.plot(x_curves, curves[0])
plt.axis([0, len(x_curves), 0, max(curves[0])])
plt.xlabel("time")
plt.ylabel("consommation")
plt.show()