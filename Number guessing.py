import random 
print("Hello")
b=random.randint(1,100)
while True:
    user_input=input("Guess a number between 1 to 100:")
    try:
        if user_input.isdigit():
            a=int(user_input)
            if a>b:
                print("it's high")
            elif a<b:
                print("it's low")
            elif a==b:
                print("Fantastic...! That's Correct..")
            else:
                print("Something went wrong")
                
            
        else:
            print("Please check your input")


    except Exception as e:
        print("Error:",e)
