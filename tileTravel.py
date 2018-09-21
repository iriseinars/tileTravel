tala1 = 1
tala2 = 1

#Segir til hvort maður sé sigurvegari
def winner(x, y):
    if x == 3 and y == 1:
        print("Victory!")
        return True
    else:
        return False


#Segir til um hvaða átt þú getur farið í
def compass(x, y):
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

#Segir til um hvort notandi hafi valið gildann möguleika
def valid_input(x, y, direction):
    if y == 1:
        if direction.lower() == "n":
            return True
        else:    
            print("Not a valid direction!")
            return False
    elif x == y:
        if direction.lower() == "s" or direction.lower() == "w":
            return True
        else:
            print("Not a valid direction!")
            return False
    elif x == 1 and y == 2:
        if direction.lower() == "n" or direction.lower() == "e" or direction.lower() == "s":
            return True
        else:
            print("Not a valid direction!")
            return False 
    elif x == 1 and y == 3:
        if direction.lower() == "e" or direction.lower() == "s":
            return True 
        else:
            print("Not a valid direction!")
            return False 
    elif x == 2 and y == 3:
        if direction.lower() == "e" or direction.lower() == "w":
            return True  
        else:
            print("Not a valid direction!")
            return False
    else:
        if direction.lower() == "n" or direction.lower() == "s":
            return True 
        else:
            print("Not a valid direction!")
            return False        


                     
#Hreyfir leikmann á næsta reit út frá því hvað notandi valdi
def move(x, y, direction):
    if direction.lower() == "n":
        return x, y+1
    if direction.lower() == "e":
        return x+1, y
    if direction.lower() == "s":
        return x, y-1
    if direction.lower() == "w":
        return x-1, y    


good_input = True

while not winner(tala1, tala2):
    if good_input:
        compass(tala1, tala2)
    direction = input("Direction: ")
    good_input = valid_input(tala1, tala2, direction)

    if good_input:
        tala1, tala2 = move(tala1, tala2, direction)
        








 