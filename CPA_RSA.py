import os
import sympy
import matplotlib.pyplot as plt
import numpy as np

print("Welcome to Axel's and Yassine's baby RSA !")

def hamming_weight(dec): return bin(dec).count('1')

def hamming_distance(a, b): return hamming_weight(a^b)

def M_d_mod_N(M, d, N):
    T = M
    for i in range(len(d)-2, -1, -1):
        T = (T**2) % N
        if (d[i] == 1):
            T = (T*M) % N
        elif (i == 0):
            T = (T**2) % N
    return T

def read_mat_hyp():
    result = []
    file_read = open("mat_hyp.txt", "r")
    for line in file_read:
        result.append([int(X) for X in line.split()])
    return result

def mat_hyp(msg_list, n):
    # 65536 key hyoptheses
    # result is a 65536 x 1000 matrice with a hypothese for each msg for each hypothese of key
    result = []
    prog = 0
    printed = 0

    for d in range(65536):
        prog = 100*d//65536
        if (prog%100 > printed):
            print("progress:",prog, "%")
            printed += 1
        result.append([])
        for msg in msg_list:
            result[d].append(hamming_distance(msg, M_d_mod_N(msg, bin(d), n)))
            
    return result

def solution():
    N = 95559869
    # public exponent
    E = 65537
    P = 2
    while (N%P != 0):
        P = sympy.nextprime(P)
    print("P: ", P)
    Q = N//P
    print("Q: ", Q) 
    PHI = (P-1)*(Q-1)
    D = mod_inverse(E,PHI)
    print("D: ", D)
    return D


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

def MESD(msg_list, curves_list, N):
    # find the private exponent with Multiple-Exponent Single Data Attack
    e = [1]

    i = 0
    while (curves_list[0][i] >= 0):
        S1, S0 = [], []

        e1 = [1] + e
        e0 = [0] + e

        for m in msg_list:  
            S1.append(hamming_weight(M_d_mod_N(m, e1, N)))
            S0.append(hamming_weight(M_d_mod_N(m, e0, N)))

        D1 = np.corrcoef(S1, np.array(curves_list)[:, i:i+1], False)[1][0]
        D0 = np.corrcoef(S0, np.array(curves_list)[:, i:i+1], False)[1][0]

        if D1 >= D0:
            e = [1] + e
            i += 2
        else:
            e = [0] + e
            i += 1
        
    e.reverse()
    print("length:",len(e))
    return e


# find N in the files 95559869
N = int(open("Ressources/N.txt", "r").readlines()[0])

# get the curves from the files
curves = generate("curve_", 1000)
x_curves = [k for k in range(len(curves[0]))]

# get the messages from the files
messages = generate("msg_", 1000)


# hyp_matrice = np.array(mat_hyp(messages,N))
#hyp_matrice = read_mat_hyp()
#print("dimensions:",len(hyp_matrice),"x",len(hyp_matrice[0]))
#corr_matrice = np.corrcoef(np.transpose(hyp_matrice), np.array(curves), False)

# show the results
#plt.plot(x_curves, curves[1])
#plt.axis([0, len(x_curves), 0, max(curves[5])])
#plt.xlabel("time")
#plt.ylabel("consommation")
#plt.show()
#print("length:", len(curves[1]))


#print("Solution by brute force:")
#solution()
#28.151.873

E = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

key = MESD(messages, curves, N)
key.reverse()
print("MESD:", key)
key_s = [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
key_s.reverse()

cipher = M_d_mod_N(85, key, N)
decipher = M_d_mod_N(cipher, E, N)

cipher_s = M_d_mod_N(85, key_s, N)
decipher_s = M_d_mod_N(cipher_s, E, N)

print("MESD cipher:", cipher)
print("MESD decipher:", decipher)
print("solution cipher:", cipher_s)
print("solution cipher:", decipher_s)
