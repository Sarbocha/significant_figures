zeros = 0
significant_number = 0
non_significant = 0
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

number_before_decimal = float(input("Enter total numbers before decimal points:"))
i = 0

variables = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
while i <= number_before_decimal:
    i = i + 1
    variables[i] = float(input("Enter the number serially:"))

    if variables[i] in list:
        significant_number += 1
    elif variables[0] == 0:
        non_significant += 1
    elif variables[i] == 0:
        non_significant += 1
    else:
        print("No numbers")





angstorm = 0
variable = ["ab", "bc", "cd", "de", "ef", "fg", "gh", "hi", "ij", "jk"]
number_after_decimal = float(input("Enter total numbers after decimal points:"))
while angstorm <= number_after_decimal:
    angstorm = angstorm + 1
    variable[angstorm] = float(input("Enter the number serially:"))

    if variable[angstorm] in list:
        significant_number += 1
    elif variable[angstorm] == 0:
        non_significant += 1
    elif variable[angstorm] == 0:
        non_significant += 1
    else:
        print("No numbers")

total_number = number_after_decimal + number_after_decimal
print(non_significant)
print(significant_number)






