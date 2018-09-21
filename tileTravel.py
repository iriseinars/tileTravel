
x = 1
y = 1
winner = False
valid_input = True


while not winner:
    if valid_input:
        if y == 1:
            print("You can travel: (N)orth.")
        elif x == y:
            print("You can travel: (S)outh or (W)est.")
        elif x == 1 and y == 2:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif x == 1 and y == 3:
            print("You can travel: (E)ast or (S)outh.")
        elif x == 2 and y == 3:
            print("You can travel: (E)ast or (W)est.")
        else:
            print("You can travel: (N)orth or (S)outh.") 

    direction = input("Direction: ")

    valid_input = True
    if y == 1:
        if direction.lower() == "n":
            valid_input = True
        else:    
            print("Not a valid direction!")
            valid_input = False
    elif x == y:
        if direction.lower() == "s" or direction.lower() == "w":
            valid_input = True
        else:
            print("Not a valid direction!")
            valid_input = False
    elif x == 1 and y == 2:
        if direction.lower() == "n" or direction.lower() == "e" or direction.lower() == "s":
            valid_input = True
        else:
            print("Not a valid direction!")
            valid_input = False 
    elif x == 1 and y == 3:
        if direction.lower() == "e" or direction.lower() == "s":
            valid_input = True 
        else:
            print("Not a valid direction!")
            valid_input = False 
    elif x == 2 and y == 3:
        if direction.lower() == "e" or direction.lower() == "w":
            valid_input = True  
        else:
            print("Not a valid direction!")
            valid_input = False
    else:
        if direction.lower() == "n" or direction.lower() == "s":
            valid_input = True 
        else:
            print("Not a valid direction!")
            valid_input = False        

    if valid_input:
        if direction.lower() == "n":
            y = y+1
        if direction.lower() == "e":
            x = x+1
        if direction.lower() == "s":
            y = y-1
        if direction.lower() == "w":
            x = x-1 
    
    if x == 3 and y == 1:
        print("Victory!")
        winner = True

           