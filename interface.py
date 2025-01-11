from deviation import calculate_statistics # type: ignore
ub = float(input("Podaj niepewność typu b: "))
count = int(input("Podaj liczbę pomiarów do wprowadzenia: "))
parameters = []
for i in range(0, count):
    parameters.append(float(input(f"Podaj parametr {i+1}: ")))
print(parameters)
mean, std, total_uncertainty, error = calculate_statistics(parameters,ub)

print(f"Średnia: {mean} \n")
print(f"Odchylenie standardowe: {std}\n")
print(f"Całkowita niepewność: {total_uncertainty}\n")
print(f"Błąd {error}\n")


