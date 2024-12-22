import math

def get_input(prompt, is_weight=False):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "":
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

    for i in range(n):
        value = get_input(f"Podaj wartość nr {i+1}: ")
        weight = get_input(f"Podaj wagę dla wartości nr {i+1} (jeśli brak, przypiszemy wagę 1): ", is_weight=True)
        if weight == 1: 
            print(f"Przypisano wagę 1 dla wartości {value}.")
        values.append(value)
        weights.append(weight if weight != 1 else 1)

    weighted_mean = sum(v * w for v, w in zip(values, weights)) / sum(weights)
    variance = sum(w * (v - weighted_mean) ** 2 for v, w in zip(values, weights)) / sum(weights)
    std_deviation = math.sqrt(variance)

    print(f"\nŚrednia ważona: {weighted_mean}")
    print(f"Odchylenie standardowe: {std_deviation}")

if __name__ == "__main__":
    main()
