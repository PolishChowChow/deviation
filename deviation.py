import math
from scipy import stats

def get_input(prompt, is_weight=False, is_uncertainty=False):
    while True:
        user_input = input(prompt)
        
        if user_input.strip() == "":
            if is_weight:
                return 1
            elif is_uncertainty:
                return 0
            else:
                print("Błąd: Wartość nie może być pusta.")
                continue
        
        try:
            value = float(user_input)
            if is_weight and value <= 0:
                print("Błąd: Waga musi być dodatnia.")
                continue
            return value
        except ValueError:
            print("Błąd: Proszę podać liczbę.")

def main():
    n = int(get_input("Ile danych chcesz wprowadzić? "))
    values = []
    weights = []

    uncertainty_b = get_input("Podaj niepewność typu B (dla wszystkich pomiarów): ", is_uncertainty=True)

    for i in range(n):
        value = get_input(f"Podaj wartość nr {i+1}: ")
        weight = get_input(f"Podaj wagę dla wartości nr {i+1} (jeśli brak, przypiszemy wagę 1): ", is_weight=True)
        
        print(f"Przypisano wagę {weight} i niepewność typu B {uncertainty_b} dla wartości {value}.")
        
        values.append(value)
        weights.append(weight)

    weighted_mean = sum(v * w for v, w in zip(values, weights)) / sum(weights)

    variance = sum(w * (v - weighted_mean) ** 2 for v, w in zip(values, weights)) / sum(weights)
    std_deviation = math.sqrt(variance)

    if n > 1:
        t_value = stats.t.ppf(0.975, n-1)
        std_deviation *= t_value / math.sqrt(n)

    total_uncertainty = math.sqrt(std_deviation**2 + uncertainty_b**2)

    print(f"\nŚrednia ważona: {weighted_mean}")
    print(f"Odchylenie standardowe (niepewność typu A): {std_deviation}")
    print(f"Całkowita niepewność (A + B): {total_uncertainty}")

if __name__ == "__main__":
    main()
