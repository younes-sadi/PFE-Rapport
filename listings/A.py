a = float(input("Mag Controle:"))
aa = float(input("Mag Tp :"))

b= float(input("AL Controle:"))
bb= float(input("AL TP:"))

c = float(input("ABD Controle:"))
cc = float(input("ABD TP:"))

d = float(input("POA Controle:"))
dd = float(input("POA TP:"))

f = float(input("SOACC Controle:"))
ff = float(input("SOACC TP:"))


m = float(input("IDM Controle:"));
mm = float(input("IDM TP:"));

mag = (a*0.67 + aa*0.33)*3
al = (b*0.6+bb*0.4)*3
abd = (c*0.67+cc*0.33)*3
poa = (d*0.67+dd*0.33)*4
idm = (m*0.67+mm*0.33)*4
soacc = ((f*2+ff)/3)*4
print(mag/3)
print(al/3)
print(abd/3)
print(poa/4)
print(idm/4)
print(soacc/4)






moyenne = (mag+al+abd+poa+idm+soacc)/21
print(moyenne)