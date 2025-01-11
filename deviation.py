import numpy as np
from scipy.stats import t

def calculate_statistics(data, ub, confidence_level=0.95):
    n = len(data) 
    mean_value = np.mean(data)
    std_dev = np.std(data, ddof=1)
    total_uncertainty = np.sqrt(std_dev**2 + ub**2)
    
    dof = n - 1 
    t_student = t.ppf((1 + confidence_level) / 2, dof)
    
    margin_of_error = t_student * std_dev / np.sqrt(n)
    
    return mean_value, std_dev, total_uncertainty, margin_of_error
