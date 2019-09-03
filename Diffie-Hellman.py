import random
import math as m


#Extended Euclid Alg
#a = e, b = phiN
def ExtendedEuc(a, b):
    #initializies for the equation
    pX, X = 1, 0
    pY, Y = 0, 1
    while b!=0:
        #integer division
        #if a < b then q = 0 and they just swap places
        q = a//b
        #x = new value, old = x
        X, pX = pX - q*  X, X
        Y, pY = pY - q * Y, Y
        a, b = b, a%b
    return (pX, pY)
    
#-------------------------------
#MillerRabin
def MillerRabin(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True
#--------------------------------
#Checks to see if the number is a composite, or a BaseCase
def BasePrime(n):

    if (n < 2):
        return False # 0, 1, and negative numbers are not prime
    #Array of all primes less than 1000
    BaseCase = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
                193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
                421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
                547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
                659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
                929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    #Checks to see if n is in the array BaseCase
    if n in BaseCase:
        return True
    #Check if n is a composite number
    for p in BaseCase:
        if (n % p == 0):
            return False
    return MillerRabin(n)
#------------------------------------
#Make large number, will continue to make numbers until a prime is made
def generateLargePrime(size):
    while True:
        num = random.randrange(2**(size-1), 2**(size))
        if BasePrime(num):
            return num
#-----------------------------------
#Encryption of message
def Encryption(e,n):
    m = open("message.txt","r")
    msg = int(m.read())
    ct = pow(msg,e,n)
    m.close()
    temp = open("ciphertext.txt","w+")
    temp.write(str(ct))
    temp.close()
#-----------------------------------
#Decryption of ciphertext
def Decryption(d,n):
    m = open("message.txt","r")
    c = open("ciphertext.txt","r")

    msg = int(m.read())
    ct = int(c.read())

    m.close()
    c.close()
    
    dec = pow(ct,d,n)
    
    temp = open("decrypted_message.txt","w+")
    temp.write(str(dec))
    temp.close()
    
#-----------------------------------
#MAIN
#Number of bits the number p will have
sizep = random.randrange(6,100)
#Keeps the two numbers relatively the same size
sizeq = random.randrange(sizep-2,sizep+2)

#This makes p and q
p =generateLargePrime(sizep)
q =generateLargePrime(sizeq)

N = p * q

phiN = (p-1)*(q-1)
x = 16
#If 2^16 + 1 is not relatively prime to phi of N
while m.gcd((2**x+1),phiN)!= 1:
    x+=1;
#Encryption value
e=2**x+1
#print("e= ",e)
XY = ExtendedEuc(e,phiN)
#Checks to see if x <0
if (XY[0] < 0):
    d = XY[0] + phiN
else:
    d = XY[0] 

#Opens and closes the public and private key text documents after writing in the relevant information
pk= open("public_key.txt","w+")
prik = open("private_key.txt","w+")
pk.write(str(N))
pk.write("\n")
pk.write(str(e))
pk.close()
prik.write(str(d))
prik.close()
Encryption(e,N)
Decryption(d,N)


