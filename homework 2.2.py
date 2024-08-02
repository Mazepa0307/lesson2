user_number = int(input("Enter a number:"))

cifra1 = user_number // 10000
cifra2 = user_number % 10000 // 1000
cifra3 = user_number % 1000 // 100
cifra4 = user_number % 100 // 10
cifra5 = user_number % 10

reversed_number = cifra5 * 10000 + cifra4 * 1000 + cifra3 * 100 + cifra2 * 10 + cifra1
print(reversed_number)
