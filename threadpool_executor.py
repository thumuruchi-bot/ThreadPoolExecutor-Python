from concurrent.futures import ThreadPoolExecutor

def square(number):
    print(f"Task {number} Completed")
    return number * number

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(square, [1, 2]))

print("Results:", results)
