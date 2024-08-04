import statistics
import random


def mean(data):
    return statistics.mean(data)

def median(data):
    return statistics.median(data)

def mode(data):
    return statistics.mode(data)

def std_dev(data):
    return statistics.stdev(data)


def analyze_data(data, operation):
    if operation in data_analysis_functions:
        return data_analysis_functions[operation](data)
    
    
data_analysis_functions = {
    "mean": mean,
    "median": median,
    "mode": mode,
    "standard_deviation": std_dev
}


data = [random.randint(1, 100) for _ in range(12)]


operation = input("Write analyze data:\t").lower()

if operation == "mean":
    print("All generated numbers:", data)
    print("Mean:", analyze_data(data, 'mean'))
    

elif operation == "median":
    print("All generated numbers:", data)
    print("Median:", analyze_data(data, 'median'))

elif operation == "mode":
    print("All generated numbers:", data)
    print("Mode:", analyze_data(data, 'mode'))

elif operation == "standard":
    print("All generated numbers:", data)
    print("Standard Deviation:", analyze_data(data, 'standard_deviation'))


else:
    print("Operation not found!")