# # TODO for LOOP with LISTS
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# # TODO Average student height
# student_heights = input("Input a list of student heights divided by comma:\n").split(",")
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#
# total_height = 0
# num_of_students = 0
#
# for height in student_heights:
#     total_height += height
# for student in student_heights:
#     num_of_students += 1
#
# whole = round(total_height / num_of_students)
# print(f"Average height of these students is {whole} cm.")

# # TODO Highest student score
# student_scores = input("Input a list of student scores divided by comma:\n").split(",")
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#
# print(f"The highest score in the class is {highest_score}.")

# # TODO for LOOPS and range() FUNCTION
# # List of numbers
# for number in range(1, 10):
#     print(number)
#
# # List of numbers in range +3
# for number in range(1, 10, 3):
#     print(number)
#
# # Sum of some numbers
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# # TODO Adding Even Numbers
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# # TODO The FizzBuzz Job Interview
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
