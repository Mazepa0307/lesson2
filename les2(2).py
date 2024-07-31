user_number = int(input("Enter a number:"))

cifra1 = user_number // 10000
cifra2 = user_number % 10000 // 1000
cifra3 = user_number % 1000 // 100
cifra4 = user_number % 100 // 10
cifra5 = user_number % 10

lst = []
lst.append(cifra1)
lst.append(cifra2)
lst.append(cifra3)
lst.append(cifra4)
lst.append(cifra5)
for i in lst [::-1]:
    print(i,end='')
