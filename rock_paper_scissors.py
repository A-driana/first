# # TODO Rock, paper, scissors
# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# lizard = '''
#                     .
#       _.--._       /|
#     .'()..()`.    / /
#    ( `-.__.-' )  ( (
#     \        /    \ )
#      \      /      ) )
#    .' -.__.- `.-.-'_.'
#  .'  /-____-\  `.-'
#  \  /-.____.-\  /-.
#   \ \`-.__.-'/ /\|\|
#   .'  `.   .'  `.
#   |/\/\|   |/\/\|
# '''
#
# Spock = '''
#                       _
#                      | |
#  ___ _ __   ___   ___| | __
# / __| '_ \ / _ \ / __| |/ /
# \__ \ |_) | (_) | (__|   <
# |___/ .__/ \___/ \___|_|\_)
#     | |
#     |_|
# '''
#
# game_images = [rock, paper, scissors, lizard, Spock]
#
# user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, 2 for Scissors, 3 for lizard, "
#                         "4 for Spock.\n"))
# if user_choice >= 5 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# else:
#     print(game_images[user_choice])
#
#     computer_choice = random.randint(0, 4)
#     print("Computer chose:")
#     print(game_images[computer_choice])

# #  TODO Clean the code

#     if user_choice == computer_choice:
#         print("It's a draw.")
#     elif user_choice == 0:
#         if computer_choice == 1:
#             print("You lose!")
#         if computer_choice == 2:
#             print("You win!")
#         if computer_choice == 3:
#             print("You win!")
#         if computer_choice == 4:
#             print("You lose!")
#     elif user_choice == 1:
#         if computer_choice == 0:
#             print("You win!")
#         if computer_choice == 2:
#             print("You lose!")
#         if computer_choice == 3:
#             print("You lose!")
#         if computer_choice == 4:
#             print("You win!")
#     elif user_choice == 2:
#         if computer_choice == 0:
#             print("You lose!")
#         if computer_choice == 1:
#             print("You win!")
#         if computer_choice == 3:
#             print("You win!")
#         if computer_choice == 4:
#             print("You lose!")
#     elif user_choice == 3:
#         if computer_choice == 0:
#             print("You lose!")
#         if computer_choice == 1:
#             print("You win!")
#         if computer_choice == 2:
#             print("You lose!")
#         if computer_choice == 4:
#             print("You win!")
#     elif user_choice == 4:
#         if computer_choice == 0:
#             print("You win!")
#         if computer_choice == 1:
#             print("You lose!")
#         if computer_choice == 2:
#             print("You win!")
#         if computer_choice == 3:
#             print("You lose!")
#     else:
#         print("Your did something wrong.")
