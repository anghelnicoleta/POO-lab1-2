n=int(input("Dati numarul dorit:"))
print("8.1.1")
print("n*8=",n*8)
print("8.1.2")
print("Catul impartirii lui n la 4 este ",n/4)
print("8.1.3")
print("n*10 cu operatorii logici de deplasare la nivel de bit=",(n<<2<<1)+(n<<1))
print("8.2")
if((n&1)==0):
    print("Nr par")
else:
    print("Nr impar")
print("8.3")
x=int(input("Dati x:"))
n=int(input("Dati n:"))
print("Bitul n din x este:",(x & (1<<n)))
print("8.4.1")
print("setarea n la valoarea 0: ",(x & (255 ^ (1 << n))))
print("setarea n la valoarea 1:",(x | (1 << n)))
print("8.4.3")
print("șterge bitul n:",(x & ~(1 << n)))
print("8.4.4")
print("complementează bitul n:",(x ^ 1 << n))
print("8.5.1")
a=int(input("Dati a:"))
b=int(input("Dati b:"))
a = a + b
b = a - b
a = a - b
print(a," ",b)
a=int(input("Dati a:"))
b=int(input("Dati b:"))
a = a ^ b
b = a ^ b
a = a ^ b
print(a," ",b)
print("8.6")
n=int(input("Dati n:"))
k=int(input("Dati k:"))
if (n == (1<<k)):
    print("este")
else:
    print("Nu este")
print("8.7")
m=int(input("Dati m:"))
p=int(input("Dati p:"))
q=int(input("Dati q:"))
r=int(input("Dati r:"))
m = m % pow(2, r)
p = p % pow(2, q)
p = p << r
m = m | p
print("Noua valoare a lui p este:",p)