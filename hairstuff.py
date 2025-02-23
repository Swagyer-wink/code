Hair_length = input("What is the length of your hair: \n")




if Hair_length == "long":
    print("you need to maintan its health")
elif Hair_length == "medium": 
    print("you need use use some product")
else:
    print("you have short hair")
if Hair_length == "long":
    hair_conditon = (input("is your hair damaged?: \n"))
    if hair_conditon == "yes":
        print("go buy some product or it will die intirely")
    else:
        print("good make sure it doesnt become damaged")
if Hair_length == "short":
    Hair_value = (input("is it going bald or do you keep it short? \n"))
    if Hair_value == "going bald":
        print("you should go see a hair technition about a wig or translplant")
    else:
        print("good luck with keeping it in check")



if Hair_length == "medium":
    hair_dying = (input("is your hair going short, or is it styled like that? \n"))
    if hair_dying == "going short":
        scared = (input("are you wanting it to go short? \n")) 
        if scared == "yes":
            ellse = print("find some good styles for yourself")
        else:
            print("you might want to get help before you go bald")

    
