import os
import sympy
import matplotlib.pyplot as plt

print("Welcome to Axel's and Yassine's baby RSA !")

def hamming_weigth(dec): return bin(dec).count('1')

def mat_hyp(msg_list, n):
    # 65536 key hyoptheses
    # result is a 65536 x 1000 matrice with a hypothese for each msg for each hypothese of key
    result = []

    for d in range(65536):
        print(100*d/65536, "%")
        result.append([])
        for msg in msg_list:
            result[d].append(hamming_weigth(pow(int(msg),d)%n))

    return result

def solution():
    N = 95559869
    E = 65535
    P = 2
    while (N%P != 0):
        P = sympy.nextprime(P)
    Q = N//P
    PHI = (P-1)*(Q-1)
    D = mod_inverse(E,PHI)
    print("P: ", P)
    print("Q: ", Q) 
    print("D: ", D)


def mod_inverse(x,m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break

        elif n == m - 1:
            return "Null"
        else:
            continue

def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)

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

# find N in the files 95559869
N = int(open("Ressources/N.txt", "r").readlines()[0])
print(f"N : {N}")
# solution()

# get the curves from the files
curves = generate("curve_", 1000)
x_curves = [k for k in range(len(curves[0]))]

# get the messages from the files
messages = generate("msg_", 1000)

# public exponent
E = 65535

# show the results
# plt.plot(x_curves, curves[0])
# plt.axis([0, len(x_curves), 0, max(curves[0])])
# plt.xlabel("time")
# plt.ylabel("consommation")
# plt.show()

print(mat_hyp(messages, N))