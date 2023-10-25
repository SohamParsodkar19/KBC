import random

choices = [ "Rock", "Paper", "Scissors"]
user_win_matrix = [ 
                   ['D', 'L', 'W'],
                   ['W', 'D', 'L'],
                   ['L', 'W', 'D'],
]

dict_points = {'R':0, 'P':1, 'S':2}

user = input(" Choose your option : ")

computer = random.choice(choices)
print(f"The computer has selected : {computer}")

result = user_win_matrix[dict_points[user[0]]][dict_points[computer[0]]]

if( result == 'W'):
    print("Congratulations!!! You have won")
elif(result == 'L'):
    print("Oops!!! You lost the game.")
else:
    print("Its a draw!!!")