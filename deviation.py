import numpy as np

# Zadanie A: Obliczenia dla wysokości i energii potencjalnej
def calculate_statistics(data, ub):
    mean_value = np.mean(data)
    std_dev = np.std(data, ddof=1)  # Odchylenie standardowe z n-1
    total_uncertainty = np.sqrt(std_dev**2 + ub**2)
    return mean_value, std_dev, total_uncertainty