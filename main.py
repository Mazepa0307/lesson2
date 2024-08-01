user_number = int(input("Enter a number:"))

cifra1 = user_number // 10000
cifra2 = user_number % 10000 // 1000
cifra3 = user_number % 1000 // 100
cifra4 = user_number % 100 // 10
cifra5 = user_number % 10

print(cifra5, cifra4, cifra3, cifra2, cifra1)
