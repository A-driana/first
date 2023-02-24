# # TODO Automatic pizza order program - first try
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# S_pizza_cost = 15
# M_pizza_cost = 20
# L_pizza_cost = 25
#
# pepperoni_S = 2
# pepperoni_M_L = 3
#
# cheese = 1
#
# bill = 0
#
# if size == "S":
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             bill = S_pizza_cost + pepperoni_S + cheese
#             print(f"Your final bill is {bill}€.")
#     if add_pepperoni == "N":
#         if extra_cheese == "Y":
#             bill = S_pizza_cost + cheese
#             print(f"Your final bill is {bill}€.")
#     if add_pepperoni == "Y":
#         if extra_cheese == "N":
#             bill = S_pizza_cost + pepperoni_S
#             print(f"Your final bill is {bill}€.")
#     else:
#         print(f"Your final bill is {S_pizza_cost}€.")
#
# if size == "M":
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             bill = M_pizza_cost + pepperoni_M_L + cheese
#             print(f"Your final bill is {bill}€.")
#     if add_pepperoni == "N":
#         if extra_cheese == "Y":
#             bill = M_pizza_cost + cheese
#             print(f"Your final bill is {bill}€.")
#     if add_pepperoni == "Y":
#         if extra_cheese == "N":
#             bill = M_pizza_cost + pepperoni_M_L
#             print(f"Your final bill is {bill}€.")
#     else:
#         print(f"Your final bill is {M_pizza_cost}€.")
#
# if size == "L":
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             bill = L_pizza_cost + pepperoni_M_L + cheese
#             print(f"Your final bill is {bill}€.")
#     if add_pepperoni == "N":
#         if extra_cheese == "Y":
#             bill = L_pizza_cost + cheese
#             print(f"Your final bill is {bill}€.")
#     if add_pepperoni == "Y":
#         if extra_cheese == "N":
#             bill = L_pizza_cost + pepperoni_M_L
#             print(f"Your final bill is {bill}€.")
#     else:
#         print(f"Your final bill is {L_pizza_cost}€.")

# # TODO Automatic pizza order program - easier way:
# # Small pizza = 15€, Medium pizza = 20€, Large pizza = 25€
# # Extra cheese +1€
# # Extra pepperoni for small pizza +2€
# # Extra pepperoni for medium and large pizza +3€
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is {bill}€.")
