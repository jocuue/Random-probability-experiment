trial = []
maximum_values = []

def collect_graphing_data(total_attempts, successful_attempts):
    probability = float(successful_attempts / total_attempts)
    trial.append(probability)
    maximum_values.append(total_attempts)
    return trial, maximum_values
