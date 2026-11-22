user_name =input("Enter your name:")
numerical_score = int(input("Enter your energy score:"))
for count in range(3,0,-1):
    print(f"{count}...",end=" ") # used the line here so the countdown happens before the final answer and end=" " is used to keep the countdown in same line
    
print() # used to print a new line after the countdown ans <- must be aall the way to the left
if 90 <= numerical_score <= 100:
    print(f"Agent {user_name} has energy score {numerical_score} and is a Special Grade sorcerer")
elif 75 <= numerical_score <= 89:
    print(f"Agent {user_name} has energy score {numerical_score} and is a Grade 1 sorcerer")
elif 50 <= numerical_score <= 74:
    print(f"Agent {user_name} has energy score {numerical_score} and is a grade 2 sorcerer")
else:
    print(f"Agent {user_name} has energy score {numerical_score} and Remedial training required")

