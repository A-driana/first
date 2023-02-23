initial_height = input("Enter your height in m: ")
initial_weight = input("Enter your weight in kg: ")

height = float(initial_height)
weight = int(initial_weight)

result = weight / (height * height)

print(int(result))
