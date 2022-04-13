x = int(input("Tapez la valeur de x : "))
print("----------------------------------------")
print("Voici la table de multiplication de " ,x)
print("----------------------------------------")
for i in range(1,10):
    print(i, " x ", x ,"=",i*x)
print("----------------------------------")
print("Voici la table des puissances de " ,x)
print("----------------------------------")
for u in range(1,10):
    print(x, " puissance ", u ,"=",x**u)

