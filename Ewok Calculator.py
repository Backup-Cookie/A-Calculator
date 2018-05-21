
# what this Code dose

# in this code the player is able to + or - or * or / numbers
# just like a calculator

# The code gives random questions for the player to solve with numbers from 1 to 10

def Again(A):
    Again = True
    while Again == True:
        print("")
        print("Do you want to play agian?")
        Again = raw_input("Yes or No = ")
    
        if Again == "No":
            print("End Program")
            
        if Again == "Yes":
            print("")
            return Main()
def Main():
    import random
    
    Number_1 = [1,2,3,4,5,6,7,8,9,10]
    Number_2 = [1,2,3,4,5,6,7,8,9,10]
    Anwser = 0
    random.shuffle(Number_1)
    random.shuffle(Number_2)

    
    Addition = 1
    Subtraction = 2
    print("Random Question")
    print("Want type of questions do u want to do?")
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print
    print("Do you want to do your own Calculation")
    print("5 - Your own Calculation")
    print
    Game = input("What Number = ")
    print("")
    
    if Game >= 6:
        print ("That number isent assigned to anything")
        return Main()
    
    if Game == 1:
        print("Addition")
        print Number_1[0],
        print ("+"),
        print Number_2[0],
        print("=")
        Anwser = input("What is the Anwser")
        if Anwser == Number_1[0] + Number_2[0]:
            print ("You are Correct")
        if Anwser != Number_1[0] + Number_2[0]:
            print ("You are incorrect")
            print("The correct Anwser is"),
            print Number_1[0] + Number_2[0]
        Again(Game)
        
    if Game == 2:
        print("Subtraction")
        print Number_1[0],
        print ("-"),
        print Number_2[0],
        print("=")
        Anwser = input("What is the Anwser")
        if Anwser == Number_1[0] - Number_2[0]:
            print ("You are Correct")
        if Anwser != Number_1[0] - Number_2[0]:
            print ("You are incorrect")
            print("The correct Anwser is"),
            print Number_1[0] - Number_2[0]
        Again(Game)
        
    if Game == 3:
        print("Multiplication")
        print Number_1[0],
        print ("x"),
        print Number_2[0],
        print("=")
        Anwser = input("What is the Anwser")
        if Anwser == Number_1[0] * Number_2[0]:
            print ("You are Correct")
        if Anwser != Number_1[0] * Number_2[0]:
            print ("You are incorrect")
            print("The correct Anwser is"),
            print Number_1[0] * Number_2[0]
        Again(Game)
        
    if Game == 4:
        print("Division")
        print("Round down to the closest whole number")
        print Number_1[0],
        print ("÷"),
        print Number_2[0],
        print("=")
        Anwser = input("What is the Anwser")
        if Anwser == Number_1[0] / Number_2[0]:
            print ("You are Correct")
        if Anwser != Number_1[0] / Number_2[0]:
            print ("You are incorrect")
            print("The correct Anwser is"),
            print Number_1[0] / Number_2[0]
        Again(Game)
        
    if Game == 5:
        print("Creat your own Equation")
        print("1 = Addition")
        print("2 = Subtraction")
        print("3 = Multiplication")
        print("4 = Division")
        Math = input("what type of Arithmetic Operations do you want to use? = ")
        if Math >= 5:
            print ("That number isent assigned to anything")
            Again(Game)
            return
        One = input("What your first Number? = ")
        Two = input("Whats your second Number? = ")

        if Math == 1:
            # Addition
            print One,
            print ("+"),
            print Two,
            print("="),
            print One + Two
            
        if Math == 2:
            #Subtraction
            print One,
            print ("-"),
            print Two,
            print("="),
            print One - Two
            
        if Math == 3:
            #Multiplication
            print One,
            print ("x"),
            print Two,
            print("="),
            print One * Two
            
        if Math == 4:
            #Division
            print One,
            print ("÷"),
            print Two,
            print("="),
            print One / Two
            
        Again(Game)

Main()
